"""
FILE HANDLER - Gerenciamento de arquivos local/cloud
"""
import tempfile
from pathlib import Path
import io
import zipfile
import shutil

class FileHandler:
    """Gerencia operações com arquivos"""
    
    @staticmethod
    def save_uploaded_file(uploaded_file, subdir="uploads"):
        """Salva arquivo uploadado em pasta temporária"""
        temp_dir = Path(tempfile.gettempdir()) / "cfis_financeiro" / subdir
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = temp_dir / uploaded_file.name
        with open(file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        return str(file_path)
    
    @staticmethod
    def create_temp_file(content, suffix=".txt"):
        """Cria arquivo temporário com conteúdo"""
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            if isinstance(content, str):
                tmp.write(content.encode())
            else:
                tmp.write(content)
            return tmp.name
    
    @staticmethod
    def create_zip_from_files(files_dict):
        """Cria ZIP a partir de dicionário {nome: conteudo_bytes}"""
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for nome, conteudo in files_dict.items():
                zipf.writestr(nome, conteudo)
        zip_buffer.seek(0)
        return zip_buffer.getvalue()
    
    @staticmethod
    def get_temp_dir():
        """Retorna pasta temporária do projeto"""
        temp_dir = Path(tempfile.gettempdir()) / "cfis_financeiro"
        temp_dir.mkdir(parents=True, exist_ok=True)
        return temp_dir
