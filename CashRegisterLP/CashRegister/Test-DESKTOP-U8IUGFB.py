'''

byte_object = b'1'

string_object = byte_object.decode()

print(string_object)

print(byte_object)
'''



byte_list = [b'0', b'\r', b'\n', b'1']
test_byte = b'1'

if test_byte in byte_list:
    print(f"{test_byte} is present in the list.")
else:
    print(f"{test_byte} is not present in the list.")