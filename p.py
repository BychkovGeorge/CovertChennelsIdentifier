import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

g.add_node('A')
g.add_node('B')
g.add_edge('A', 'B', color='r', weight=6)

edges = g.edges()
colors = [g[u][v]['color'] for u, v in edges]
weights = [g[u][v]['weight'] for u, v in edges]

nx.draw_circular(g, node_color='blue', node_size=10000, edge_color=colors, width=weights, with_labels=True, label='graph_tc')
plt.show()
