f = int(input("введіть 4-значне число ")) #наприклад 1234
print(f)
number1 = f // 1000
number2 = (f % 1000) //100
number3 = (f % 100) //10
number4 = f % 10
print(number1)
print(number2)
print(number3)
print(number4)
