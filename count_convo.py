instr = input("Enter a word :  ")
instr = instr.upper()
cv = 0
cc = 0

for c in instr.lower():
    if c in "aeiou":
        cv += 1
    else:
        cc += 1

print("Vowels:", cv)
print("Consonants:", cc)
