#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-07-plataforma
#############################################################################################################
def ATRIB_VALORES():#função para input dos valores da plataforma; posição inicial; 
    plataforma = [int(i) for i in input().split()]; posicao_inicial = int(input())
    posicoes_anteriores = [posicao_inicial]; posicao_atual = posicao_inicial - 1 #lista para anotar as posiçoes passadas e atual
    return plataforma, posicao_inicial, posicoes_anteriores, posicao_atual #return de todos os valores
def FINALIZACAO(POSICOES_ANT,POSICOES_PLAT):          
    for valor in POSICOES_ANT: print(valor) #"for" feito para printar cada item dessa lista
    if POSICOES_ANT[-1]<1: print("esquerda") #caso personagem saia pela esquerda
    elif POSICOES_ANT[-1]>len(POSICOES_PLAT): print("direita") #caso personagem saia pela direita     
    else: print("loop") #ou caso entre em loop      
def main(): 
    POSICOES_PLAT, POS_INICIAL, POSICOES_ANT, POS_ATUAL = ATRIB_VALORES() #Retorno o valor para cada variavel adequada
    while 1<=POSICOES_ANT[-1]<=len(POSICOES_PLAT):  #enquanto o ultimo valor das posicoes passadas estiver dentro dos limites
        if (POS_ATUAL) + (POSICOES_PLAT[POS_ATUAL]) +1 in POSICOES_ANT: break #encerrar caso tente adicionar um valor repetido         
        else: #acrescentar na lista de variaveis passadas o valor da nova posição
            POSICOES_ANT.append( (POS_ATUAL) + (POSICOES_PLAT[POS_ATUAL]) +1)
            POS_ATUAL += (POSICOES_PLAT[POS_ATUAL])  #posição atual muda de valor
    FINALIZACAO(POSICOES_ANT,POSICOES_PLAT) #função é chamada, finalizando o programa caso saia do while
main()