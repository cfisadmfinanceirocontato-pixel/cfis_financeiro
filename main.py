"""
MAIN - Ponto de entrada da aplicação (versão compatível com Streamlit antigo)
"""
import streamlit as st
import os
from pathlib import Path


st.write(f"Versão do Streamlit: {st.__version__}")

# Configuração da página (DEVE ser a primeira linha)
st.set_page_config(
    page_title="CFIS Financeiro",
    page_icon="💰",
    layout="wide"
)

# Título na sidebar
st.sidebar.title("💰 CFIS Financeiro")

# Verifica conexão MongoDB (opcional)
try:
    from src.database import MongoDB
    sucesso, mensagem = MongoDB.testar_conexao()
    if sucesso:
        st.sidebar.success("✅ MongoDB conectado")
    else:
        st.sidebar.error(f"❌ MongoDB: {mensagem}")
except Exception as e:
    st.sidebar.warning("⚠️ MongoDB não disponível (use app_teste.py para testar)")

# Definição das páginas no formato ANTIGO (sem st.Page)
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Navegação")

# Usando radio buttons para navegação (funciona em qualquer versão)
opcao = st.sidebar.radio(
    "Ir para:",
    ["🏠 Home", 
     "📋 Cadastros",
     "💰 Diárias",
     "📊 Provisionamento",
     "🔧 Teste"]
)

# Carrega a página correspondente
if opcao == "🏠 Home":
    try:
        from pages.home import main as home_main
        home_main()
    except:
        st.title("🏠 Home")
        st.write("Página Home em construção")
        
elif opcao == "📋 Cadastros":
    st.title("📋 Cadastros")
    tab1, tab2, tab3 = st.tabs(["Instrumentos", "Fornecedores", "Funcionários"])
    
    with tab1:
        st.write("Cadastro de Instrumentos")
        # Tenta importar se existir
        try:
            from pages.cadastros.cadastrosinstrumentos import main as inst_main
            inst_main()
        except:
            st.info("Módulo de instrumentos em construção")
    
    with tab2:
        st.write("Cadastro de Fornecedores")
        try:
            from pages.cadastros.pgfornecedores import main as forn_main
            forn_main()
        except:
            st.info("Módulo de fornecedores em construção")
    
    with tab3:
        st.write("Cadastro de Funcionários")
        try:
            from pages.cadastros.pgfuncionarios import main as func_main
            func_main()
        except:
            st.info("Módulo de funcionários em construção")
            
elif opcao == "💰 Diárias":
    st.title("💰 Diárias")
    tab1, tab2 = st.tabs(["Recibos", "Pagamentos"])
    
    with tab1:
        try:
            from pages.diarias.pgdiarias import main as diarias_main
            diarias_main()
        except:
            st.info("Módulo de recibos em construção")
    
    with tab2:
        try:
            from pages.diarias.pgpgtodiarias import main as pgto_main
            pgto_main()
        except:
            st.info("Módulo de pagamentos em construção")
            
elif opcao == "📊 Provisionamento":
    st.title("📊 Provisionamento")
    try:
        from pages.provisionamento.pgprovisionamentocd import main as prov_main
        prov_main()
    except:
        st.info("Módulo de provisionamento em construção")
        
elif opcao == "🔧 Teste":
    st.title("🔧 Página de Teste")
    st.write("### Informações do Sistema:")
    st.write(f"- Python: {os.sys.version}")
    st.write(f"- Streamlit: {st.__version__}")
    
    try:
        import pymongo
        st.success(f"✅ pymongo {pymongo.__version__}")
    except:
        st.error("❌ pymongo não instalado")

# Informações na sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### ℹ️ Informações")
    st.info("Sistema de gestão financeira CFIS")
    st.caption(f"Streamlit v{st.__version__}")
    
    if 'STREAMLIT_SERVER_BASE_URL' in os.environ:
        st.warning("☁️ Rodando na Cloud")
    else:
        st.info("🏠 Rodando Localmente")