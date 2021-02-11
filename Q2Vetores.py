vetor = []
i = 0
sumPar = 0
sumImp = 0

while i < 7:

    vetor.append(int(input("Insira o numero na posição " + str(i) + " do vetor: ")))
    i += 1

print("\n\nO vetor ficou organizado da seguinte forma: " + str(vetor))

i = 0
while i < 7:
    if vetor[i] % 2 == 0:
        sumPar += vetor[i]
    else:
        sumImp += vetor[i]
    i += 1

print("\n\nSoma Par: " + str(sumPar) + "\nSoma Impar: " + str(sumImp))