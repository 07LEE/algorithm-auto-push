def solution(myString):
    s =  "a","b","c","d","e","f","g","h","i","j","k"
    for i in s:
        myString = myString.replace(i,'l')
    return myString