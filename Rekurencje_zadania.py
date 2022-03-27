from typing import List

def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    numbers(n - 1)


def fib(n) -> int:
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return number * power(number, n - 1)

def reverse(txt: str) -> str:
    if len(txt) == 0:
        return ""
    else:
        return txt[len(txt) - 1] + reverse(txt[0: len(txt) - 1])

def factorial(n: int) -> int:
    if n < 1:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def prime(n: int) -> bool:
    if n < 2:
        return False




txt: str = "adam"
new_txt: str = ""
new_txt += txt[len(txt) - 1]
txt = txt.replace(txt[3], '')
print(txt)
print(new_txt)
print(reverse(txt))
print(factorial(4))
print(prime(9))


print(fib(5))
print(power(10,4))
numbers(10)






