"""File that contains the application code."""

from fastapi import FastAPI
from .schema import ProdutosSchema
from .data import Produtos
from typing import Dict, List

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/")
async def ola_mundo():
    """Função que retorna uma mensagem de olá mundo."""
    return {"Ola": "Mundo"}

@app.get("/produtos", response_model=list[ProdutosSchema])
async def listar_produtos():
    """Função que retorna a lista de produtos."""
    return lista_de_produtos.listar_produtos()

@app.get("/produto/{id}", response_model=ProdutosSchema)
async def buscar_produto(id: int):
    """Função que retorna um produto."""
    return lista_de_produtos.buscar_produto(id)

@app.post("/produto", response_model=ProdutosSchema)
async def adicionar_produto(produto: ProdutosSchema):
    """Função que cria um produto."""
    return lista_de_produtos.adicionar_produto(produto)