def fizzBuzz(n):
    for i in range(1, n + 1):
        if i % a == 0 and i % b == 0:
            print("FizzBuzz")
        elif i % a == 0:
            print("Fizz")
        elif i % b == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    n = int(input("enter the range of number: ").strip())
    a=int(input("enter the value of a: "))
    b=int(input("enter the value of b: "))
    fizzBuzz(n)
