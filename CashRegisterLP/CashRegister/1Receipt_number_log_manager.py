import mmap

def receipt_number_log_manager(selecetd_option):
# if option is 'u' then add 1 to file log
# if option is 'i' then just update the number log with the one in mem
    global str_current_receipt_number_mem

    if selecetd_option == 'u':
        int_receipt_number= int(str_current_receipt_number_mem) + 1
        str_updated_receipt_number = str(int_receipt_number)
    elif selecetd_option == 'i':
        str_updated_receipt_number = str_current_receipt_number_mem

    bytestr_receipt_number = str_updated_receipt_number.encode('utf-8')
    _f_ = open('Receipt_number_log/Receipt_num_log.txt', 'r+')
    new_size = len(str_updated_receipt_number)
    _f_.truncate(new_size)
    _mmap_f = mmap.mmap(_f_.fileno(), 0, access=mmap.ACCESS_WRITE)
    _mmap_f.write(bytestr_receipt_number)
    _mmap_f.flush()
    _mmap_f.close()
    _f_.close()