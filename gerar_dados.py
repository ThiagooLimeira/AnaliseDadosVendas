import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar o Faker para gerar dados fictícios em português
fake = Faker('pt_BR')

# 1. Definir os parâmetros da base de dados
num_linhas = 15000
print(f"Gerando {num_linhas} registros de vendas...")

# 2. Criar listas de produtos e categorias para garantir consistência
produtos_categorias = {
    'Eletrônicos': ['Smartphone', 'Notebook', 'Tablet', 'Fone de Ouvido', 'Smartwatch', 'Carregador Portátil'],
    'Livros': ['Ficção Científica', 'Romance', 'Biografia', 'Fantasia', 'Autoajuda'],
    'Casa e Cozinha': ['Cafeteira', 'Liquidificador', 'Panela de Pressão', 'Jogo de Pratos', 'Aspirador de Pó'],
    'Moda e Acessórios': ['Camiseta', 'Calça Jeans', 'Tênis', 'Bolsa de Couro', 'Óculos de Sol'],
    'Esportes e Lazer': ['Bicicleta Ergométrica', 'Bola de Futebol', 'Barraca de Camping', 'Corda de Pular']
}

lista_categorias = list(produtos_categorias.keys())
lista_produtos_completa = [item for sublist in produtos_categorias.values() for item in sublist]

# Mapear produto para sua categoria
produto_para_categoria = {produto: categoria for categoria, produtos in produtos_categorias.items() for produto in produtos}

# Definir uma faixa de preço base para cada produto
precos_base = {
    'Smartphone': 1200, 'Notebook': 2500, 'Tablet': 800, 'Fone de Ouvido': 150, 'Smartwatch': 500, 'Carregador Portátil': 90,
    'Ficção Científica': 40, 'Romance': 35, 'Biografia': 50, 'Fantasia': 45, 'Autoajuda': 30,
    'Cafeteira': 120, 'Liquidificador': 80, 'Panela de Pressão': 150, 'Jogo de Pratos': 100, 'Aspirador de Pó': 300,
    'Camiseta': 50, 'Calça Jeans': 120, 'Tênis': 200, 'Bolsa de Couro': 180, 'Óculos de Sol': 90,
    'Bicicleta Ergométrica': 700, 'Bola de Futebol': 60, 'Barraca de Camping': 250, 'Corda de Pular': 20
}

# 3. Gerar os dados
dados = []
data_inicial = datetime.now() - timedelta(days=730) # Dados dos últimos 2 anos

for i in range(num_linhas):
    # Escolher produto e obter sua categoria
    produto_escolhido = random.choice(lista_produtos_completa)
    categoria_escolhida = produto_para_categoria[produto_escolhido]
    
    # Gerar preço com uma pequena variação aleatória
    preco_base = precos_base[produto_escolhido]
    preco_unitario = round(random.uniform(preco_base * 0.9, preco_base * 1.1), 2)
    
    # Gerar quantidade (mais provável ser baixa)
    quantidade = np.random.choice([1, 2, 3, 4, 5], p=[0.6, 0.2, 0.1, 0.05, 0.05])
    
    valor_total = round(preco_unitario * quantidade, 2)
    
    data_pedido = data_inicial + timedelta(seconds=random.randint(0, 730*24*60*60))
    
    dados.append({
        'ID_Pedido': 1000 + i,
        'ID_Cliente': random.randint(100, 1500), # Menos clientes que pedidos para garantir recorrência
        'Data_Pedido': data_pedido.strftime('%Y-%m-%d'),
        'Produto': produto_escolhido,
        'Categoria': categoria_escolhida,
        'Preco_Unitario': preco_unitario,
        'Quantidade': quantidade,
        'Valor_Total': valor_total
    })

# 4. Criar o DataFrame com o Pandas
df = pd.DataFrame(dados)

# 5. Salvar em um arquivo CSV
nome_arquivo = 'database_vendas_online.csv'
df.to_csv(nome_arquivo, index=False, encoding='utf-8')

print(f"\nArquivo '{nome_arquivo}' gerado com sucesso!")
print(f"Total de linhas: {len(df)}")
print("5 primeiras linhas do arquivo:")
print(df.head())