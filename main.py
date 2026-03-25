def split_bin_packet(packet):
    sections = []
    TCP_Packet_Len_Array = [16, 16, 32, 32, 4, 4, 8, 16, 16, 16, 40]

    chunk_size = TCP_Packet_Len_Array[0]
    offset = 0

    for i in range(0, len(packet), chunk_size):
        sections.append(packet[offset : i + TCP_Packet_Len_Array[i]])
        print(f"Section {i}: {sections[i]}")
        offset = i + TCP_Packet_Len_Array[i]

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
            packet_data = bin(int(packet_data, 16))  # Convert hex to binary

        else:
            raise ValueError("Input must be either binary or hexadecimal.")

        print(f"Packet data: {packet_data}")

        split_bin_packet(packet_data)


if __name__ == "__main__":
    main()


class Packet:
    def __init__(self):

        self.headerLen = None

        self.header = None
        self.payload = None
        self.footer = None

        self.src = None
        self.dst = None
        self.seq = None
        self.ack = None
        self.data_offset = None
        self.reserved = None
        self.flags = None
        self.window = None
        self.checksum = None
        self.urgent_pointer = None
        self.options = None
        self.padding = None
        self.data = None

    def __str__(self):
        return f"Header: {self.header}, Payload: {self.payload}, Footer: {self.footer}"
