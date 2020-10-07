from scapy.layers.inet import ICMP, IP, TCP
from scapy.layers.inet6 import IPv6
from scapy.sendrecv import sendp, sr

print("Введите IPv6 адрес хоста, для которого вы хотите выполнить идентификацию скрытых каналов")
ipv6_addr = input()

packet_tc = IPv6(dst=ipv6_addr) / TCP(dport=22)
packet_fl = IPv6(dst=ipv6_addr) / TCP(dport=22)
packet_plen = IPv6(dst=ipv6_addr) / TCP(dport=22)
packet_nh = IPv6(dst=ipv6_addr) / TCP(dport=22)
packet_hlim = IPv6(dst=ipv6_addr) / TCP(dport=22)
packet_src = IPv6(dst=ipv6_addr) / TCP(dport=22)

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

if len(answer_tc[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Traffic Class возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Traffic Class")

if len(answer_fl[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Flow Label возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Flow Label")

if len(answer_plen[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Payload Length возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Payload Length")

if len(answer_nh[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Next Header возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Next Header")

if len(answer_hlim[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Hop Limit возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Hop Limit")

if len(answer_src[0]) != 0:
    print("Скрытый канал до выбранного хоста по полю Source Address возможен")
else:
    print("Невозможно построить скрытый канал до выбранного хоста по полю Source Address")
