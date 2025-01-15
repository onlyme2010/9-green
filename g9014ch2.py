"""------1-------"""
from math import sqrt
sonlar = list(range(1,500))
for s in sonlar:
    if s < 200:
        print(s**2)
    elif s > 300:
        print(sqrt(s))
"""------2-------"""
friends = []
while True:
    ism = input("Ismingizni kiriting: ")
    if ism == "exit" or ism == "quit":
        break
    else:
        friends.append(ism)
print(friends)
"""------3-------"""
# def info(ism:str,familia:str,yosh:int,tel:int,username:str,manzil:str):
#     """hamma infolaringiz"""





















