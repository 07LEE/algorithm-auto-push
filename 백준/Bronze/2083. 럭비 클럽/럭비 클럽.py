while True:
    club = list(input().split(' '))
    if int(club[1]) > 17 or int(club[2]) >= 80:
        print(club[0], 'Senior')
    elif int(club[1]) == 0 and int(club[2]) == 0:
        break
    else :
        print(club[0], 'Junior')