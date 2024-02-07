def prime_composite(n):
    print("Number Given: {}" .format(n))
    for x in range(2,n//2+1):
        if n%x == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")

prime_composite(6)
prime_composite(131432432424)
