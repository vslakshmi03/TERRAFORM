for x in range(1,101):
    if x % 15 == 0:
       print("helloworld")
       continue
    elif x % 3 == 0:
        print("hello")
        continue
    elif x % 5 == 0:
        print("world")
        continue

    print(x)
