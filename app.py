import json
import pandas as pd
import streamlit as st

 
st.set_page_config(page_title="Data App | DEV.AK", page_icon="🟣", layout="centered")
 
# ---------- ESTILO DEV.AK ----------
st.markdown(
    """
    <style>
        :root {
            --dev-purple: #9b8cff;
            --dev-purple-dark: #6c5ce7;
            --dev-black: #111111;
        }
 
        html, body, [data-testid="stAppViewContainer"] {
            background: #ffffff;
            color: var(--dev-black);
        }
 
        /* Bola roxa clara em degradê no canto superior esquerdo */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed;
            top: -180px;
            left: -180px;
            width: 480px;
            height: 480px;
            background: radial-gradient(circle at center, rgba(155,140,255,0.55) 0%, rgba(155,140,255,0.25) 45%, rgba(255,255,255,0) 75%);
            border-radius: 50%;
            z-index: 0;
            pointer-events: none;
        }
 
        [data-testid="stHeader"] {
            background: transparent;
        }
 
        .block-container {
            position: relative;
            z-index: 1;
            padding-top: 3rem;
        }
 
        h1, h2, h3 {
            color: var(--dev-black) !important;
            font-weight: 800 !important;
            letter-spacing: -0.5px;
        }
 
        h1 {
            font-size: 2.4rem !important;
        }
 
        h1 span.accent {
            color: var(--dev-purple-dark);
        }
 
        p, label, .stMarkdown, .stCaption {
            color: #333333;
        }
 
        /* Inputs */
        .stTextArea textarea, .stTextInput input {
            border: 1.5px solid #e4defc !important;
            border-radius: 10px !important;
            background-color: #fafaff !important;
        }
 
        .stTextArea textarea:focus, .stTextInput input:focus {
            border-color: var(--dev-purple-dark) !important;
            box-shadow: 0 0 0 2px rgba(100, 92, 231, 0.35) !important;
        }
 
        /* File uploader */
        [data-testid="stFileUploaderDropzone"] {
            border: 1.5px dashed var(--dev-purple) !important;
            background-color: #faf9ff !important;
            border-radius: 12px !important;
        }
        /* Botão "Browse files" do uploader */
        [data-testid="stFileUploaderDropzone"] button {
            background: linear-gradient(135deg, var(--dev-purple) 0%, var(--dev-purple-dark) 100%) !important;
            color: #ffffff !important;
            border: none !important;
            border-radius: 10px !important;
            font-weight: 600 !important;
            box-shadow: 0 4px 14px rgba(108, 92, 231, 0.25);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }

        [data-testid="stFileUploaderDropzone"] button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 18px rgba(108, 92, 231, 0.35);
            color: #ffffff !important;
        }
 
        /* Botões */
        .stButton > button, .stDownloadButton > button {
            background: linear-gradient(135deg, var(--dev-purple) 0%, var(--dev-purple-dark) 100%);
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 0.5rem 1.2rem;
            font-weight: 600;
            transition: transform 0.15s ease, box-shadow 0.15s ease;
            box-shadow: 0 4px 14px rgba(108, 92, 231, 0.25);
        }
 
        .stButton > button:hover, .stDownloadButton > button:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 18px rgba(100, 92, 231, 0.35);
            color: #ffffff;
        }
 
        /* Selectbox */
        [data-baseweb="select"] > div {
            border-radius: 10px !important;
            border-color: #e4defc !important;
        }
 
        /* Dataframe */
        [data-testid="stDataFrame"] {
            border: 1px solid #ece9ff;
            border-radius: 12px;
            overflow: hidden;
        }
 
        /* Code block */
        .stCodeBlock, pre {
            border-radius: 10px !important;
            border: 1px solid #ece9ff !important;
        }
 
        /* Divider sutil */
        hr {
            border-color: #ece9ff;
        }
 
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
# ---------- FIM ESTILO ----------


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
