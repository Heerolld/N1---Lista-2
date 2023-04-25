numeros = [1,2,3,4,5,6,7,8,9]
numero = int(input("Informe um numero que deseja conferir se esta na listas: "))
contagem = 0
for i in numeros:
    if i==numero:
        contagem = contagem + 1
if contagem > 0:
    print("O numero está ",contagem," vezes na lista" )
else:
    print("O numero nao esta na lista.")