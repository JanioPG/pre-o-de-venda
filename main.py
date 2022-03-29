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
        clean_screen()
        message = ""
        if op == '6':
            print("Program closed")
            break

        else:
            header_text = ["Product Registration", "Product List", "Product Data", "Registry Update", "Delete record"]
            header(header_text[int(op) - 1])
            action = operation(op)
            match op:
                case '1':
                    print(action)

                case '2':
                    if type(action) != 'str': 
                        display(operation(op))
                    else:
                        print(action)
                case '3':
                    if len(action) == 0:
                        print("No matching products.")
                    else:
                        display(action)
                case '4':
                    print(action)
                case '5':
                    print(action)
                case _:
                    message = "ERROR: No corresponding action."
            stop_showing()
