from dpkt import *
fp = open('testtcp.pcap')
pcapy = pcap.Reader(fp)
for ts,buf in pcapy:
