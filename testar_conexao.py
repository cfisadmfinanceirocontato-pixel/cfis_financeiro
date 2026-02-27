# testar_conexao.py
from src.database import MongoDB
import streamlit as st

print("🔍 TESTANDO CONEXÃO COM MONGODB...")
print("-" * 50)

try:
    # Tenta conectar
    cliente = MongoDB.get_client()
    
    # Tenta listar as coleções
    colecoes = cliente.list_collection_names()
    
    print("✅ CONEXÃO BEM-SUCEDIDA!")
    print(f"📊 Banco de dados: {cliente.name}")
    print(f"📋 Coleções encontradas: {len(colecoes)}")
    
    if colecoes:
        print("   " + ", ".join(colecoes[:5]))
    else:
        print("   Nenhuma coleção ainda (banco vazio)")
        
except Exception as e:
    print("❌ ERRO DE CONEXÃO!")
    print(f"🔴 {e}")
    print("-" * 50)
    print("\n🔧 POSSÍVEIS CAUSAS:")
    print("1. Senha incorreta no secrets.toml")
    print("2. IP não liberado (Network Access)")
    print("3. Usuário não tem permissão")
    print("4. String de conexão incorreta")