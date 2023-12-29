"""File that contains the data of the application."""

from typing import Dict, List

class Produtos:
    """Class that contains the data of the application."""
    
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Um smartphone top de linha.",
            "preco": 1500.00
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Um notebook gamer.",
            "preco": 3500.00
        },
        {
            "id": 3,
            "nome": "Tablet",
            "descricao": "Um tablet intermediario.",
            "preco": 1200.00
        }
    ]

    def listar_produtos(self):
        """Função que retorna a lista de produtos."""
        return self.produtos

    def buscar_produto(self, id: int):
        """Função que retorna um produto."""
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Erro": "Produto não encontrado."}
    
    def adicionar_produto(self, produto):
        """Função que adiciona um produto."""
        self.produtos.append(produto)
        return produto