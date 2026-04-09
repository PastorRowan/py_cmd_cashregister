import os
from datetime import date


def auto_load_todays_receipts_paths():
    global todays_folder_path
    global todays_receipt_folder_name

    todays_date = date.today()
    str_today_date = todays_date.strftime("%Y-%m-%d")
    todays_receipt_folder_name = 'Receipts_' + str_today_date
    todays_folder_path = 'Receipts/' + todays_receipt_folder_name
    print(str_today_date)

# this is gonna happen at the start of the program like when we autoload the current receipt number


def auto_create_todays_receipt_folder():
    global todays_folder_path
    if not (os.path.exists(todays_folder_path)):
        os.makedirs(todays_folder_path)



auto_load_todays_receipts_paths()

auto_create_todays_receipt_folder()

print(todays_folder_path)
print(todays_receipt_folder_name)




























# do wewant to store the current date as a global varialbe or in memory yeah lets rather try store it in memry as a lobal aralbe i liek tah slutoin better