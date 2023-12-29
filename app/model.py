"""File that contains the model of the application."""

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Definindo o modelo de dados
class Produto(Base):
    """Classe que representa a tabela de produtos do banco de dados."""
    
    __tablename__ = "produtos"
    __table_args__ = {"schema":"dbo"} # Esquema do banco de dados SOMENTE PARA SQL SERVER
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String)
    preco = Column(Float, nullable=False)

