import hashlib
str1 = input().rstrip()
print(hashlib.sha512(str1.encode()).hexdigest())