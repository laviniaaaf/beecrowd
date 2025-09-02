casos_teste = int(input())

for _ in range(casos_teste):
    numero_pessoas = int(input())
    idiomas = []

    for _ in range(numero_pessoas):
        idioma = input().strip().lower()  
        idiomas.append(idioma)

    if all(i == idiomas[0] for i in idiomas):
        print(idiomas[0])
    else:
        print("ingles")
