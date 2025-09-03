#O programa deve receber uma palavra ou frase digitada pelo usuário. 
#Em seguida, ele precisa percorrer cada caractere da string e verificar se esse caractere é uma 
# vogal (a, e, i, o, u), considerando tanto letras maiúsculas quanto minúsculas.
#Cada vez que encontrar uma vogal, o programa deve somar 1 em um contador. No final, deve mostrar quantas vogais foram encontradas.

frase = input("Digite uma palavra ou frase:")

frase = frase.lower()

contador = 0

consoantes = 0

for i in range(len(frase)):
    if frase[i] == 'a':
        contador+=1 
    else:
        if frase[i] == 'e':
            contador+=1
        if frase[i] == 'i':
            contador+=1
        if frase[i] == 'o':
            contador+=1
        if frase[i] == 'u':
            contador+=1
    if frase[i] in 'bcdfghjklmnpqrstvwxyz': #acrescentei a verificacoes de consoantes
        consoantes+=1


print(f"A frase tem {contador} vogais e {consoantes} consoantes.")
