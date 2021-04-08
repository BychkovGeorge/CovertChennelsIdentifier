# -*- coding: utf-8 -*-

from scapy.layers.inet import TCP
from scapy.layers.inet import IP
from scapy.sendrecv import sr
import networkx as nx
import matplotlib.pyplot as plt

print("Введите IPv4 адреса хостов сети через запятую, первым укажите текущий хост")
network_addresses = input()
list_of_network_addresses = network_addresses.split(", ")

graph_ihl = nx.Graph()
graph_tos = nx.Graph()
graph_len = nx.Graph()
graph_id = nx.Graph()
graph_frag = nx.Graph()
graph_ttl = nx.Graph()
graph_proto = nx.Graph()

for z in range(len(list_of_network_addresses)):
    graph_ihl.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_tos.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_len.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_id.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_frag.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_ttl.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_proto.add_node(list_of_network_addresses[z])

for x in range(len(list_of_network_addresses)):
    for y in range(len(list_of_network_addresses)):
        if x < y:
            print(f"Существует ли связь между хостом {list_of_network_addresses[x]}  и хостом {list_of_network_addresses[y]} \n")
            print("Введите 1 если да и 0, если нет")
            val = input()
            if val == "1":
                graph_ihl.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_tos.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_len.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_id.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_frag.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_ttl.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_proto.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)

