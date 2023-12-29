"""File that contains the tests of the application."""

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ola_mundo_status_code():
    response = client.get("/")
    assert response.status_code == 200
    
def test_ola_mundo_conteudo():
    response = client.get("/")
    assert response.json() == {"Ola": "Mundo"}
    
def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200
    
def test_tamanho_lista_de_produtos():
    response = client.get("/produtos")
    assert len(response.json()) == 3
    
def test_pega_produto_um_produto():
    response = client.get("/produto/1")
    assert response.json() == {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone top de linha.",
        "preco": 1500.00,
    }