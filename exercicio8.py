#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-07-plataforma
#############################################################################################################
def ATRIB_VALORES():
    plataforma = [int(i) for i in input().split()]
    posicao_inicial = int(input())
    posicoes_anteriores = [posicao_inicial]
    posicao_atual = posicao_inicial - 1
    return plataforma, posicao_inicial, posicoes_anteriores, posicao_atual

def FINALIZACAO(POSICOES_ANT,POSICOES_PLAT):
    valores_print = []
    for p in POSICOES_ANT:
        if p not in valores_print and p>=0 and p<=len(POSICOES_PLAT):
            valores_print.append(p)
    for valor in valores_print:
        print(valor)
    
    if POSICOES_ANT[-1]<1:
        print("esquerda")
    elif POSICOES_ANT[-1]>len(POSICOES_PLAT):
        print("direita")
    else:
        print("loop")

def main():
    POSICOES_PLAT, POS_INICIAL, POSICOES_ANT, POS_ATUAL = ATRIB_VALORES()

    while 1<=POSICOES_ANT[-1]<=len(POSICOES_PLAT):  
        if (POS_ATUAL) + (POSICOES_PLAT[POS_ATUAL]) +1 in POSICOES_ANT:
            break
        else:
            POSICOES_ANT.append( (POS_ATUAL) + (POSICOES_PLAT[POS_ATUAL]) +1)
            POS_ATUAL = (POS_ATUAL) + (POSICOES_PLAT[POS_ATUAL])
       
    FINALIZACAO(POSICOES_ANT,POSICOES_PLAT)

main()