"""File that contains the schema of the application."""

from pydantic import BaseModel, PositiveFloat
from typing import Optional

class ProdutosSchema(BaseModel):
    """Classe que representa o schema de um produto."""
    
    id: Optional[int] = None
    titulo: str
    descricao: Optional[str] = None
    preco: PositiveFloat