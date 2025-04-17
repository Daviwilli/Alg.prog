a = int(input())
par = False
PRIMO = False
quad_perf = False
div = []
def par_impar(a):
    if (a%2) == 0:
        return True
def divisores(a):
    for i in range(1,a+1):
        if a%i == 0:
            div.append(i)
def quadrado_perf(a):
    for i in range(a+1):
        if i**2 == a:
            return True
def Primo(a):
    if len(div) == 2:
        return True
def analise(a):
    if par_impar(a) == True:
        print("Esse número é par\n")
    else:
        print("Esse número é impar\n")
    if Primo(a) == True:
        print("Esse número é primo\n")
    if quadrado_perf(a) == True:
        print("Esse número é um quadrado perfeito\n")
    print(f"Seus divisores são:{div}")

par_impar(a)
Primo(a)
divisores(a) 
quadrado_perf(a) 
analise(a)


    
        
            

    

