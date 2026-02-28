"""
MAIN - Ponto de entrada da aplicação (versão compatível)
"""
import streamlit as st
import os

# Configuração da página (DEVE ser a primeira linha)
st.set_page_config(
    page_title="CFIS Financeiro",
    page_icon="💰",
    layout="wide"
)

# Título na sidebar
st.sidebar.title("💰 CFIS Financeiro")

# Verifica conexão MongoDB (opcional, pode comentar se der erro)
try:
    from src.database import MongoDB
    sucesso, mensagem = MongoDB.testar_conexao()
    if sucesso:
        st.sidebar.success("✅ MongoDB conectado")
    else:
        st.sidebar.error(f"❌ MongoDB: {mensagem}")
except Exception as e:
    st.sidebar.warning("⚠️ MongoDB não disponível (ignore se for o app de teste)")

# Menu de navegação manual (em vez de st.Page)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 MENU")

# Páginas disponíveis
paginas = {
    "🏠 Home": "pages/home.py",
    "📋 Instrumentos": "pages/cadastros/cadastrosinstrumentos.py",
    "🏢 Fornecedores": "pages/cadastros/pgfornecedores.py",
    "👥 Funcionários": "pages/cadastros/pgfuncionarios.py",
    "📄 Recibos": "pages/diarias/pgdiarias.py",
    "💰 Pagamentos": "pages/diarias/pgpgtodiarias.py",
    "📊 Provisionamento": "pages/provisionamento/pgprovisionamentocd.py",
}

# Selectbox para navegação
pagina_selecionada = st.sidebar.selectbox(
    "Ir para:",
    options=list(paginas.keys())
)

# Informações na sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### ℹ️ Informações")
    st.info("Sistema de gestão financeira CFIS")
    st.caption("Versão 2.0.0 (MongoDB + Cloud)")
    
    if 'STREAMLIT_SERVER_BASE_URL' in os.environ:
        st.warning("☁️ Rodando na Cloud")
    else:
        st.info("🏠 Rodando Localmente")

# Executa a página selecionada
caminho_pagina = paginas[pagina_selecionada]

# Verifica se o arquivo existe
if os.path.exists(caminho_pagina):
    with open(caminho_pagina, 'r', encoding='utf-8') as f:
        codigo = f.read()
    exec(codigo)
else:
    st.error(f"❌ Página não encontrada: {caminho_pagina}")
    st.info("Use o app_teste.py para testar a conexão primeiro.")