import hashlib
str1 = input().rstrip()
print(hashlib.sha1(str1.encode()).hexdigest())