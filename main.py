"""

MAIN - Ponto de entrada da aplicação

"""

import streamlit as st

import os

from src.database import MongoDB



# Configuração da página

st.set_page_config(

    page_title="CFIS Financeiro",

    page_icon="💰",

    layout="wide"

)

# Verifica conexão MongoDB
try:
    sucesso, mensagem = MongoDB.testar_conexao()
    if sucesso:
        st.sidebar.success(f"✅ MongoDB conectado")
    else:
        st.sidebar.error(f"❌ MongoDB: {mensagem}")
except Exception as e:
    st.sidebar.error(f"❌ MongoDB: {e}")

# Definição das páginas (comentadas até serem criadas)

pages = {

    "Página Inicial": [

        st.Page("pages/home.py", title="Home")

    ],

    "Cadastros": [

        st.Page("pages/cadastros/cadastrosinstrumentos.py", title="Instrumentos"),

        st.Page("pages/cadastros/pgfornecedores.py", title="Fornecedores"),

        st.Page("pages/cadastros/pgfuncionarios.py", title="Funcionários")

    ],

    "Diárias": [

        st.Page("pages/diarias/pgdiarias.py", title="Recibos"),

        st.Page("pages/diarias/pgpgtodiarias.py", title="Pagamentos"),

        st.Page("pages/diarias/pghomediarias.py", title="Home Diárias"),

        st.Page("pages/diarias/pgrelatoriosdiarias.py", title="Relatórios")

    ],

    "Provisionamento": [

        st.Page("pages/provisionamento/pgprovisionamento.py", title="Geral"),

        st.Page("pages/provisionamento/pgprovisionamentocd.py", title="Custo Direto"),

        st.Page("pages/provisionamento/pgprovisionamentoci.py", title="Custo Indireto"),

        st.Page("pages/provisionamento/pgprovisionamentopessoal.py", title="Pessoal")

    ],

    "Pagamentos": [

        st.Page("pages/pagamentos/pgconsumo.py", title="Consumo"),

        st.Page("pages/pagamentos/pgservicos.py", title="Serviços"),

        st.Page("pages/pagamentos/pgveiculos.py", title="Veículos"),

        st.Page("pages/pagamentos/pgeventoscd.py", title="Eventos"),

        st.Page("pages/pagamentos/pgmanutencoes.py", title="Manutenções"),

        st.Page("pages/pagamentos/pgservieventuais.py", title="Serviços Eventuais")

    ],

    "Repasses": [

        st.Page("pages/pgrepasses.py", title="Cronograma")

    ]

}



# Navegação

pg = st.navigation(pages)



# Informações na sidebar

with st.sidebar:

    st.markdown("---")

    st.markdown("### ℹ️ Informações")

    st.info("Sistema de gestão financeira CFIS")

    

    # Versão

    st.caption("Versão 2.0.0 (MongoDB + Cloud)")

    

    # Ambiente

    if 'STREAMLIT_SERVER_BASE_URL' in os.environ:

        st.warning("☁️ Rodando na Cloud")

    else:

        st.info("🏠 Rodando Localmente")



# Executa a página

pg.run()

