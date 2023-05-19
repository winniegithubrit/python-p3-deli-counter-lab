katz_deli = ["Logan", "Avi", "Spencer", "Gracie"]

def line(katz_deli):
    
    if katz_deli == []:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for person in katz_deli:
            place_in_line = katz_deli.index(person) + 1
            message += f" {place_in_line}. {person}"
        print(message)

line(katz_deli)

def take_a_number(katz_deli, new_customer):
    
    katz_deli.append(new_customer)
    print(f"Welcome, {new_customer}. You are number {len(katz_deli)} in line.")

take_a_number(katz_deli, "John")

def now_serving(katz_deli):
    
    if katz_deli == []:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)

now_serving(katz_deli)
    