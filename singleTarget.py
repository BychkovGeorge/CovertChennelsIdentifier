# -*- coding: utf-8 -*-

from scapy.layers.inet import TCP
from scapy.layers.inet6 import IPv6
from scapy.sendrecv import sr
import json

print("Введите IPv6 адрес хоста, для которого вы хотите выполнить идентификацию скрытых каналов")
ipv6_addr = input()
result = """
{
    "addr": "",
    "tc": "",
    "fl": "",
    "plen": "",
    "nh": "",
    "hlim": "",
    "src": ""
}"""
result_json = json.loads(result)
result_json["addr"] = ipv6_addr

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

if len(answer_tc[0]) != 0 and not hasattr(answer_tc[0][0][1], 'type'):
    result_json["tc"] = "True"
else:
    result_json["tc"] = "False"
if len(answer_fl[0]) != 0 and not hasattr(answer_fl[0][0][1], 'type'):
    result_json["fl"] = "True"
else:
    result_json["fl"] = "False"

if len(answer_plen[0]) != 0 and not hasattr(answer_plen[0][0][1], 'type'):
    result_json["plen"] = "True"
else:
    result_json["plen"] = "False"

if len(answer_nh[0]) != 0 and not hasattr(answer_nh[0][0][1], 'type'):
    result_json["nh"] = "True"
else:
    result_json["nh"] = "False"

if len(answer_hlim[0]) != 0 and not hasattr(answer_hlim[0][0][1], 'type'):
    result_json["hlim"] = "True"
else:
    result_json["hlim"] = "False"

if len(answer_src[0]) != 0 and not hasattr(answer_src[0][0][1], 'type'):
    result_json["src"] = "True"
else:
    result_json["src"] = "False"

print(result_json)
f = open('res.json', 'w')
f.write(json.dumps(result_json))
f.close()
