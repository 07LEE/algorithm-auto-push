def solution(my_string):
    unique_chars = set()
    answer = ""
    for char in my_string:
        if char not in unique_chars:
            unique_chars.add(char)
            answer += char
    return answer