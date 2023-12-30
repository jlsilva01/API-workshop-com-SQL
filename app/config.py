"""File that contains the configuration of the application."""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv
import urllib

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

from decouple import config

db_user = config('DB_USER')
db_pass = config('DB_PASS')
db_name = config('DB_NAME')
db_host = config('DB_HOST')
db_port = config('DB_PORT')

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

odbc_str = f'''Driver={{ODBC Driver 17 for SQL Server}};Server={db_host};Database={db_name};Uid={db_user};Pwd={db_pass};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'''

url_parseada = urllib.parse.quote_plus(odbc_str)
# DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}" # Postgres
# DATABASE_URL = f'mssql+pyodbc://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server' # SQL Server

connect_str = f'mssql+pyodbc:///?odbc_connect={url_parseada}'

# Criando a engine de conexão
engine = create_engine(connect_str, echo=False)

# Criando a sessão

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

# Funcao para criar a sessão
def get_db():
    """Função que retorna a sessão do banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()