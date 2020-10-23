# -*- coding: utf-8 -*-

import os
import sys
from scapy.layers.inet import ICMP, IP, TCP
from scapy.layers.inet6 import IPv6, IPv6ExtHdrRouting, ICMPv6EchoRequest
from scapy.sendrecv import sendp, sr
from scapy.volatile import RandString
import itertools
import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt

from functions import print_matrix

print("Введите IPv6 адреса хостов сети через запятую, кроме адреса текущего хоста")
network_addresses = input()
list_of_network_addresses = network_addresses.split(", ")
print("Выберите тип скрытого канала, для которого вы хотите выполнить идентификацию (введите число):\n"
      "1 - traffic class\n"
      "2 - flow label\n"
      "3 - payload length\n"
      "4 - next header\n"
      "5 - hop limit\n"
      "6 - source address\n")
channel_type = input()

result_matrix = [0] * (len(list_of_network_addresses) + 1)
for i in range(len(list_of_network_addresses) + 1):
    result_matrix[i] = [0] * (len(list_of_network_addresses) + 1)

for j in range(len(list_of_network_addresses)):
    packet = IPv6(dst=list_of_network_addresses[j]) / TCP(dport=22)
    if channel_type == "1":
        packet.tc = 18
    elif channel_type == "2":
        packet.fl = 18
    elif channel_type == "3":
        packet.plen = 18
    elif channel_type == "4":
        packet.nh = 18
    elif channel_type == "5":
        packet.hlim = 18
    elif channel_type == "6":
        packet.src = 18
    else:
        print("Ошибка ввода")
        raise SystemExit
    answer = sr(packet, timeout=4)
    if len(answer[0]) != 0 and not hasattr(answer[0][0][1], "type"):
        result_matrix[0][j + 1] = 1
        result_matrix[j + 1][0] = 1

for k in range(len(list_of_network_addresses)):
    counter = 1
    while counter < len(list_of_network_addresses):
        if k != counter:
            packet = IPv6(dst=list_of_network_addresses[counter]) / IPv6ExtHdrRouting(type=0, addresses=[list_of_network_addresses[k]], segleft=1) / TCP(dport=22)
            if channel_type == "1":
                packet.tc = 18
            elif channel_type == "2":
                packet.fl = 18
            elif channel_type == "3":
                packet.plen = 18
            elif channel_type == "4":
                packet.nh = 18
            elif channel_type == "5":
                packet.hlim = 18
            elif channel_type == "6":
                packet.src = 18
            else:
                print("Ошибка ввода")
                raise SystemExit
            answer = sr(packet, timeout=4)
            if len(answer[0]) != 0:
                print(answer[0][0])
                result_matrix[k + 1][counter + 1] = 1
                result_matrix[counter + 1][k + 1] = 1
        counter += 1

print_matrix(result_matrix)

# covert_channels_graph = nx.Graph()
#
# covert_channels_graph.add_node('Текущий хост')
# for z in range(len(list_of_network_addresses)):
#     covert_channels_graph.add_node(list_of_network_addresses[z])
#
# for x in range(len(result_matrix[0])):
#     for y in range(len(result_matrix[0])):
#         if result_matrix[x][y] == 1:
#             if x == 0:
#                 covert_channels_graph.add_edge('Текущий хост', list_of_network_addresses[y - 1])
#             elif y == 0:
#                 covert_channels_graph.add_edge(list_of_network_addresses[x - 1], 'Текущий хост')
#             else:
#                 covert_channels_graph.add_edge(list_of_network_addresses[x - 1], list_of_network_addresses[y - 1])
#
# nx.draw_circular(covert_channels_graph, node_color='red', node_size=3000, with_labels=True)
# plt.show()
