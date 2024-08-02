#Pizza Shop


bill = 0
print("what size of pizza do you want? S, M or L")
size = input()
if size == "L":
    bill = bill + 25
    print("Add pepperoni for large pizza (Y or N): ")
    add_pepperoni = input()
    if add_pepperoni == "Y":
        bill = bill + 3
elif size == "M":
    bill = bill + 20
    print("Add pepperoni for medium or large pizza (Y or N): ")
    add_pepperoni = input()
    if add_pepperoni == "Y":
        bill = bill + 3
else:
    bill = bill + 15
    print("Add pepperoni for small pizza (Y or N): ")
    add_pepperoni = input()
    if add_pepperoni == "Y": 
         bill = bill + 2
print("Add extra cheese for any size pizza (Y or N): ")
extra_cheese = input()
if extra_cheese == "Y":
        bill = bill + 1
print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")
