# CS333-net-utils-team-1oneday
This repo contains a collection of several network utilities for educational purposes.

This tool is created to disassemble, mutate and reassemble an IP packet.

## Team Members
- Gabriel Jones
- Damian Robert
- Dolan Lavoie

## Getting Started
- Install UV

## Network Packet Structure

# TCP Packet
- Source Port (16 bits): The port number that the packet is coming from
- Destination Port (16 bits): The port number that the packet is being sent to
- Sequence Number (32 bits): The position of the first byte of data
- Acknowledgement Number (32 bits): Confirms that the packet was successfully sent and the next byte to look at
- Data Offset (4 bits): Indicates where the data begins
- Control Flags (8 bits): Bits like SYN, ACK, FIN, RST
- Window Size (16 bits): The amount of data the reciever can accept at a time
- Checksum (16 bits): Used to detect errors my making sure the data and header is correct
- Urgent Pointer (16 bits): Points to data that should be processed immediately
- Options (Variable length): Additional options
- Data: The actual data being sent

# IP Packet
- Version (4 bits): IPv4 or IPv6
- Header Length (4 bits): Size of the IP header
- Type of Service (8 bits): Marks the packet for prioritization and quality of service (QoS).
- Total Length (16 bits): Size of the packet
- Identification (16 bits): ID used for when packets are reassembled
- Flags (3 bits): Dont Fragment/More Fragments indicators
- Fragment Offset (13 bits): The position of this fragment
- Time to Live (TTL) (8 bits): Limits the number of hops a packet can travel
- Protocol (8 bits): Which transport protocol is being used
- Header Checksum (16 bits): Detects errors in the IP header
- Source IP Address (32 bits): IP Address that the packet is coming from
- Destination IP Address (32 bits): IP Address that the packet is going to
- Options (Variable length): Optional features
- Data/Payload: The data or payload, often times the TCP segment

### Sources

- https://www.geeksforgeeks.org/computer-networks/tcp-ip-packet-format/
- https://en.wikipedia.org/wiki/Transmission_Control_Protocol