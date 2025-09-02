while (True):
    n1, n2 = map(int, input().split())
    if n1 == 0 and n2 == 0:
        break
    else:
        soma = n1 + n2
        lista = list(str(soma)) 
        lista_sem_zeros = [d for d in lista if d != '0']
        transfor = "".join(lista_sem_zeros) 
    print(transfor)