for j in range(len(list_of_network_addresses)):
    if j != 0:
        packet_ihl = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_tos = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_len = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_id = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_frag = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_ttl = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_proto = IP(dst=list_of_network_addresses[j]) / TCP(dport=22)

        packet_ihl.ihl = 18
        packet_tos.tos = 18
        packet_len.len = 18
        packet_id.id = 18
        packet_frag.frag = 18
        packet_ttl.ttl = 18
        packet_proto.proto = 18

        answer_ihl = sr(packet_ihl, timeout=4)
        answer_tos = sr(packet_tos, timeout=4)
        answer_len = sr(packet_len, timeout=4)
        answer_id = sr(packet_id, timeout=4)
        answer_frag = sr(packet_frag, timeout=4)
        answer_ttl = sr(packet_ttl, timeout=4)
        answer_proto = sr(packet_proto, timeout=4)

        if len(answer_ihl[0]) != 0:
            if len(nx.dijkstra_path(graph_ihl, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_ihl.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_ihl_path = nx.dijkstra_path(graph_ihl, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_ihl_path) - 1):
                    if index != len(arr_of_ihl_path) - 1:
                        graph_ihl.add_edge(str(arr_of_ihl_path[index]), str(arr_of_ihl_path[index + 1]), color='r', weight=6)
        if len(answer_tos[0]) != 0:
            if len(nx.dijkstra_path(graph_tos, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_tos.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_tos_path = nx.dijkstra_path(graph_tos, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_tos_path) - 1):
                    if index != len(arr_of_tos_path) - 1:
                        graph_tos.add_edge(str(arr_of_tos_path[index]), str(arr_of_tos_path[index + 1]), color='r', weight=6)
        if len(answer_len[0]) != 0:
            if len(nx.dijkstra_path(graph_len, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_len.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_len_path = nx.dijkstra_path(graph_len, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_len_path) - 1):
                    if index != len(arr_of_len_path) - 1:
                        graph_len.add_edge(str(arr_of_len_path[index]), str(arr_of_len_path[index + 1]), color='r', weight=6)
        if len(answer_id[0]) != 0:
            if len(nx.dijkstra_path(graph_id, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_id.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_id_path = nx.dijkstra_path(graph_id, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_id_path) - 1):
                    if index != len(arr_of_id_path) - 1:
                        graph_id.add_edge(str(arr_of_id_path[index]), str(arr_of_id_path[index + 1]), color='r', weight=6)
        if len(answer_frag[0]) != 0:
            if len(nx.dijkstra_path(graph_frag, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_frag.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_frag_path = nx.dijkstra_path(graph_frag, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_frag_path) - 1):
                    if index != len(arr_of_frag_path) - 1:
                        graph_frag.add_edge(str(arr_of_frag_path[index]), str(arr_of_frag_path[index + 1]), color='r', weight=6)
        if len(answer_ttl[0]) != 0:
            if len(nx.dijkstra_path(graph_ttl, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_ttl.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_ttl_path = nx.dijkstra_path(graph_ttl, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_ttl_path) - 1):
                    if index != len(arr_of_ttl_path) - 1:
                        graph_ttl.add_edge(str(arr_of_ttl_path[index]), str(arr_of_ttl_path[index + 1]), color='r', weight=6)
        if len(answer_proto[0]) != 0:
            if len(nx.dijkstra_path(graph_proto, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_proto.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                arr_of_proto_path = nx.dijkstra_path(graph_proto, list_of_network_addresses[0], list_of_network_addresses[j])
                for index in range(len(arr_of_proto_path) - 1):
                    if index != len(arr_of_proto_path) - 1:
                        graph_proto.add_edge(str(arr_of_proto_path[index]), str(arr_of_proto_path[index + 1]), color='r', weight=6)

edges_ihl = graph_ihl.edges()
colors_ihl = [graph_ihl[u][v]['color'] for u, v in edges_ihl]
weights_ihl = [graph_ihl[u][v]['weight'] for u, v in edges_ihl]

edges_tos = graph_tos.edges()
colors_tos = [graph_tos[u][v]['color'] for u, v in edges_tos]
weights_tos = [graph_tos[u][v]['weight'] for u, v in edges_tos]

edges_len = graph_len.edges()
colors_len = [graph_len[u][v]['color'] for u, v in edges_len]
weights_len = [graph_len[u][v]['weight'] for u, v in edges_len]

edges_id = graph_id.edges()
colors_id = [graph_id[u][v]['color'] for u, v in edges_id]
weights_id = [graph_id[u][v]['weight'] for u, v in edges_id]

edges_frag = graph_frag.edges()
colors_frag = [graph_frag[u][v]['color'] for u, v in edges_frag]
weights_frag = [graph_frag[u][v]['weight'] for u, v in edges_frag]

edges_ttl = graph_ttl.edges()
colors_ttl = [graph_ttl[u][v]['color'] for u, v in edges_ttl]
weights_ttl = [graph_ttl[u][v]['weight'] for u, v in edges_ttl]

edges_proto = graph_proto.edges()
colors_proto = [graph_proto[u][v]['color'] for u, v in edges_proto]
weights_proto = [graph_proto[u][v]['weight'] for u, v in edges_proto]

nx.draw_circular(graph_ihl, node_color='blue', node_size=10000, font_color='w', edge_color=colors_ihl, width=weights_ihl, with_labels=True, label='graph_ihl')
plt.show()
nx.draw_circular(graph_tos, node_color='blue', node_size=10000, font_color='w', edge_color=colors_tos, width=weights_tos, with_labels=True, label='graph_tos')
plt.show()
nx.draw_circular(graph_len, node_color='blue', node_size=10000, font_color='w', edge_color=colors_len, width=weights_len, with_labels=True, label='graph_len')
plt.show()
nx.draw_circular(graph_id, node_color='blue', node_size=10000, font_color='w', edge_color=colors_id, width=weights_id, with_labels=True, label='graph_id')
plt.show()
nx.draw_circular(graph_frag, node_color='blue', node_size=10000, font_color='w', edge_color=colors_frag, width=weights_frag, with_labels=True, label='graph_frag')
plt.show()
nx.draw_circular(graph_ttl, node_color='blue', node_size=10000, font_color='w', edge_color=colors_ttl, width=weights_ttl, with_labels=True, label='graph_ttl')
plt.show()
nx.draw_circular(graph_proto, node_color='blue', node_size=10000, font_color='w', edge_color=colors_proto, width=weights_proto, with_labels=True, label='graph_proto')
plt.show()

