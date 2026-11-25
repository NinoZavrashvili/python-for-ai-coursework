print("Started the program")
try:
    num1 = float(input("შეიყვანე რიცხვი1: "))
    num2 = float(input("შეიყვანე რიცხვი2: "))

    result = num1 / num2
except ValueError:
    print("შეცდომა: გთხოვთ შეიყვანოთ სწორი რიცხვი!")
except ZeroDivisionError:
    print("შეცდომა: 0-ზე გაყოფა არ შეიძლება!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("შედეგი:", result)
finally:
    print("პროგრამა დასრულდა")
