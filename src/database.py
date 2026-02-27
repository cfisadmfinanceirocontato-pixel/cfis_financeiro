"""

DATABASE - Módulo central de banco de dados MongoDB

"""

import streamlit as st

from pymongo import MongoClient

import pandas as pd

from datetime import datetime

import os

from dotenv import load_dotenv



load_dotenv()



# src/database.py (VERSÃO CORRIGIDA)
"""
DATABASE - Módulo central de banco de dados MongoDB
"""
import streamlit as st
from pymongo import MongoClient
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class MongoDB:
    """Classe central para todas operações MongoDB"""
    
    @staticmethod
    @st.cache_resource
    def get_client():
        """Retorna cliente MongoDB cacheado"""
        if 'mongodb' in st.secrets:
            uri = st.secrets['mongodb']['uri']
            db_name = st.secrets['mongodb']['database']
        else:
            uri = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
            db_name = os.getenv('MONGODB_DB', 'cfis_financeiro')
        
        client = MongoClient(uri)
        return client[db_name]
    
    @staticmethod
    def testar_conexao():
        """Testa se a conexão está funcionando"""
        try:
            # Obtém o cliente
            db = MongoDB.get_client()
            # Tenta listar coleções (operação simples para testar)
            colecoes = db.list_collection_names()
            return True, f"Conectado! {len(colecoes)} coleções encontradas."
        except Exception as e:
            return False, str(e)
    
    @staticmethod
    def get_collection(nome):
        """Obtém uma coleção específica"""
        return MongoDB.get_client()[nome]
    
    @staticmethod
    def df_to_collection(df, colecao, limpar=False):
        """Salva DataFrame no MongoDB"""
        if limpar:
            MongoDB.get_collection(colecao).delete_many({})
        if not df.empty:
            registros = df.to_dict('records')
            # Converte NaN para None
            for reg in registros:
                for k, v in reg.items():
                    if pd.isna(v):
                        reg[k] = None
            MongoDB.get_collection(colecao).insert_many(registros)
        return len(df)
    
    @staticmethod
    def collection_to_df(colecao, filtro=None):
        """Carrega coleção MongoDB para DataFrame"""
        filtro = filtro or {}
        cursor = MongoDB.get_collection(colecao).find(filtro)
        df = pd.DataFrame(list(cursor))
        if '_id' in df.columns:
            df['_id'] = df['_id'].astype(str)
        return df


# ============================================================================

# OPERAÇÕES ESPECÍFICAS DO SISTEMA

# ============================================================================



class DiariasDB:

    """Operações do módulo de diárias"""

    

    @staticmethod

    def salvar_recibo(dados_recibo, arquivo_docx=None):

        """Salva um recibo de diária"""

        colecao = MongoDB.get_collection('diarias')

        

        documento = {

            'termo_colaboracao': dados_recibo.get('Termo de Colaboração'),

            'instrumento': dados_recibo.get('Instrumento'),

            'funcionario': dados_recibo.get('Funcionário'),

            'cpf': dados_recibo.get('CPF'),

            'cargo': dados_recibo.get('Cargo'),

            'quantidade': float(dados_recibo.get('Quantidade', '0').replace(',', '.')),

            'valor': dados_recibo.get('Valor'),

            'periodo': dados_recibo.get('Período'),

            'oficio': dados_recibo.get('Ofício'),

            'data_recibo': dados_recibo.get('Data Recibo'),

            'timestamp': datetime.now(),

            'status': 'ativo'

        }

        

        if arquivo_docx:

            documento['arquivo_docx'] = arquivo_docx

        

        return colecao.insert_one(documento)

    

    @staticmethod

    def listar_recibos(limite=100):

        """Lista últimos recibos"""

        colecao = MongoDB.get_collection('diarias')

        return list(colecao.find().sort('timestamp', -1).limit(limite))



class InstrumentosDB:

    """Operações dos instrumentos/termos"""

    

    @staticmethod

    def carregar_todos():

        """Carrega todos os instrumentos"""

        colecao = MongoDB.get_collection('instrumentos')

        return pd.DataFrame(list(colecao.find()))



class ProvisionamentoDB:

    """Operações do módulo de provisionamento"""

    

    @staticmethod

    def salvar_registro(dados):

        """Salva um registro de provisionamento"""

        colecao = MongoDB.get_collection('provisionamento')

        dados['timestamp'] = datetime.now()

        return colecao.insert_one(dados)

