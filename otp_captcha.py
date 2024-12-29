#1. wAF generate a 4-digit otp
"""import random
for i in range(4):
    a=random.randint(0,9)
    print(a,end=' ')"""


"""import random
def digit_4otp():
    for i in range(0,4):
        a=random.randint(0,9)
        yield a
print(list(digit_4otp()))"""

#2.WAF generate a 6-digit otp

"""import random
for i in range(6):
    out=random.randint(0,9)
    print(out,end=' ')"""

#3.WAF generate a 4-6 captcha

"""import random
n=random.randint(4,6)
for i in range(1,n+1):
    out=random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtstuvwxyz0123456789')
    print(out,end=' ')"""






    
