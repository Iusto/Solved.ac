while True :
    try :
        i = int(input())
    except :
        break
    num = 1
    count = 1
    while True :
        if num % i != 0 :
            num = num * 10 + 1
            count += 1
        else :
            break
    print(count)