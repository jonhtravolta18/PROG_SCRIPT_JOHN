#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-07-plataforma
#############################################################################################################

def main():
    pos_plat = [int(i) for i in input().split()]
    pos_inicial = int(input())
    pos_passadas = [pos_inicial]
    pos_atual  = pos_inicial-1

    while pos_passadas[-1]>=1 and pos_passadas[-1]<=len(pos_plat):  
        if pos_plat[pos_atual]<0:
            if (pos_atual) - (pos_plat[pos_atual] * -1) +1 in pos_passadas:
                break
            else:
                pos_passadas.append( (pos_atual) - (pos_plat[pos_atual] * -1) +1)
                pos_atual = (pos_atual) - (pos_plat[pos_atual] * -1)
        
        elif (pos_plat[pos_atual]>=0):
            if (pos_atual) + (pos_plat[pos_atual]) +1 in pos_passadas:
                break
            else:
                pos_passadas.append( (pos_atual) + (pos_plat[pos_atual]) +1)
                pos_atual = (pos_atual) + (pos_plat[pos_atual])

    valores_print = []
    for p in pos_passadas:
        if p not in valores_print and p>=0 and p<=len(pos_plat):
            valores_print.append(p)
    for valor in valores_print:
        print(valor)
    
    if pos_passadas[-1]<1:
        print("esquerda")
    elif pos_passadas[-1]>len(pos_plat):
        print("direita")
    else:
        print("loop")

main()