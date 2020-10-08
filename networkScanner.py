import os
import sys
from scapy.layers.inet import ICMP, IP, TCP
from scapy.layers.inet6 import IPv6, IPv6ExtHdrRouting
from scapy.sendrecv import sendp, sr
from functions import print_matrix


print("Введите IPv6 адреса хостов сети через запятую, кроме адреса текущего хоста")
network_addresses = input()
list_of_network_addresses = network_addresses.split(", ")
print("Выберите тип скрытого канала, для которого вы хотите выполнить идентификацию (введите число):"
      "1 - traffic class"
      "2 - flow label"
      "3 - payload length"
      "4 - next header"
      "5 - hop limit"
      "6 - source address")
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
    if len(answer[0]) != 0:
        result_matrix[0][j + 1] = 1

print_matrix(result_matrix)
