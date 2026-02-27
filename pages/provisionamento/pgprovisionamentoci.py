"""
Provisionamento CI - Página do sistema
"""
import streamlit as st

st.set_page_config(page_title="Provisionamento CI", layout="wide")

st.title(f"📄 Provisionamento CI")

st.info("Esta página está em construção. Em breve estará disponível!")

try:
    from src.database import MongoDB
    colecoes = MongoDB.get_client().list_collection_names()
    st.sidebar.success("✅ MongoDB conectado")
except:
    st.sidebar.warning("⚠️ MongoDB não disponível")
