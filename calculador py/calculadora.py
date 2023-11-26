def soma(a,b):
    soma = a+b
    return soma
    
def subtracao(a,b):
    subtracao = a-b
    return subtracao

def divisao(a,b):
    divisao = a/b
    return divisao

def multiplicacao(a,b):
    multiplicacao = a*b
    return multiplicacao

opcao = 0;
vet = []
while(opcao!=5) :  
    a=int(input("digite o primeiro numero:" ))
    b=int(input("digite o segundo numero:"))
    r=int(0)
    print('digite 1 para soma')
    print('digite 2 para subtracao')
    print('digite 3 para divisao')
    print('digite 4 para multiplicacao')
    print('digite 5 para sair da calculadora')
    opcao=int(input("agora selecione uma opcao:"))

    if opcao == 1:
        r = soma(a,b)
    if opcao == 2:
        r = subtracao(a,b)
    if opcao == 3 :
        r = divisao(a,b)
    if opcao == 4:
        r = multiplicacao(a,b)
    if opcao == 5:
        print("O Codígo será finalizado")
    print('o resultado é:', r)

    vet.append(r)
print(vet)

