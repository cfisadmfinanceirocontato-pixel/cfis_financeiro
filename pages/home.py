"""
HOME - Página inicial do sistema
"""
import streamlit as st
import pandas as pd
from src.database import MongoDB
from src.utils import formatar_moeda_br

st.set_page_config(page_title="Home", layout="wide")

st.title("🏠 Dashboard Principal")

# Verifica conexão com MongoDB
try:
    MongoDB.get_client().admin.command('ping')
    st.sidebar.success("✅ MongoDB conectado")
except Exception as e:
    st.sidebar.error(f"❌ MongoDB não conectado: {e}")
    st.warning("Configure as credenciais do MongoDB no arquivo .streamlit/secrets.toml")
    st.stop()

# Estatísticas
col1, col2, col3, col4 = st.columns(4)

try:
    with col1:
        total_colab = MongoDB.get_collection('colaboradores').count_documents({})
        st.metric("👥 Colaboradores", total_colab)
    
    with col2:
        total_inst = MongoDB.get_collection('instrumentos').count_documents({})
        st.metric("📋 Instrumentos", total_inst)
    
    with col3:
        total_diarias = MongoDB.get_collection('diarias').count_documents({})
        st.metric("💰 Diárias", total_diarias)
    
    with col4:
        total_prov = MongoDB.get_collection('provisionamento').count_documents({})
        st.metric("📊 Provisionamento", total_prov)
    
    # Últimos recibos
    st.subheader("📋 Últimos Recibos de Diárias")
    ultimos_recibos = list(MongoDB.get_collection('diarias')
                          .find({}, {'_id': 0, 'funcionario': 1, 'valor': 1, 'data_recibo': 1})
                          .sort('timestamp', -1)
                          .limit(10))
    
    if ultimos_recibos:
        df = pd.DataFrame(ultimos_recibos)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Nenhum recibo encontrado")
        
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
