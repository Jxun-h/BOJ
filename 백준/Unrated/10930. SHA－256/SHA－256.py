import hashlib
str1 = input().rstrip()
print(hashlib.sha256(str1.encode()).hexdigest())