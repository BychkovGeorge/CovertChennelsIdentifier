# -*- coding: utf-8 -*-

from scapy.layers.inet import TCP
from scapy.layers.inet6 import IPv6
from scapy.sendrecv import sr
import networkx as nx
import matplotlib.pyplot as plt

print("Введите IPv6 адреса хостов сети через запятую, первым укажите текущий хост")
network_addresses = input()
list_of_network_addresses = network_addresses.split(", ")

graph_tc = nx.Graph()
graph_fl = nx.Graph()
graph_plen = nx.Graph()
graph_nh = nx.Graph()
graph_hlim = nx.Graph()
graph_src = nx.Graph()

for z in range(len(list_of_network_addresses)):
    graph_tc.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_fl.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_plen.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_nh.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_hlim.add_node(list_of_network_addresses[z])
for z in range(len(list_of_network_addresses)):
    graph_src.add_node(list_of_network_addresses[z])

for x in range(len(list_of_network_addresses)):
    for y in range(len(list_of_network_addresses)):
        if x < y:
            print(f"Существует ли связь между хостом {list_of_network_addresses[x]}  и хостом {list_of_network_addresses[y]} \n")
            print("Введите 1 если да и 0, если нет")
            val = input()
            if val == "1":
                graph_tc.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_fl.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_plen.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_nh.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_hlim.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)
                graph_src.add_edge(list_of_network_addresses[x], list_of_network_addresses[y], color='b', weight=1)


for j in range(len(list_of_network_addresses)):
    if j != 0:
        packet_tc = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_fl = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_plen = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_nh = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_hlim = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
        packet_src = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)

        packet_tc.tc = 18
        packet_fl.fl = 18
        packet_plen.plen = 18
        packet_nh.nh = 18
        packet_hlim.hlim = 18
        packet_src.src = 18

        answer_tc = sr(packet_tc, timeout=4)
        answer_fl = sr(packet_fl, timeout=4)
        answer_plen = sr(packet_plen, timeout=4)
        answer_nh = sr(packet_nh, timeout=4)
        answer_hlim = sr(packet_hlim, timeout=4)
        answer_src = sr(packet_src, timeout=4)

        if len(answer_tc[0]) != 0 and not hasattr(answer_tc[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_tc, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_tc.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_tc, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_tc, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_tc.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)
        if len(answer_fl[0]) != 0 and not hasattr(answer_fl[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_fl, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_fl.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_fl, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_fl, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_fl.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)
        if len(answer_plen[0]) != 0 and not hasattr(answer_plen[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_plen, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_plen.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_plen, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_plen, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_plen.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)
        if len(answer_nh[0]) != 0 and not hasattr(answer_nh[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_nh, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_nh.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_nh, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_nh, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_nh.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)
        if len(answer_hlim[0]) != 0 and not hasattr(answer_hlim[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_hlim, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_hlim.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_hlim, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_hlim, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_hlim.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)
        if len(answer_src[0]) != 0 and not hasattr(answer_src[0][0][1], "type"):
            if len(nx.dijkstra_path(graph_src, list_of_network_addresses[0], list_of_network_addresses[j])) == 2:
                graph_src.add_edge(str(list_of_network_addresses[0]), str(list_of_network_addresses[j]), color='r', weight=6)
            else:
                for index in range(len(nx.dijkstra_path(graph_src, list_of_network_addresses[0], list_of_network_addresses[j]))):
                    if index != len(nx.dijkstra_path(graph_src, list_of_network_addresses[0], list_of_network_addresses[j])) - 1:
                        graph_src.add_edge(str(list_of_network_addresses[index]), str(list_of_network_addresses[index + 1]), color='r', weight=6)


edges_tc = graph_tc.edges()
colors_tc = [graph_tc[u][v]['color'] for u, v in edges_tc]
weights_tc = [graph_tc[u][v]['weight'] for u, v in edges_tc]

edges_fl = graph_fl.edges()
colors_fl = [graph_fl[u][v]['color'] for u, v in edges_fl]
weights_fl = [graph_fl[u][v]['weight'] for u, v in edges_fl]

edges_plen = graph_plen.edges()
colors_plen = [graph_plen[u][v]['color'] for u, v in edges_plen]
weights_plen = [graph_plen[u][v]['weight'] for u, v in edges_plen]

edges_nh = graph_nh.edges()
colors_nh = [graph_nh[u][v]['color'] for u, v in edges_nh]
weights_nh = [graph_nh[u][v]['weight'] for u, v in edges_nh]

edges_hlim = graph_hlim.edges()
colors_hlim = [graph_hlim[u][v]['color'] for u, v in edges_hlim]
weights_hlim = [graph_hlim[u][v]['weight'] for u, v in edges_hlim]

edges_src = graph_src.edges()
colors_src = [graph_src[u][v]['color'] for u, v in edges_src]
weights_src = [graph_src[u][v]['weight'] for u, v in edges_src]

nx.draw_circular(graph_tc, node_color='blue', node_size=10000, edge_color=colors_tc, width=weights_tc, with_labels=True, label='graph_tc')
plt.show()
nx.draw_circular(graph_fl, node_color='red', node_size=10000, edge_color=colors_fl, width=weights_fl, with_labels=True, label='graph_fl')
plt.show()
nx.draw_circular(graph_plen, node_color='yellow', node_size=10000, edge_color=colors_plen, width=weights_plen, with_labels=True, label='graph_plen')
plt.show()
nx.draw_circular(graph_nh, node_color='green', node_size=10000, edge_color=colors_nh, width=weights_nh, with_labels=True, label='graph_nh')
plt.show()
nx.draw_circular(graph_hlim, node_color='purple', node_size=10000, edge_color=colors_hlim, width=weights_hlim, with_labels=True, label='graph_hlim')
plt.show()
nx.draw_circular(graph_src, node_color='orange', node_size=10000, edge_color=colors_src, width=weights_src, with_labels=True, label='graph_tc')
plt.show()
