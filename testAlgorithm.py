def Recur(n):
    if n <= 5:
        return n
    else:
        s = 0
        for i in range(1,n-4):
            s += (n - i)*Recur(i)
        return s



def Dynam(n):
    mem = [0]
    for i in range(0,n):
        mem.append(0)
    for i in range(1,n+1):
        if i <= 5:
            mem[i] = i
        else:
            s = 0
            for j in range(1,i - 4):
                s += (i - j)*mem[j]
            mem[i] = s
    return mem[n]

print(Recur(60))
print(Dynam(60))
