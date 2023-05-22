string = input()
letters = []

for char in string:
    if char.isupper():
        letters.append(char)

required_letters = ['M', 'O', 'B', 'I', 'S']

if all(letter in letters for letter in required_letters):
    print("YES")
else:
    print("NO")