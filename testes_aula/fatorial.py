
def fatorial(a):
    if a == 1:
        return 1
    while a>1:
        a -= 1
        return fatorial(a)*fatorial(a-1)
a = int(5)
print(fatorial(a))

print(f"davi {}")