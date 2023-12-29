"""File that contains the routes of the application."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .schema import ProdutosSchema
from .config import get_db, SessionLocal
from .model import Produto

router = APIRouter()

@router.get("/")
async def ola_mundo():
    """Função que retorna ola mundo."""
    return {"mensagem": "Olá mundo!"}

@router.get("/produtos", response_model=list[ProdutosSchema])
async def listar_produtos(db: SessionLocal = Depends(get_db)):
    """Função que retorna a lista de produtos do sqlalchemy postgres."""
    return db.query(Produto).all() # SELECT * FROM produtos

@router.get("/produto/{produto_id}", response_model=ProdutosSchema)
async def buscar_produto(produto_id: int, db: SessionLocal = Depends(get_db)):
    """Função que retorna um produto do sqlalchemy postgres."""
    produto = db.query(Produto).filter(Produto.id == produto_id).first() # SELECT * FROM produtos WHERE id = produto_id
    
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        return produto

@router.post("/produto", response_model=ProdutosSchema)
async def criar_produto(produto_data: ProdutosSchema, db: SessionLocal = Depends(get_db)):
    """Função que cria um produto no banco de dados."""
    db_produto = Produto(**produto_data.model_dump())
    db.add(db_produto) # INSERT INTO produtos (titulo, descricao, preco) VALUES (db_produto.titulo, db_produto.descricao, db_produto.preco)
    db.commit() # COMMIT
    db.refresh(db_produto)
    return db_produto

@router.delete("/produto/{produto_id}", response_model=ProdutosSchema)
async def remover_produto(produto_id: int, db: SessionLocal = Depends(get_db)):
    """Função que remove um produto do banco de dados."""
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        db.delete(produto) # DELETE FROM produtos WHERE id = produto_id
        db.commit() # COMMIT
        return produto

@router.put("/produto/{produto_id}", response_model=ProdutosSchema)
async def atualizar_produto(produto_id: int, produto_data: ProdutosSchema, db: SessionLocal = Depends(get_db)):
    """Função que atualiza um produto do banco de dados."""
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    else:
        for key, value in produto_data.model_dump().items():
            setattr(db_produto, key, value) if value else None
        db.commit() # COMMIT
        db.refresh(db_produto) # SELECT * FROM produtos WHERE id = db_produto.id
        return db_produto