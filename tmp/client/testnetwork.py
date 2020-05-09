#!/usr/bin/python

import sys, getopt
from scapy.all import *

#thresholds are number of packets over the poll time that is deemed enough traffic to do our business
FF_IP_PATH = 'FFcloudflareIPs'
FFDoH_counter = 0
FFDoH_threshold = 50
GIT_IP_PATH = 'GitHubIPs'
Git_counter = 0
Git_threshold = 50
POLL_TIME = 20
INTERFACE = "wlp0s20f3"

def test_network():
    """ Analyze the network for Firefox DoH and Github Traffic """
    """ Returns 1 if Firefox Doh Traffic meets threshold """
    """ Returns 2 if Github traffic meets threshold and DoH traffic did not """
    """ Returns -1 if both thresholds are failed """
    bpf = create_bpf_filter(FF_IP_PATH)
    sniff_packets(INTERFACE, bpf, addFFcount)
    if(FFDoH_counter > FFDoH_threshold):
        return(1)

    bpf = create_bpf_filter(GIT_IP_PATH)
    sniff_packets(INTERFACE, bpf, addGitcount)
    if(Git_counter > Git_threshold):
        return(2)
    
    return(-1)

def create_bpf_filter(path):
    """ Create a bpf filter for a list of IPs from a file """
    bpf_filter = "ip and ("
    IPs = open(path)
    addresses = IPs.readlines()
    IPs.close()
    for addr in addresses[:-1]:
        bpf_filter = "%snet %s or " % (bpf_filter, addr)
    bpf_filter = "%snet %s)" % (bpf_filter, addresses[-1])
    return bpf_filter


def sniff_packets(interface, bpf_filter, process):
    """ Sniff for traffic accoring to the filter """
    scapy.all.sniff(iface=interface, filter = bpf_filter, store=False, prn = process, timeout = POLL_TIME)
    

def addFFcount(pkt):
    global FFDoH_counter
    FFDoH_counter += 1
    #print("DoH count: " + str(FFDoH_counter))

def addGitcount(pkt):
    global Git_counter
    Git_counter += 1
    #print("Git count: " + str(Git_counter))

if __name__ == "__main__":
    print(test_network())