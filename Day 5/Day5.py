import random

print("Welcome to the PyPassword Generator!")

print("How many letters would you like in your password?")
nr_letters = int(input())

print("How many symbols would you like?")
nr_symbols = int(input())

print("How many numbers would you like?")
nr_numbers = int(input())

password = ""
for i in range(0, nr_letters):
    password += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in range(0, nr_symbols):
    password += random.choice("!@#$%^&*()")
for i in range(0, nr_numbers):
    password += random.choice("0123456789")
print(f"Here is your pasword: {password}")
