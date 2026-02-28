# app_teste.py
import streamlit as st
import sys
import pymongo
import pandas as pd

st.set_page_config(page_title="TESTE CFIS", page_icon="🔧", layout="wide")

st.title("🔧 APP DE TESTE - CFIS FINANCEIRO")

st.write("### Informações do Sistema:")

col1, col2 = st.columns(2)

with col1:
    st.write("**Python version:**", sys.version)
    
    try:
        import pymongo
        st.success(f"✅ pymongo {pymongo.__version__} instalado!")
    except Exception as e:
        st.error(f"❌ pymongo erro: {e}")
    
    try:
        import pandas
        st.success(f"✅ pandas {pandas.__version__} instalado!")
    except Exception as e:
        st.error(f"❌ pandas erro: {e}")

with col2:
    try:
        from src.database import MongoDB
        sucesso, msg = MongoDB.testar_conexao()
        if sucesso:
            st.success(f"✅ MongoDB: {msg}")
            
            # Mostra algumas estatísticas
            colecoes = MongoDB.get_client().list_collection_names()
            st.info(f"📊 Coleções: {', '.join(colecoes[:5])}")
        else:
            st.error(f"❌ MongoDB: {msg}")
    except Exception as e:
        st.error(f"❌ Erro MongoDB: {e}")

st.write("---")
st.write("### ✅ App de teste funcionando corretamente!")