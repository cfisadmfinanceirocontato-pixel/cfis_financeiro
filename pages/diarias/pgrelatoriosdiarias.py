"""
Relatórios de Diárias - Página do sistema
"""
import streamlit as st

st.set_page_config(page_title="Relatórios de Diárias", layout="wide")

st.title(f"📄 Relatórios de Diárias")

st.info("Esta página está em construção. Em breve estará disponível!")

try:
    from src.database import MongoDB
    colecoes = MongoDB.get_client().list_collection_names()
    st.sidebar.success("✅ MongoDB conectado")
except:
    st.sidebar.warning("⚠️ MongoDB não disponível")
