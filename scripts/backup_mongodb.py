#!/usr/bin/env python3
"""
BACKUP - Faz backup de todas as coleções do MongoDB
"""
import json
from datetime import datetime
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from src.database import MongoDB

def fazer_backup():
    """Faz backup de todas as coleções para arquivos JSON"""
    
    backup_dir = Path(__file__).parent.parent / "data" / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_pasta = backup_dir / f"backup_{timestamp}"
    backup_pasta.mkdir(exist_ok=True)
    
    print(f"📂 Criando backup em: {backup_pasta}")
    
    # Lista todas as coleções
    colecoes = MongoDB.get_client().list_collection_names()
    
    for colecao in colecoes:
        print(f"📄 Backup da coleção: {colecao}")
        
        dados = list(MongoDB.get_collection(colecao).find({}))
        
        # Converte ObjectId para string
        for doc in dados:
            doc['_id'] = str(doc['_id'])
        
        # Salva como JSON
        arquivo = backup_pasta / f"{colecao}.json"
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        
        print(f"   ✅ {len(dados)} registros salvos")
    
    print(f"\n✅ Backup concluído em: {backup_pasta}")

if __name__ == "__main__":
    fazer_backup()
