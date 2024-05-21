my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    for e in my_list:
        if e == 'Monday':
            continue
        print (e)
    i += 1
