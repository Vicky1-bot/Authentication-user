import getpass
database={"sreekanth":"123456","vicky":"476828"}
username=input("Enter your username:")
password=input("Enter your password:")

for i in database.keys():
    if username==i:
        while password!=database.get(i):
            password=input("Enter your password again:")
            break
print("Verified")