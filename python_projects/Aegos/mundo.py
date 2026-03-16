import networkx as nx

class Lugar():
    def __init__(self):
        self.nome_exibicao = "Reino Inicial"

# 1. Criar o Grafo
mapa = nx.Graph()

# 2. Seus lugares (objetos)
lugares = {
    "A": Lugar(),
    "B": Lugar(),
    "C": Lugar(),
    "D": Lugar(),
    "E": Lugar(),
    "F": Lugar(),
    "G": Lugar(),
    "H": Lugar(),
    "I": Lugar(),
    "J": Lugar(),
    "K": Lugar(),
    "L": Lugar(),
    "M": Lugar(),
    "N": Lugar(),
    "O": Lugar(),
    "P": Lugar(),
    "Q": Lugar(),
    "R": Lugar(),
    "S": Lugar(),
    "T": Lugar(),
    "U": Lugar(),
    "V": Lugar(),
    "W": Lugar(),
    "X": Lugar(),
    "Y": Lugar(),
    "Z": Lugar(),
    "A2": Lugar(),
    "B2": Lugar(),
    "C2": Lugar(),
    "D2": Lugar(),
}

# 3. Adicionar os lugares ao grafo
for nome, obj in lugares.items():
    mapa.add_node(nome, dados=obj)

# 4. Criar as "vizinhanças" (Arestas)
# Aqui você define quem é vizinho de quem
conexoes = [
    ("A", "B"), # A é vizinho de B
    ("A", "D2"),
    ("B", "C"),
    ("B", "D"),
    ("B", "D2"),
    ("B", "C2"),
    ("C", "D"),
    ("C", "E"),
    ("D", "E"),
    ("D", "C2"),
    ("D", "I"),
    ("D", "J"),
    ("E", "F"),
    ("E", "N1"),
    ("E", "I"),
    ("F", "N1"),
    ("F", "G"),
    ("F", "I"),
    ("F", "H"),
    ("G", "H"),
    ("G", "I"),
    ("H", "I"),
    ("H", "L"),
    ("H", "K"),
    ("I", "J"),
    ("I", "K"),
    ("J", "K"),
    ("J", "M"),
    ("J", "Q"),
    ("K", "L"),
    ("K", "M"),
    ("M", "N"),
    ("M", "O"),
    ("M", "P"),
    ("M", "Q"),
    ("M", "S"),
    ("N", "O"),
    ("O", "P"),
    ("P", "S"),
    ("P", "T"),
    ("Q", "R"),
    ("Q", "S"),
    ("R", "S"),
    ("R", "V"),
    ("R", "T"),
    ("S", "T"),
    ("T", "V"),
    ("T", "W"),
    ("U", "X"),
    ("U", "Y"),
    ("U", "V"),
    ("V", "W"),
    ("V", "Y"),
    ("W", "Y"),
    ("X", "C2"),
    ("X", "N2"),
    ("X", "A2"),
    ("X", "Y"),
    ("Y", "Z"),
    ("A2", "B2"),
    ("A2", "N2"),
    ("B2", "N2"),
    ("C2", "N2"),
    ("C2", "D2"),
    ("D2", "N2")
]

mapa.add_edges_from(conexoes)

# 5. Como usar isso no jogo?
"""
lugar_atual = "B"
vizinhos = list(mapa.neighbors(lugar_atual))
print(f"Você está em {lugar_atual}. Lugares acessíveis: {vizinhos}")

print("\n" + "="*40)
print("       🗺️  INSPEÇÃO DO MAPA DE AEGOS")
print("="*40)

for lugar in sorted(mapa.nodes()):
    vizinhos = list(mapa.neighbors(lugar))
    # Se você já tiver o atributo nome_real no objeto, pode usar:
    # nome = mapa.nodes[lugar]['dados'].nome
    print(f"📍 Local: {lugar: <3} | Conecta com: {', '.join(vizinhos)}")

print("="*40)
print(f"Total de Lugares: {mapa.number_of_nodes()}")
print(f"Total de Conexões: {mapa.number_of_edges()}")
"""
