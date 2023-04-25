numeros = [0,1,2,3,4,5,6,7,8,9,]
tabuada = int(input("Digite um numero para tabuada: "))
for n in numeros:
    resultado = tabuada * numeros[n]
    print (tabuada, "multiplicado por ", numeros[n], " é igual a: ", resultado)