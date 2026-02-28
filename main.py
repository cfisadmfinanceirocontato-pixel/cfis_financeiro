"""
MAIN - Ponto de entrada da aplicação
CORRIGIDO: set_page_config é o primeiro comando
"""
import streamlit as st

# ⚠️ PRIMEIRÍSSIMA COISA: configurar a página
st.set_page_config(
    page_title="CFIS Financeiro",
    page_icon="💰",
    layout="wide"
)

# ✅ AGORA SIM: outros imports
import os
from pathlib import Path

# Tentativa de importar MongoDB (com try/except para evitar erros)
try:
    from src.database import MongoDB
    mongodb_disponivel = True
except Exception as e:
    mongodb_disponivel = False
    print(f"Erro ao importar MongoDB: {e}")

# Título na sidebar
st.sidebar.title("💰 CFIS Financeiro")

# Verifica conexão MongoDB
with st.sidebar:
    try:
        if mongodb_disponivel:
            sucesso, mensagem = MongoDB.testar_conexao()
            if sucesso:
                st.success("✅ MongoDB conectado")
            else:
                st.error(f"❌ MongoDB: {mensagem}")
        else:
            st.warning("⚠️ MongoDB não disponível")
    except Exception as e:
        st.warning("⚠️ Erro na conexão")

# Menu de navegação
st.sidebar.markdown("---")
st.sidebar.markdown("### 📋 Navegação")

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
    st.title("🏠 Home")
    try:
        from pages.home import main as home_main
        home_main()
    except:
        st.info("Página Home em construção")

elif opcao == "📋 Cadastros":
    st.title("📋 Cadastros")
    tab1, tab2, tab3 = st.tabs(["Instrumentos", "Fornecedores", "Funcionários"])
    
    with tab1:
        try:
            from pages.cadastros.cadastrosinstrumentos import main
            main()
        except:
            st.info("Instrumentos em construção")
    
    with tab2:
        try:
            from pages.cadastros.pgfornecedores import main
            main()
        except:
            st.info("Fornecedores em construção")
    
    with tab3:
        try:
            from pages.cadastros.pgfuncionarios import main
            main()
        except:
            st.info("Funcionários em construção")

elif opcao == "💰 Diárias":
    st.title("💰 Diárias")
    try:
        from pages.diarias.pgdiarias import main
        main()
    except:
        st.info("Módulo de diárias em construção")

elif opcao == "📊 Provisionamento":
    st.title("📊 Provisionamento")
    try:
        from pages.provisionamento.pgprovisionamentocd import main
        main()
    except:
        st.info("Provisionamento em construção")

elif opcao == "🔧 Teste":
    st.title("🔧 Página de Teste")
    st.write(f"**Streamlit:** {st.__version__}")
    st.write(f"**Python:** {os.sys.version}")
    
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