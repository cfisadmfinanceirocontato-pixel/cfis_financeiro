#!/usr/bin/env python3
"""
MIGRAÇÃO ÚNICA - Execute apenas 1 vez para migrar CSVs para MongoDB
"""
import pandas as pd
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.database import MongoDB

def migrar():
    """Migra todos os arquivos CSV para MongoDB"""
    
    print("=" * 60)
    print("🚀 INICIANDO MIGRAÇÃO CSV → MONGODB")
    print("=" * 60)
    
    # Mapeamento de arquivos para coleções
    arquivos = [
        ('dados_colaboradores.csv', 'colaboradores'),
        ('itens_despesas.csv', 'itens_despesas'),
        ('itens_instrumento.csv', 'itens_instrumento'),
        ('lista_instrumentos.csv', 'instrumentos'),
        ('provisionamentocd.csv', 'provisionamento')
    ]
    
    for arquivo, colecao in arquivos:
        print(f"\n📄 Processando {arquivo} -> {colecao}...")
        
        # Procura o arquivo em diferentes locais
        caminhos = [
            Path(__file__).parent.parent / arquivo,
            Path(__file__).parent.parent / "data" / arquivo,
            Path.cwd() / arquivo
        ]
        
        caminho = None
        for c in caminhos:
            if c.exists():
                caminho = c
                break
        
        if not caminho:
            print(f"❌ Arquivo não encontrado: {arquivo}")
            continue
        
        # Tenta diferentes encodings
        df = None
        for encoding in ['utf-8-sig', 'latin1', 'cp1252']:
            try:
                df = pd.read_csv(caminho, encoding=encoding)
                print(f"   ✅ Lido com {encoding}: {len(df)} linhas")
                break
            except:
                continue
        
        if df is None:
            print(f"❌ Não foi possível ler {arquivo}")
            continue
        
        # Limpa coleção e insere
        MongoDB.get_collection(colecao).delete_many({})
        
        # Converte NaN para None
        registros = df.where(pd.notna(df), None).to_dict('records')
        
        if registros:
            MongoDB.get_collection(colecao).insert_many(registros)
            print(f"   ✅ {len(registros)} registros inseridos")
    
    print("\n" + "=" * 60)
    print("✅ MIGRAÇÃO CONCLUÍDA!")
    print("=" * 60)

if __name__ == "__main__":
    migrar()
