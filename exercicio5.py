#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-04-street-figther
#######################################################################

#criando 2 funções de acordo com a vitoria de cada lutador, Ken ou Ryu.
def vitoria_ken(g_ryu, g_ken): 
    print("LUTADOR VENCEDOR: KEN")  #nome do vencedor
    print(f"GOLPES RYU = {g_ryu}") #qntd de golpes do ryu
    print(f"GOLPES KEN = {g_ken}") #qntd de golpes do ken
def vitoria_ryu(g_ryu, g_ken):
    print("LUTADOR VENCEDOR: RYU")
    print(f"GOLPES RYU = {g_ryu}") 
    print(f"GOLPES KEN = {g_ken}")

#criando função principal  
def main(): 
    #input do hp do lutador 
    HP_RYU = int(input()) 
    HP_KEN = int(input())
    #######################

    ########################################
    #informando quantidade inicial de golpes
    GOLPES_RYU = 0 
    GOLPES_KEN = 0
    ########################################
    
    while (HP_RYU>0 and HP_KEN>0): #criando laço de acordo com o hp dos lutadores
        VALOR_ATAQUE = int(input()) #input do valor de ataque (repete até a condição do while ser aceita)
        if VALOR_ATAQUE>0:
            #nesse IF, caso o ataque tenha valor maior que 0, o ryu atacará, realizando um print da na tela
            print(f"RYU APLICOU UM GOLPE: {(VALOR_ATAQUE*-1)}")
            #diminuindo a vida do ken a partir da subtração do valor absoluto do ataque
            HP_KEN -= (VALOR_ATAQUE*-1)
            #após isso já verifico se o hp vai ficar um valor negativo, alterando-o, caso sim, para 0.
            if HP_KEN<=0:
                HP_KEN=0
            #termino printando o valor do hp de ambos os jogadores e adicionando 1 ao número de golpes
            #realizados pelo ryu
            print(f"HP RYU = {HP_RYU}")
            print(f"HP KEN = {HP_KEN}")
            GOLPES_RYU += 1
        
        elif VALOR_ATAQUE<0:
            #nesse ELIF, caso o ataque tenha valor menor que 0, o ken atacará, realizando um print da na tela
            print(f"KEN APLICOU UM GOLPE: {(VALOR_ATAQUE*-1)}")
            #diminuindo a vida do ryu a partir da subtração do valor absoluto do ataque
            HP_RYU -= (VALOR_ATAQUE*-1)
            if HP_RYU<=0:
                HP_RYU=0
            #termino printando o valor do hp de ambos os jogadores e adicionando 1 ao número de golpes
            #realizados pelo ken
            print(f"HP RYU = {HP_RYU}")
            print(f"HP KEN = {HP_KEN}")
            GOLPES_KEN += 1
    else: #quando a condição do while for aceita, ele verificará quem foi o jogador que ganhou e
          #chamará a função da vitória de acordo com o lutador correspondente
        if HP_RYU==0:
            vitoria_ken(GOLPES_RYU, GOLPES_KEN)
        elif HP_KEN==0:
            vitoria_ryu(GOLPES_RYU, GOLPES_KEN)



#chamando função principal
main()
