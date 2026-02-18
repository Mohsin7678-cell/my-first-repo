# print(ord("+"))
# print(ord("a"))
# print(chr(43))
ch = input("Enter a character: ")

if ord(ch) >= 65 and ord(ch) <= 90:
    print("Uppercase character")
elif ord(ch) >= 97 and ord(ch) <= 122:
    print("Lowercase character")
else:
    print("Not an alphabet character")
