#Program vowels vs Consonants

print ("---------------Continue Statements--------------")
for letter in 'abcdefghijklmnopqrstuvwxyz':
    if letter=="a" or letter=="e"  or letter=="i" or letter=="o" or letter=="u":
        continue
    print("The letters are:",letter)

print("--------------Break Statement----------------")
for letter in 'zyxwvutsrqponmlkjihgfedcba':
     if letter=="a" or letter=="e"  or letter=="i" or letter=="o" or letter=="u":
         break
     print("The letters are:",letter)
