def uppercase(str):
    for c in str:
        if ord(c) in range (97, 123):
            upper = chr(ord(c) - 32)
        else:
            upper = c
        print("{}".format(upper), end="")
    print(f"\n")