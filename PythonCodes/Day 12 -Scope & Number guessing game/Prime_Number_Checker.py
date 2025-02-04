def is_prime(num):
    isitprime = False
    maradek = 0
    for n in range(num+1):
        print(n)
        if n == 0:
            pass
        else:
            if num % n == 0:
                maradek += 1
            print(f"szam: {n} maradek{num % n}") 
        
    if maradek == 2:
        isitprime = True
    print(isitprime)
    return isitprime

is_prime(7)
    