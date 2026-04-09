def pos (x,y):
    return '\x1b[' + str(y) + ';' + str(x) + 'H'



def dic_column_title_coords_and_percentages(box_length, dic_title_plus_frac_apart_out_of_1_whole, box_start_x, title_start_x, title_start_y):

    available_len = box_length + (title_start_x - box_start_x)

    
    dic_column_title_coords_and_percentages = {}
    ls_column_titles = []

    for title, percentage in dic_title_plus_frac_apart_out_of_1_whole.items():

        float_x_offset = percentage * available_len

        int_x_offset = int(float_x_offset)

        curr_title_x = title_start_x + int_x_offset
        
        curr_title_pos = pos(curr_title_x, title_start_y)
        ls_column_titles.append(curr_title_pos)
        ls_column_titles.append(title)

        str_column_title = ''.join(ls_column_titles)

        dic_column_title_coords_and_percentages[title] = {'str' : str_column_title, 'coords' : [curr_title_x, title_start_y], 'percentage' : percentage}
    

    return dic_column_title_coords_and_percentages










boxes_start_and_end_percentages = {'block_1' : {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5},
                              
                             'block_2' : {'percentage_start_x' : 0.5, 'percentage_start_y' : 0, 'percentage_end_x' : 1, 'percentage_end_y' : 0.5}
                             }




def block_coords(menu_length, menu_height, boxes_start_and_end_percentages, menu_start_x, menu_start_y, menu_end_x, menu_end_y):


    boxes_start_and_end_coords = {}

    for box in boxes_start_and_end_percentages:
        curr_box = boxes_start_and_end_percentages[box]
        curr_box_start_and_end_coords = {}

        # start x
        percentage_start_x = curr_box['percentage_start_x']
        float_x_offset = percentage_start_x * menu_length
        int_x_offset = int(float_x_offset)
        curr_box_start_x = menu_start_x + int_x_offset
        curr_box_start_and_end_coords['start_x'] = curr_box_start_x

        # start y
        percentage_start_y = curr_box['percentage_start_y']
        float_start_y_offset = percentage_start_y * menu_height
        int_start_y_offset = int(float_start_y_offset)
        curr_box_start_y = menu_start_y + int_start_y_offset
        curr_box_start_and_end_coords['start_y'] = curr_box_start_y

        # end x
        percentage_end_x = curr_box['percentage_end_x']
        float_end_x_offset = percentage_end_x * menu_length
        int_end_x_offset = int(float_end_x_offset)
        curr_box_end_x = menu_start_x + int_end_x_offset
        curr_box_start_and_end_coords['end_x'] = curr_box_end_x

        # end y
        percentage_end_y = curr_box['percentage_end_y']
        float_end_y_offset = percentage_end_y * menu_height
        int_end_y_offset = int(float_end_y_offset)
        curr_title_end_y = menu_start_y + int_end_y_offset
        curr_box_start_and_end_coords['end_y'] = curr_title_end_y


        boxes_start_and_end_coords[box] = curr_box_start_and_end_coords


    return boxes_start_and_end_coords


def boxes_length_and_height(boxes_start_and_end_coords):




    boxes_length_and_height = {}
    for box in boxes_start_and_end_coords:
        curr_box = boxes_start_and_end_coords[box]

        box_length_and_height = {}

        # l
        start_x = curr_box['start_x']
        end_x = curr_box['end_x']
        box_length = end_x - start_x
        box_length_and_height['length'] = box_length

        # w
        start_y = curr_box['start_y']
        end_y = curr_box['end_y']
        box_height = end_y - start_y
        box_length_and_height['height'] = box_height

        boxes_length_and_height[box] = box_length_and_height

    return boxes_length_and_height



boxes_start_and_end_coords___ = {'block_1': {'start_x': 2, 'start_y': 2, 'end_x': 27, 'end_y': 14}, 
                                 'block_2': {'start_x': 27, 'start_y': 2, 'end_x': 52, 'end_y': 14}
                                 }


def boxes_start_and_end_poses_(boxes_start_and_end_coords):

    boxes_start_and_end_poses = {}
    for curr_box in boxes_start_and_end_coords:
        curr_box_start_and_end_coords = boxes_start_and_end_coords[curr_box]

        # start_pos
        curr_box_start_pos = pos(curr_box_start_and_end_coords['start_x'],curr_box_start_and_end_coords['start_y'])
        # end_pos
        curr_box_end_pos = pos(curr_box_start_and_end_coords['end_x'],curr_box_start_and_end_coords['end_y'])


        boxes_start_and_end_poses[curr_box] = {'start_pos' : curr_box_start_pos, 'end_pos' : curr_box_end_pos}

    return boxes_start_and_end_poses
    




menu_length = 50
menu_height = 25
menu_start_x = 2
menu_start_y = 2
menu_end_x = 52
menu_end_y = 27




boxes_start_and_end_coords = block_coords(menu_length, menu_height, boxes_start_and_end_percentages, menu_start_x, menu_start_y, menu_end_x, menu_end_y)

boxes_start_and_end_poses = boxes_start_and_end_poses_(boxes_start_and_end_coords)



boxes_size = boxes_length_and_height(boxes_start_and_end_coords)


def empt_block_info_into_full_block(boxes_info, boxes_start_and_end_percentages, boxes_start_and_end_coords, boxes_start_and_end_poses, boxes_size):


    for box in boxes_info:

        curr_box = boxes_info[box]
        curr_box['boxes_start_and_end_percentages'] = boxes_start_and_end_percentages[box]
        curr_box['start_and_end_coords'] = boxes_start_and_end_coords[box]
        curr_box['start_and_end_poses'] = boxes_start_and_end_poses[box]
        curr_box['size'] = boxes_size[box]

    return boxes_info

boxes_info_empt = {'block_1' : {'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} },
              
              'block_2' : { 'boxes_start_and_end_percentages' : {}, 'start_and_end_coords' : {}, 'start_and_end_poses' : {}, 'size' : {} }
              }

boxes_start_and_end_percentages = {'block_1' : {'percentage_start_x' : 0, 'percentage_start_y' : 0, 'percentage_end_x' : 0.5, 'percentage_end_y' : 0.5},
                              
                             'block_2' : {'percentage_start_x' : 0.5, 'percentage_start_y' : 0, 'percentage_end_x' : 1, 'percentage_end_y' : 0.5}
                             }


boxes_start_and_end_coords = block_coords(menu_length, menu_height, boxes_start_and_end_percentages, menu_start_x, menu_start_y, menu_end_x, menu_end_y)

boxes_start_and_end_poses = boxes_start_and_end_poses_(boxes_start_and_end_coords)

boxes_size = boxes_length_and_height(boxes_start_and_end_coords)

boxes_info = empt_block_info_into_full_block(boxes_info_empt, boxes_start_and_end_percentages, boxes_start_and_end_coords, boxes_start_and_end_poses, boxes_size)

print(boxes_info)








# ok shoudlw enow we ahve 2 otion either we try to 100% seperate every single block information thing and then what we will end uyp with is with seperaet blokc iunformation for each lboc or we can 
# say t he star tna dne dpsotions of each block is found in this dicitoanry and the dimensions f the blocksd are found in this dicitoanry or we can just bahve many many different idcitoanries and data sturutue#
# all seperated by each thig yeah that oudsn way way better to me