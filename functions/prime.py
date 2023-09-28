def prime(num):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    return "prime number" if is_prime==True else "not prime"
print(prime(7))