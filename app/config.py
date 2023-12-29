"""File that contains the configuration of the application."""

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Validar a questao do dotenv porque nao funciona no windows
db_user     = 'meu_usuario'
db_password = 'minha_senha'
db_name     = 'meu_banco'
db_host     = '192.168.0.110'
db_instance = 'SQL2022'
db_port     = '54341'

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

# DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}" # Postgres
DATABASE_URL = f'mssql+pyodbc://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server&instance={db_instance}' # SQL Server

# Criando a engine de conexão
engine = create_engine(DATABASE_URL, echo=True)

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