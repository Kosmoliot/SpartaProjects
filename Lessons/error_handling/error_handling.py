try:
    with open("order.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.rstrip('\n'))
except FileNotFoundError as errmsg:
    print("There has been an error, panic!")
    print(errmsg)
finally:
    print("Execution Complete!")
    
    
def write_to_file(file, order_item):
    try:
        with open(file, "a") as file:
            file.write(order_item + "\n")
    except FileNotFoundError as errmsg:
        print("There has been an error, panic!")
        print(errmsg)
        
write_to_file("order.txt", "Burger")