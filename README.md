# ble_pcap_dissector
A python tool to dissect various BLE GATT packets for replay and analysis.

# Requirements:

Scapy-Radio

https://github.com/BastilleResearch/scapy-radio


To run the code:

python3 ble_pkt_filter.py 

  Submit the location of the pcap file: file.pcap
  Please choose:
  1. Filter only write_req
  2. Filter only write_cmd
  What do you want to analyse? : 1
  Handle  Hex                                        Ascii                    
  -----------------------------------------------------------------------------------------------------------
  0x12    0100                                       b'\x01\x00'              
  0xe     ab04000c                                   b'\xab\x04\x00\x0c'      
  0xe     ab04000c                                   b'\xab\x04


More features are to be released soon
