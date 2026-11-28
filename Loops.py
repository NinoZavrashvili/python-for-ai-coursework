# # 1 HW

print("Program started!")

int_number = int(input("Enter a number: "))

factorial = 1

for i in range(int_number, 0, -1):
    factorial *= i

print(factorial)

print("Program ended!")

# #2 HW

print("Program started!")

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")

print("Program ended!")

#3 HW
print("Program started!")

price = 50
print("Amount to pay: ", price, "GEL")
print("Please insert bills of 5, 10, or 20 GEL.")

while True:
    bill = int(input("Insert a bill: "))
    if bill == 5 or bill == 10 or bill == 20:
        price -= bill
        if price > 0:
            print("Remaining amount to pay: ", price, "GEL")    
        if price == 0:
            print("Payment complete!")
            break
        if price < 0:
            print("Change to be returned: ", -price, "GEL")
            break
    else:
        print("Invalid bill! Please insert a valid bill.")
print("Program ended!")
