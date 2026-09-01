import json
import pandas as pd
import streamlit as st


def texto_para_dataframe(texto):
    texto = texto.strip()

    if "=" in texto and not texto.startswith(("{", "[")):
        texto = texto.split("=", 1)[1].strip()

    dados = eval(texto, {"__builtins__": {}}, {})

    if isinstance(dados, dict) and "data" in dados:
        dados = dados["data"]

    if isinstance(dados, dict):
        return pd.DataFrame(dados)

    if isinstance(dados, list):
        return pd.DataFrame(dados)

    raise ValueError("Digite um dict ou array/lista Python válido.")


st.title("Data App")
st.subheader("DEV.AK")

if "df" not in st.session_state:
    st.session_state["df"] = None

try:
    texto = st.text_area(
        "Digite um dict ou array/lista Python",
        "dicionario = {'nome': ['Ana', 'Bruno'], 'idade': [20, 25]}",
    )
    arquivo = st.file_uploader(
        "Ou envie um arquivo CSV, JSON, XLSX ou PY",
        type=["csv", "json", "xlsx", "py"],
    )

    col_texto, col_arquivo = st.columns(2)

    if col_texto.button("Carregar texto"):
        if texto.strip():
            st.session_state["df"] = texto_para_dataframe(texto)
        else:
            st.error("Digite um dict/lista Python.")

    if col_arquivo.button("Carregar arquivo"):
        if not arquivo:
            st.error("Envie um arquivo.")
        else:
            nome = arquivo.name.lower()

            if nome.endswith(".csv"):
                st.session_state["df"] = pd.read_csv(arquivo)
            elif nome.endswith(".xlsx"):
                st.session_state["df"] = pd.read_excel(arquivo)
            elif nome.endswith(".py"):
                texto_py = arquivo.getvalue().decode("utf-8")
                st.session_state["df"] = texto_para_dataframe(texto_py)
            else:
                dados = json.load(arquivo)
                if isinstance(dados, dict) and "data" in dados:
                    dados = dados["data"]
                st.session_state["df"] = pd.DataFrame(dados)

    df = st.session_state["df"]

    if df is not None:
        st.subheader("Dados carregados")
        st.dataframe(df)

        formato = st.selectbox("Converter para", ["JSON", "CSV", "XLSX"])

        if formato == "JSON":
            conteudo = df.to_json(orient="records", indent=4, force_ascii=False)
            arquivo_saida = "dados.json"
            tipo = "application/json"
            download = conteudo.encode("utf-8")
            st.code(conteudo)

        elif formato == "CSV":
            conteudo = df.to_csv(index=False)
            arquivo_saida = "dados.csv"
            tipo = "text/csv"
            download = conteudo.encode("utf-8")
            st.code(conteudo)

        else:
            conteudo = pd.io.common.BytesIO()
            df.to_excel(conteudo, index=False)
            arquivo_saida = "dados.xlsx"
            tipo = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            download = conteudo.getvalue()

        st.download_button("Baixar arquivo", data=download, file_name=arquivo_saida, mime=tipo)

except Exception as erro:
    st.error(f"Erro: {erro}")
    st.error(f"Tipo: {type(erro).__name__}")
