#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-07-plataforma
#############################################################################################################
plataforma = [int(i) for i in input().split()]
i = int(input())

valores = []
valores.append(i)

while i>=1 and i<=len(plataforma):
    if i>0:
        valores.append(plataforma[i + plataforma[i]])
    elif i<0:
        valores.append(plataforma[i - plataforma[i] * -1])  
    else:
        if i<1:
            print("esquerda")
        elif i>len(plataforma):
            print("direita")
        else:
            print("loop")