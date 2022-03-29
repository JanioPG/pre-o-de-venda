from option import operation, request_from_user
from interface import header, menu, clean_screen, display, stop_showing

message = ""
while True:
    clean_screen()
    menu("SALE PRICE", ["Register product", "Consult all products", "Consult individual products", "Update a product registration", "Delete record", "Quit"], message)
    op = request_from_user("\nOption: ")
    
    if op not in ['1', '2', '3', '4', '5', '6']:
        message = "Invalid option"
    else:
        message = ""
        if op == '6':
            break
        else:
            clean_screen()
            action = operation(op)
            print(type(action))
            match op:
                case '1':
                    header("Product registration")
                    message = action
                case '2':
                    header("Product List")
                    if type(action) != 'str': 
                        display(action)
                    else:
                        print(action)
                    stop_showing()
                case '3':
                    pass
                case '4':
                    pass
                case '5':
                    print(action)
                    stop_showing()

                case _:
                    message = "ERROR: No corresponding action."
            print(message)
