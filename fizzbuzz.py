for n in range(1,101):
    if n%3 == 0 and n % 5 ==0:
        print("Fizzbuzz")
    if n % 3 == 0:
        print("fizz")
    if n % 5 ==0:
        print("Buzz")
    else :
        print(n)