import mmap

def receipt_number_log_manager():
    global str_current_receipt_number_mem
    int_next_receipt_number= int(str_current_receipt_number_mem) + 1
    str_next_receipt_number = str(int_next_receipt_number)
    bytestr_next_receipt_number = str_next_receipt_number.encode('utf-8')
    _f_ = open('Receipt_number_log/Receipt_num_log.txt', 'r+')
    new_size = len(str_next_receipt_number)
    _f_.truncate(new_size)
    _mmap_f = mmap.mmap(_f_.fileno(), 0, access=mmap.ACCESS_WRITE)
    _mmap_f.write(bytestr_next_receipt_number)
    _mmap_f.flush()
    _mmap_f.close()
    _f_.close()

str_current_receipt_number_mem = 1

receipt_number_log_manager()