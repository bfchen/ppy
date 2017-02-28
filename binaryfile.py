import struct

# write
#file = open("/Users/admin/Desktop/binary.dat", "wb")

# for n in range(1000):
# 	data = struct.pack("i", n)
# 	file.write(data)
# file.close()


# read
file = open("/Users/admin/Desktop/binary.dat", "rb")
size = struct.calcsize("i")

byteRead = file.read(size)
while byteRead:
	value = struct.unpack("i", byteRead)
	value = value[0]
	print(value, end = " ")
	byteRead = file.read(size)

file.close()