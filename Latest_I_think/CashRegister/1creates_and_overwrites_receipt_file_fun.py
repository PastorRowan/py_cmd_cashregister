# shit ok what the fuck idd i do here so made this creates and overwrites receipt file func. i guess
# i could make a receipt fie in meory is euqal. ah the receipt text actreaiton fucntion already cehks that
# and then reutnres ok thats fine ok get rid of that ok now what we could do is truncate the
# ok so now we have truncated the file to the correct size what do we do next
# now we open the file using a mmap then write all hte changes to the mmap then save the changes
# using the flus

import mmap
from datetime import date

def auto_load_todays_receipts_path_plus_date():
    global todays_date
    global todays_folder_path
    global todays_receipt_folder_name

    todays_date_ = date.today()
    str_todays_date = todays_date_.strftime("%Y-%m-%d")
    todays_receipt_folder_name = 'Receipts_' + str_todays_date
    todays_folder_path = 'Receipts/' + todays_receipt_folder_name
    todays_date = str_todays_date

def creates_and_overwrites_receipt_file_func(str_text, file_address): # recept str was a list
    file = open(file_address, 'w+')
    new_size = len(str_text)
    file.truncate(new_size)
    mapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_WRITE)
    file.close()
    bytestr_text = str_text.encode('utf-8')
    mapped_file.write(bytestr_text)
    mapped_file.flush()
    mapped_file.close()



text = '''
2024-01-01 John Smith

1x GTX220_2GB 1980.01
58598y54u94u9

1980.01
'''
todays_date = 0
todays_folder_path = 0
todays_receipt_folder_name = 0
current_receipt_number_mem = '20'

auto_load_todays_receipts_path_plus_date()

receipt_address_ = todays_folder_path + '\Receipt' + current_receipt_number_mem + '.txt'

creates_and_overwrites_receipt_file_func(text, receipt_address_)