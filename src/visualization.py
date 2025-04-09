# src/visualization.py
import os
import matplotlib.pyplot as plt
import networkx as nx

def generate_similarity_graph(similarities, filename="similitudes.png"):
    G = nx.Graph()
    top_10 = similarities[:10]
    
    edge_labels = {}
    for doc1, doc2, sim in top_10:
        G.add_edge(doc1, doc2, weight=sim)
        edge_labels[(doc1, doc2)] = f"{sim * 100:.0f}%"  # Mostrar como entero
    
    plt.figure(figsize=(14, 9))
    pos = nx.spring_layout(G, k=0.5)
    
    nodes = nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightgreen')
    edges = nx.draw_networkx_edges(
        G, pos,
        width=[d['weight'] * 10 for u, v, d in G.edges(data=True)],
        edge_color=[d['weight'] for u, v, d in G.edges(data=True)],
        edge_cmap=plt.cm.Reds
    )
    
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.colorbar(edges, label="Índice de Jaccard (0-1)")
    plt.title("Red de Similitud entre Documentos", fontsize=16)
    plt.axis('off')
    
    if not os.path.exists("resultados"):
        os.makedirs("resultados")
        
    plt.savefig(os.path.join("resultados", filename), dpi=300)
    plt.show()