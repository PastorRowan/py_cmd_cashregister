def pos():
    pass



def Main_menu_main_update_sel_title(sel_option, column_start_x, column_start_y, Main_menu_options, total_titles, chars_between_titles):

    str_new_sel_option = Main_menu_options[sel_option[0]]

    new_sel_option_x = column_start_x
    new_sel_option_y = (column_start_y) + ((sel_option[0] - 1) * chars_between_titles)
    new_pos = pos(new_sel_option_x, new_sel_option_y)

    print(new_pos + str_new_sel_option)