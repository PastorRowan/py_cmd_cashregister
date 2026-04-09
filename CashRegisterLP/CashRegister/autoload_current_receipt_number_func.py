import mmap

import os

def auto_load_current_receipt_number():
    global str_current_receipt_number_mem

    if os.path.getsize('Receipt_number_log/Receipt_num_log.txt') == 0:
        str_current_receipt_number_mem = '1'
        with open ('Receipt_number_log/Receipt_num_log.txt', 'r+') as f_:
            f_.write('1')
            print('Current receipt number has been made 1')
    else:
        with open('Receipt_number_log/Receipt_num_log.txt', 'r') as f:
            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mmap_file:
                byte_string_current_receipt_number_hard = mmap_file.read()
                str_current_receipt_number = byte_string_current_receipt_number_hard.decode('utf-8')
                str_current_receipt_number_mem = str_current_receipt_number


str_current_receipt_number_mem = 0

auto_load_current_receipt_number()

print(str_current_receipt_number_mem)