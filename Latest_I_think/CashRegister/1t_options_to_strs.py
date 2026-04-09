


def Main_menu_options_to_strs(Main_menu_options):

    ls_option_title_strs = []
    for option_num,option_name in Main_menu_options.items():
        option_str = str(option_num) + ' ' + option_name
        ls_option_title_strs.append(option_str)

    return ls_option_title_strs

Main_menu_options = {1 : 'Purchase',
                     2 : 'Refund',
                     3 : 'Invoice',
                     4: 'Stock',
                     5 : 'backup'
                    }

ls_option_title_strs = Main_menu_options_to_strs(Main_menu_options)