character = input("enter character : ")   
if ord(character) >= 65 and ord(character) <= 90:
    print("entered character is alphabet")
    print("uppercase character")
    if character in ("A","E","I","O","U"):
     print("entered character is a vowel")
    else:
     print("entered character is a consonant")
elif ord(character) >= 97 and ord(character) <= 122:
    print("entered character is alphabet")
    print("Lowercase character")
    if character in ("a","e","i","o","u"):
     print("entered character is a vowel")
    else:
     print("entered character is a consonant")
else:
    print("entered character is a special character")
    print("entered character is not alphabet")   
    
    
   