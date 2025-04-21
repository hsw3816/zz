import struct

class Udphdr:
    def __init__(self, src_port, dst_port, length, checksum):
        self.src_port = src_port
        self.dst_port = dst_port
        self.length = length
        self.checksum = checksum

    def pack_Udphdr(self):
        packed = struct.pack('!HHHH', self.src_port, self.dst_port,
                             self.length, self.checksum)
        return packed

def unpack_Udphdr(buffer):
    return struct.unpack('!HHHH', buffer[:8])

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

# 테스트 실행
udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udp = udp.pack_Udphdr()
print(packed_udp)  # 바이너리 형태 출력

unpacked_udp = unpack_Udphdr(packed_udp)
print(unpacked_udp)

print('Source Port:{} Destination Port:{} Length:{} Checksum:{}'
      .format(getSrcPort(unpacked_udp), getDstPort(unpacked_udp),
              getLength(unpacked_udp), getChecksum(unpacked_udp)))
