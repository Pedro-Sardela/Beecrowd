
import math

def calc(n1, n2, d1, d2, op):
    if op == '+':
        n = (n1*d2 + n2*d1)
        d = (d1*d2)
        return n, d
    elif op == '-':   
        n = (n1*d2 - n2*d1)
        d = (d1*d2)
        return n, d
    elif op == '*':
        n = (n1*n2)
        d = (d1*d2)
        return n, d
    else:
        n = (n1*d2)
        d = (n2*d1)
        return n, d

def simpl(n, d):
    mpc = math.gcd(n, d)
    return n // mpc, d // mpc

n = int(input())
for i in range(n):
    conta = input()
    partes = conta.split()
    n1 = int(partes[0])
    d1 = int(partes[2])
    n2 = int(partes[4])
    d2 = int(partes[6])
    op = partes[3]
    n, d = calc(n1, n2, d1, d2, op)
    ns, ds = simpl(n, d)
    print(f"{n}/{d} = {ns}/{ds}")