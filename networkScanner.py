# -*- coding: utf-8 -*-

import os
import sys
import scapy as scapy

from scapy.layers.inet import ICMP, IP, TCP
from scapy.layers.inet6 import IPv6, IPv6ExtHdrRouting, ICMPv6EchoRequest
from scapy.sendrecv import sendp, sr
from graphviz import Digraph
from scapy.volatile import RandString
import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt
from scapy.utils import PcapWriter

from functions import print_matrix

print("Введите IPv6 адреса хостов сети через запятую, кроме адреса текущего хоста")
network_addresses = input()
list_of_network_addresses = network_addresses.split(", ")

graph_tc = nx.Graph()
graph_fl = nx.Graph()
graph_plen = nx.Graph()
graph_nh = nx.Graph()
graph_hlim = nx.Graph()
graph_src = nx.Graph()

graph_tc.add_node('Текущий хост Traffic Class')
for z in range(len(list_of_network_addresses)):
    graph_tc.add_node(list_of_network_addresses[z])
graph_fl.add_node('Текущий хост Flow Label')
for z in range(len(list_of_network_addresses)):
    graph_fl.add_node(list_of_network_addresses[z])
graph_plen.add_node('Текущий хост Payload Length')
for z in range(len(list_of_network_addresses)):
    graph_plen.add_node(list_of_network_addresses[z])
graph_nh.add_node('Текущий хост Next Header')
for z in range(len(list_of_network_addresses)):
    graph_nh.add_node(list_of_network_addresses[z])
graph_hlim.add_node('Текущий хост Hop Limit')
for z in range(len(list_of_network_addresses)):
    graph_hlim.add_node(list_of_network_addresses[z])
graph_src.add_node('Текущий хост Source Address')
for z in range(len(list_of_network_addresses)):
    graph_src.add_node(list_of_network_addresses[z])

for j in range(len(list_of_network_addresses)):

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
        graph_tc.add_edge('Текущий хост Traffic Class', str(list_of_network_addresses[j]))
    if len(answer_fl[0]) != 0 and not hasattr(answer_fl[0][0][1], "type"):
        graph_fl.add_edge('Текущий хост Flow Label', str(list_of_network_addresses[j]), label='fl')
    if len(answer_plen[0]) != 0 and not hasattr(answer_plen[0][0][1], "type"):
        graph_plen.add_edge('Текущий хост Payload Length', str(list_of_network_addresses[j]), label='plen')
    if len(answer_nh[0]) != 0 and not hasattr(answer_nh[0][0][1], "type"):
        graph_nh.add_edge('Текущий хост Next Header', str(list_of_network_addresses[j]), label='nh')
    if len(answer_hlim[0]) != 0 and not hasattr(answer_hlim[0][0][1], "type"):
        graph_hlim.add_edge('Текущий хост Hop Limit', str(list_of_network_addresses[j]), label='hlim')
    if len(answer_src[0]) != 0 and not hasattr(answer_src[0][0][1], "type"):
        graph_src.add_edge('Текущий хост Source Address', str(list_of_network_addresses[j]), label='src')

    dump = PcapWriter("test.pcap", append=True, sync=True)
    dump.write(packet_fl)



# блок с использованием дополнительного заголовка маршрутизации
#
# for k in range(len(list_of_network_addresses)):
#     counter = 1
#     while counter < len(list_of_network_addresses):
#         if k != counter:
#             packet = IPv6(dst=list_of_network_addresses[counter]) / IPv6ExtHdrRouting(type=2, addresses=[list_of_network_addresses[k]]) / ICMPv6EchoRequest() / TCP(dport=22) / "test"
#             if channel_type == "1":
#                 packet.tc = 18
#             elif channel_type == "2":
#                 packet.fl = 18
#             elif channel_type == "3":
#                 packet.plen = 18
#             elif channel_type == "4":
#                 packet.nh = 18
#             elif channel_type == "5":
#                 packet.hlim = 18
#             elif channel_type == "6":
#                 packet.src = 18
#             else:
#                 print("Ошибка ввода")
#                 raise SystemExit
#             answer = sr(packet, timeout=4)
#             if len(answer[0]) != 0:
#                 print(answer[0][0])
#                 result_matrix[k + 1][counter + 1] = 1
#                 result_matrix[counter + 1][k + 1] = 1
#         counter += 1


# for x in range(len(result_matrix[0])):
#     for y in range(len(result_matrix[0])):
#         if result_matrix[x][y] == 1:
#             if x == 0:
#                 covert_channels_graph.add_edge('Текущий хост', list_of_network_addresses[y - 1])
#             elif y == 0:
#                 covert_channels_graph.add_edge(list_of_network_addresses[x - 1], 'Текущий хост')
#             else:
#                 covert_channels_graph.add_edge(list_of_network_addresses[x - 1], list_of_network_addresses[y - 1])

nx.draw_circular(graph_tc, node_color='blue', node_size=10000, with_labels=True, label='graph_tc')
plt.show()
nx.draw_circular(graph_fl, node_color='red', node_size=10000, with_labels=True, label='graph_fl')
plt.show()
nx.draw_circular(graph_plen, node_color='yellow', node_size=10000, with_labels=True, label='graph_plen')
plt.show()
nx.draw_circular(graph_nh, node_color='green', node_size=10000, with_labels=True, label='graph_nh')
plt.show()
nx.draw_circular(graph_hlim, node_color='purple', node_size=10000, with_labels=True, label='graph_hlim')
plt.show()
nx.draw_circular(graph_src, node_color='orange', node_size=10000, with_labels=True, label='graph_tc')
plt.show()

