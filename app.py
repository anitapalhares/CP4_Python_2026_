import json
import pandas as pd
import streamlit as st

def read_uploaded_file(uploaded_file) -> pd.DataFrame:
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        return pd.read_csv(uploaded_file)

    if file_name.endswith(".txt"):
        return pd.read_txt(uploaded_file)

    if file_name.endswith(".json"):
        try:
            return pd.read_json(uploaded_file)
        except ValueError:
            uploaded_file.seek(0)
            data = json.load(uploaded_file)
            return pd.DataFrame(data)

    raise ValueError("Envie um arquivo CSV, JSON ou TXT.")


def convert_dataframe(df: pd.DataFrame, output_format: str, json_orient: str) -> tuple[str, str, str]:
    if output_format == "CSV":
        data = df.to_csv(index=False, encoding="utf-8")
        return data, "dados_convertidos.csv", "text/csv"

    if output_format == "TXT":
        data = df.to_csv(index=False, sep="\t")
        return data, "dados_convertidos.txt", "text/plain"

    data = df.to_json(orient=json_orient, indent=4, force_ascii=False)
    return data, "dados_convertidos.json", "application/json"


st.title("Data App - Conversor de Dados")
st.subheader("CSV ↔ JSON com Pandas e Streamlit")

st.write(
    "Envie um arquivo CSV, JSON ou TXT para visualizar os dados em tabela e baixar uma versão convertida."
)

st.write("Kauã, Anita e Vitória.")

uploaded_file = st.file_uploader("Arquivo CSV, JSON ou TXT", type=["csv", "json", "txt"])

try:
    if uploaded_file is not None:
        df = read_uploaded_file(uploaded_file)
        st.caption(f"Arquivo carregado: {uploaded_file.name}")
    else:
        st.info("Envie um arquivo para começar.")
        st.stop()

    st.divider()

    col_metric_1, col_metric_2 = st.columns(2)
    col_metric_1.metric("Linhas", df.shape[0])
    col_metric_2.metric("Colunas", df.shape[1])

    st.dataframe(df, width="stretch")

    st.divider()
    st.subheader("Converter e baixar")

    col_format, col_orient = st.columns(2)
    output_format = col_format.selectbox("Formato de saída", ["CSV", "JSON"])
    json_orient = col_orient.selectbox(
        "Orientação do JSON",
        ["records", "columns", "table"],
        disabled=output_format != "JSON",
    )

    converted_data, file_name, mime_type = convert_dataframe(df, output_format, json_orient)

    st.download_button(
        "Baixar arquivo convertido",
        data=converted_data.encode("utf-8"),
        file_name=file_name,
        mime=mime_type,
    )

    with st.expander("Prévia do arquivo convertido"):
        st.code(converted_data, language="json" if output_format == "JSON" else "csv")


except Exception as error:
    st.error(f"Não foi possível converter o arquivo: {error}")