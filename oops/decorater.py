def dec_fun(fn):
    def in_fun(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return in_fun


def dec_sq(fn):
    def in_sq(n1,n2):
        return fn(n1**2,n2**2)
    return in_sq

@dec_fun
def sub(n1,n2):
    return n1-n2


def div(n1,n2):
    return n1/n2


@dec_sq 
def prod(n1,n2):
    return(n1*n2)

print(prod(1,2))



print(sub(10,20))

