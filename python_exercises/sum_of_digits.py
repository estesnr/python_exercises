def digit_add(num):
    sum = 0
    num = num.replace('', " ")
    new_num = num.split(' ')
    for x in new_num:
        if x == "":
            new_num.remove('')
    for y in new_num:
        sum += int(y)   
    print(sum)
    
digit_add(input("Select a number\n"))
