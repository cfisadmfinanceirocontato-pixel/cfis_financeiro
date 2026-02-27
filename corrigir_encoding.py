# corrigir_encoding.py
"""
CORRIGE TODOS OS ARQUIVOS .py com encoding correto (UTF-8)
Execute este script para arrumar todos os caracteres estranhos de uma vez
"""
import os
from pathlib import Path

def corrigir_arquivo(caminho):
    """Corrige encoding de um arquivo"""
    try:
        # Tenta ler com encoding errado (latin1) e reescrever como UTF-8
        with open(caminho, 'rb') as f:
            conteudo_bytes = f.read()
        
        # Tenta decodificar com latin1 e codificar como UTF-8
        try:
            # Se o arquivo já estiver em UTF-8, isso vai funcionar
            conteudo = conteudo_bytes.decode('utf-8')
        except:
            # Se não, tenta latin1 (que aceita qualquer coisa)
            conteudo = conteudo_bytes.decode('latin1')
        
        # Reescreve como UTF-8 puro
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        return True
    except Exception as e:
        print(f"❌ Erro em {caminho}: {e}")
        return False

def main():
    print("=" * 60)
    print("🔧 CORRIGINDO ENCODING DE TODOS OS ARQUIVOS .py")
    print("=" * 60)
    
    raiz = Path.cwd()
    
    # Procura todos os arquivos .py
    arquivos_py = list(raiz.rglob("*.py"))
    
    print(f"📁 Encontrados {len(arquivos_py)} arquivos .py")
    print("-" * 60)
    
    corrigidos = 0
    for arquivo in arquivos_py:
        if "venv" not in str(arquivo) and "__pycache__" not in str(arquivo):
            print(f"📄 Corrigindo: {arquivo.relative_to(raiz)}")
            if corrigir_arquivo(arquivo):
                corrigidos += 1
    
    print("-" * 60)
    print(f"✅ {corrigidos} arquivos corrigidos com sucesso!")
    print("=" * 60)

if __name__ == "__main__":
    main()