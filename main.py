import string

class Packet:
    def __init__(self, sections):

        self.headerLen = None

        self.header = None
        self.payload = None
        self.footer = None

        self.src = sections[0]
        self.dst = sections[1]
        self.seq = sections[2]
        self.ack = sections[3]
        self.data_offset = sections[4]
        self.reserved = sections[5]
        self.flags = sections[6]
        self.window = sections[7]
        self.checksum = sections[8]
        self.urgent_pointer = sections[9]
        self.optionsAndPadding = sections[10]
        self.data = None

    def __str__(self):
        return f"src: {self.src}\ndst: {self.dst}\nseq: {self.seq}\nack: {self.ack}\ndata_offset: {self.data_offset}\nreserved: {self.reserved}\nflags: {self.flags}\nwindow: {self.window}\nchecksum: {self.checksum}\nurgent_pointer: {self.urgent_pointer}\noptionsAndPadding: {self.optionsAndPadding}  "

def split_bin_packet(packet):
    sections = []
    TCP_Packet_Len_Array = [16, 16, 32, 32, 4, 4, 8, 16, 16, 16, 0]

    offset = 0
    print({len(TCP_Packet_Len_Array)})
    for i in range(0, len(TCP_Packet_Len_Array), 1):
        print(f"Processing section {i}\n")
        sections.append(packet[offset : offset + TCP_Packet_Len_Array[i]])
        print(f"Section {i}: {sections[i]}")
        offset = offset + TCP_Packet_Len_Array[i]

    return sections

    # if len(sections) != 3:
    #     raise ValueError(
    #         "Packet must have exactly three sections: header, payload, and footer."
    #     )

    # pkt = Packet()
    # pkt.header = sections[0]
    # pkt.payload = sections[1]
    # pkt.footer = sections[2]


def main():
    print("Hello from cs333-net-utils-team-1oneday!")

    # read packet from file
    # deal with bin or hex input
    # upgrade: determine packet type automagically
    # split packet into sections
    # src/dst - 16/16
    # seq - 32
    # ack - 32
    # dataOffset/reserved/flags/window - 4/3/9/16
    # checksum/urgent pointer - 16/16
    # options/padding - 0-40/
    # data
    # convert bin bits to ascii text
    # output
    # filepath = "packet.bin"
    filepath = "Test_Packet_Hex.txt"

    with open(filepath, "r") as f:
        packet_data = f.read()
        packet_data = packet_data.strip()
        packet_data = packet_data.upper()  # Convert to uppercase for hex detection
        # determine if input is hex or bin
        if all(char in "01" for char in packet_data):
            print("Input is binary.")
        elif all(char in "0123456789ABCDEF" for char in packet_data):
            print("Input is hexadecimal.")
            print("Converting hexadecimal to binary...")
            packet_data_bin = bin(int(packet_data, 16))  # Convert hex to bin
            packet_data_hex = hex(int(packet_data, 16))

        else:
            raise ValueError("Input must be either binary or hexadecimal.")

        print(f"Packet data bin: {packet_data_bin}")
        print(f"Packet data hex: {packet_data_hex}")

        split_packet = split_bin_packet(packet_data_bin[2:])  # Remove '0b' prefix from bin str
        testPacket = Packet(split_packet)


if __name__ == "__main__":
    main()


