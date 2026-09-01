# CP4 - Data App

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)

> Ferramenta web para conversão, visualização e manipulação de dados em diferentes formatos.

## Repositorio

https://github.com/anitapalhares/CP4_Python_2026_

---

## Sobre

O **Data App** é uma ferramenta desenvolvida em Python que permite realizar a conversão de dados entre diferentes formatos de arquivos.

A aplicação utiliza **Pandas** para manipulação dos dados e **Streamlit** para criar uma interface web simples, intuitiva e visualmente agradável, com identidade visual própria inspirada no estilo **DEV.AK**.

O projeto foi desenvolvido para o **Checkpoint 4 — Computational Thinking With Python**, com foco na manipulação de dados, arquivos, conversões e tratamento de erros.

---

## Funcionalidades

- Entrada de dados por texto: digitação direta de um **dict** ou **lista/array Python** em uma caixa de texto, sem necessidade de enviar arquivo
- Upload de arquivo **.py** contendo um dict ou lista Python, que é interpretado automaticamente
- Upload de arquivos nos formatos **CSV**, **JSON** e **XLSX**
- Reconhecimento automático de dados aninhados em uma chave `"data"` (ex.: `{"data": [...]}`), tanto em JSON quanto em dict/texto
- Conversão de saída para **JSON**, **CSV** ou **XLSX**, a partir de qualquer um dos formatos de entrada suportados (conversão N para N, não apenas pares fixos)
- Visualização dos dados carregados em formato de tabela (prévia)
- Prévia do conteúdo convertido antes do download (JSON e CSV)
- Download do arquivo já convertido, com o tipo MIME correto para cada formato
- Manutenção dos dados carregados entre interações através de `st.session_state`
- Tratamento de erros e exceções durante leitura e conversão, exibindo a mensagem do erro e o tipo da exceção

---

## Interface Visual

A aplicação possui um layout customizado, com estilo próprio inspirado na identidade **DEV.AK**:

- Fundo branco com um gradiente roxo suave no canto superior esquerdo
- Paleta de cores baseada em tons de roxo (`#9b8cff` e `#6c5ce7`) e preto (`#111111`)
- Tipografia com títulos em negrito e espaçamento reduzido entre letras
- Campos de texto, área de upload, botões e seletor de formato estilizados com bordas arredondadas e destaque roxo ao interagir
- Botões com efeito de elevação (sombra e leve deslocamento) ao passar o mouse
- Rodapé padrão do Streamlit ocultado para um visual mais limpo

---

## Estrutura do Projeto

```text
CP4_Python_2026
│
├── Arquivos/
├── app.py
├── requirements.txt
└── README.md
```

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/anitapalhares/CP4_Python_2026_.git
```

2. Acesse a pasta do projeto:

```bash
cd CP4_Python_2026_
```

3. Crie um ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

5. Instale as dependências:

```bash
pip install -r requirements.txt
```

6. Execute a aplicação:

```bash
streamlit run app.py
```

---

## Como Utilizar

1. Digite um dict ou lista Python na caixa de texto **ou** envie um arquivo nos formatos CSV, JSON, XLSX ou PY
2. Clique em **Enviar**
3. Os dados carregados serão exibidos em uma tabela de prévia
4. Selecione o formato de saída desejado (JSON, CSV ou XLSX)
5. Confira a prévia do conteúdo convertido (quando aplicável) e clique em **Baixar**
6. Caso algum erro ocorra durante o processo, uma mensagem com a descrição e o tipo do erro será exibida na tela

---

## Tratamento de Erros

A aplicação foi desenvolvida prevendo cenários como:

- Texto digitado que não representa um dict ou lista Python válida
- Arquivos em formatos não suportados ou corrompidos
- Ausência de texto ou arquivo enviado no momento do envio
- Falhas durante o processo de leitura ou conversão dos dados

Em todos esses casos, o erro é capturado e exibido de forma clara para o usuário, junto com o tipo da exceção ocorrida, sem interromper a execução da aplicação.

---

## Tecnologias Utilizadas

- Python
- Pandas
- Streamlit
- Git e GitHub
- VS Code

---

## Conclusão

O **Data App** cumpre os objetivos propostos no Checkpoint 4, aplicando na prática conceitos de manipulação de dados e arquivos com Python. A ferramenta oferece conversão entre múltiplos formatos, entrada de dados via texto ou arquivo, interface visual personalizada e tratamento robusto de erros, entregando uma solução funcional e de fácil utilização.

---

## Integrantes

| Integrante |
|---|
| **Kauã Coelho Pacheco** |
| **Vitória Kereski da Rosa** |
| **Anita Palhares** |
