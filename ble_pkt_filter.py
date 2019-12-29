import os
import binascii
import codecs
from scapy.all import *


def accept_pcap():
    while True:
        try:
            # accepting the pcap file
            pcap_input = input("Submit the location of the pcap file: ")
            # Converts relative path into full path
            fullPath = os.path.join(os.getcwd(), pcap_input)
            # Reading the pcap
            pcap = rdpcap(fullPath)
            return pcap
        except BaseException:
            print(" Error 404..... Pcap not found!! ")
        else:
            break


def get_hex_ascii(pcap, i):
    # Loop to read all data and skim data
    a = pcap[i].data
    x = binascii.hexlify(a)
    y = str(x, 'ascii')
    print('{:7} {:42} {:25}'.format(hex(pcap[i].gatt_handle), y, str(a)))
#	##Create another pcap file for filtered content
#	wrpcap("filter.pcap",pcap[i])


def opcode_handling(pcap, req_opcode):
    print('{:7} {:42} {:25}'.format("Handle", "Hex", "Ascii"))
    print("-----------------------------------------------------------------------------------------------------------")
    for i in range(len(pcap) - 1):
        try:
            pkt_opcode = pcap[i + 1].opcode
            if pkt_opcode == req_opcode:
                get_hex_ascii(pcap, i + 1)
        except BaseException:
            continue
    print("Enjoy analysing now! :) ")


def let_user_pick():
    pcap = accept_pcap()
    print("Please choose:")
    print("1. Filter only write_req")
    print("2. Filter only write_cmd")
    while True:
        choice = input("What do you want to analyse? : ")
        try:
            req_opcode = filter_packets(int(choice))
            opcode_handling(pcap, req_opcode)
            return None
        except BaseException:
            print("Trying to test my patience? Good luck baby! ")
        else:
            break


def filter_packets(choice):
    try:
        if choice == 1:
            opcode = 18
        elif choice == 2:
            opcode = 82
    except BaseException:
        print("You gotta choose only from the given options bruh -_-")
    return opcode


let_user_pick()
