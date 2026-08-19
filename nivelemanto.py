
altura_m = []
altura_f = []
generof = 0
generom = 0
for i in range(15):
    genero = input("Diga Seu Genero M/F ")
    if genero.upper() == "F":
        generof = generof + 1
        altura = float(input("Diga Sua Altura:"))
        altura_f.append(altura)
    if genero.upper() == "M":
            generom = generom + 1
            altura = float(input("Diga Sua Altura:"))
            altura_m.append(altura)

alturas = altura_m + altura_f

print("Maior altura:", max(alturas))
print("Menor altura:", min(alturas))
print("Média Masculino:", sum(altura_m) / generom)
print("Número de mulheres:", generof)