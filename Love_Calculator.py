name1 = input()
name2 = input()

combined_name = name1.lower()+name2.lower()

T = combined_name.count("t")
R = combined_name.count("r")
U = combined_name.count("u")
E = combined_name.count("e")

true = T+R+U+E

print(true)

L = combined_name.count("l")
O = combined_name.count("o")
V = combined_name.count("v")
E = combined_name.count("e")

love = L+O+V+E


true_love = f"{true}{love}"


int_true_love = int(true_love)

print("The Love Calculator is calculating your score...")

if int_true_love > 40 and int_true_love < 50:
    print(f"Your score is {true}{love}, you are alright together.")
elif int_true_love < 10:
    print(f"Your score is {true}{love}, you go together like coke and mentos.")
elif int_true_love > 90:
    print(f"Your score is {true}{love}, you go together like coke and mentos.")
else:
    print(f"Your score is {true}{love}.")
