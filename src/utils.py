"""
UTILS - Funções utilitárias
"""
import re
from datetime import datetime
import pandas as pd

def formatar_moeda_br(valor):
    """Formata valor para Real Brasileiro (R$ 1.234,56)"""
    try:
        if pd.isna(valor) or valor == "":
            return "R$ 0,00"
        if isinstance(valor, (int, float)):
            return f"R$ {abs(valor):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        valor_str = str(valor).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
        valor_float = float(valor_str)
        return f"R$ {abs(valor_float):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except:
        return "R$ 0,00"

def converter_moeda_para_float(valor_str):
    """Converte string de moeda BR para float"""
    if isinstance(valor_str, (int, float)):
        return float(valor_str)
    try:
        if pd.isna(valor_str) or valor_str == "":
            return 0.0
        valor_limpo = str(valor_str).replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
        return float(valor_limpo)
    except:
        return 0.0

def limpar_cpf(cpf):
    """Remove caracteres especiais do CPF (deixa só números)"""
    if pd.isna(cpf):
        return ""
    return re.sub(r'[^0-9]', '', str(cpf))

def extrair_numero_oficio(oficio_completo):
    """Extrai apenas o número do ofício (antes da barra)"""
    if pd.isna(oficio_completo) or not isinstance(oficio_completo, str):
        return str(oficio_completo).strip()
    if '/' in oficio_completo:
        return oficio_completo.split('/')[0].strip()
    return oficio_completo.strip()

def formatar_data_completa(data_obj):
    """Formata data por extenso (01 de janeiro de 2024)"""
    meses = {1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',6:'junho',
             7:'julho',8:'agosto',9:'setembro',10:'outubro',11:'novembro',12:'dezembro'}
    try:
        if isinstance(data_obj, datetime):
            data = data_obj
        else:
            data = pd.to_datetime(data_obj, dayfirst=True)
        return f"{data.day:02d} de {meses[data.month]} de {data.year}"
    except:
        return datetime.now().strftime("%d de %B de %Y").lower()
