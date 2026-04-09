def Full_checkout_func():
    global current_cart
    global item_data_in_memory

    receipt_text = create_receipt_text_func(current_cart)
    creates_receipt_file_func(receipt_text)
    receipt_number_log_and_mem_updater('u')
    return 1




loads_and_removes_current_cart_item_s_data_to_memory()

Full_checkout_func()