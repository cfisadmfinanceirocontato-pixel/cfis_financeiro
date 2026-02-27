# criar_paginas_basicas.py
"""
Cria páginas básicas para o sistema
Execute na raiz do projeto
"""
from pathlib import Path

def criar_pagina(caminho, titulo):
    """Cria uma página básica"""
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(f'''"""
{titulo} - Página do sistema
"""
import streamlit as st

st.set_page_config(page_title="{titulo}", layout="wide")

st.title(f"📄 {titulo}")

st.info("Esta página está em construção. Em breve estará disponível!")

try:
    from src.database import MongoDB
    colecoes = MongoDB.get_client().list_collection_names()
    st.sidebar.success("✅ MongoDB conectado")
except:
    st.sidebar.warning("⚠️ MongoDB não disponível")
''')

def main():
    raiz = Path.cwd()
    print("=" * 60)
    print("🚀 CRIANDO PÁGINAS BÁSICAS")
    print("=" * 60)
    
    # Páginas de cadastros
    cadastros = [
        ("cadastrosinstrumentos.py", "Instrumentos"),
        ("pgfornecedores.py", "Fornecedores"),
        ("pgfuncionarios.py", "Funcionários")
    ]
    
    for arquivo, titulo in cadastros:
        caminho = raiz / "pages/cadastros" / arquivo
        if not caminho.exists():
            criar_pagina(caminho, titulo)
            print(f"✅ Criada: pages/cadastros/{arquivo}")
        else:
            print(f"⏩ Já existe: pages/cadastros/{arquivo}")
    
    # Páginas de diárias
    diarias = [
        ("pgdiarias.py", "Recibos de Diárias"),
        ("pgpgtodiarias.py", "Pagamentos de Diárias"),
        ("pghomediarias.py", "Home Diárias"),
        ("pgrelatoriosdiarias.py", "Relatórios de Diárias")
    ]
    
    for arquivo, titulo in diarias:
        caminho = raiz / "pages/diarias" / arquivo
        if not caminho.exists():
            criar_pagina(caminho, titulo)
            print(f"✅ Criada: pages/diarias/{arquivo}")
        else:
            print(f"⏩ Já existe: pages/diarias/{arquivo}")
    
    # Páginas de provisionamento
    provisionamento = [
        ("pgprovisionamento.py", "Provisionamento Geral"),
        ("pgprovisionamentocd.py", "Provisionamento CD"),
        ("pgprovisionamentoci.py", "Provisionamento CI"),
        ("pgprovisionamentopessoal.py", "Provisionamento Pessoal")
    ]
    
    for arquivo, titulo in provisionamento:
        caminho = raiz / "pages/provisionamento" / arquivo
        if not caminho.exists():
            criar_pagina(caminho, titulo)
            print(f"✅ Criada: pages/provisionamento/{arquivo}")
        else:
            print(f"⏩ Já existe: pages/provisionamento/{arquivo}")
    
    # Páginas de pagamentos
    pagamentos = [
        ("pgconsumo.py", "Pagamentos Consumo"),
        ("pgservicos.py", "Pagamentos Serviços"),
        ("pgveiculos.py", "Pagamentos Veículos"),
        ("pgeventoscd.py", "Pagamentos Eventos"),
        ("pgmanutencoes.py", "Pagamentos Manutenções"),
        ("pgservieventuais.py", "Pagamentos Serviços Eventuais")
    ]
    
    for arquivo, titulo in pagamentos:
        caminho = raiz / "pages/pagamentos" / arquivo
        if not caminho.exists():
            criar_pagina(caminho, titulo)
            print(f"✅ Criada: pages/pagamentos/{arquivo}")
        else:
            print(f"⏩ Já existe: pages/pagamentos/{arquivo}")
    
    # Página de repasses
    repasses = raiz / "pages" / "pgrepasses.py"
    if not repasses.exists():
        criar_pagina(repasses, "Cronograma de Repasses")
        print("✅ Criada: pages/pgrepasses.py")
    else:
        print("⏩ Já existe: pages/pgrepasses.py")
    
    print("\n" + "=" * 60)
    print("🎉 PROCESSO CONCLUÍDO!")
    print("=" * 60)

if __name__ == "__main__":
    main()