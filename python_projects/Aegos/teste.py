import networkx as nx
import matplotlib.pyplot as plt

# 1. Criar o objeto do Grafo
G = nx.DiGraph()  # DiGraph para relações direcionadas (ex: "Pai de")

# 2. Adicionar as relações (Arestas)
# Formato: (Origem, Destino, Tipo de Relação)
relacoes = [
    ("João", "Maria", "Pai de"),
    ("João", "Pedro", "Pai de"),
    ("Ana", "Maria", "Mãe de"),
    ("Ana", "Pedro", "Mãe de"),
    ("Maria", "Lucas", "Mãe de")
]

for origem, destino, tipo in relacoes:
    G.add_edge(origem, destino, relation=tipo)

# 3. Configurar o layout (posicionamento dos nomes)
pos = nx.spring_layout(G)

# 4. Desenhar o grafo
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', 
        node_size=2000, font_size=12, font_weight='bold', 
        arrowsize=20)

# Adicionar rótulos nas setas (opcional)
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Grafo de Relações Familiares")
plt.show()