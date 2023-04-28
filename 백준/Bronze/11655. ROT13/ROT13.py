W = input()
answer = ''

for i in W:
    if i.isupper():
        if (65 <= ord(i) <= 77):
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)
    
    elif i.islower():
        if (97 <= ord(i) <= 109):
            answer += chr(ord(i) + 13)
        else:
            answer += chr(ord(i) - 13)
    
    else:
        answer += i

print(answer)