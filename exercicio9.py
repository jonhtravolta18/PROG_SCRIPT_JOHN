#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-08-aventura-na-amazonia
#############################################################################################################
def PRINTAR(MAPA, QNTD_COLUNAS): #função parar printar a matriz de forma organizada, linha por linha
    for k in range(len(MAPA)):
        for l in range(len(MAPA[0])): 
            if l+1 == QNTD_COLUNAS: print(MAPA[k][l], end="") #Para não dar espaço quando estiver na ultima coluna
            else: print(MAPA[k][l], end=" ")
        print()         
def INICIO(): #função que pega tamanho do mapa... 
    TAMANHO = [int(i) for i in input().split()]
    MAPA = [["." for k in range(TAMANHO[1])] for j in range(TAMANHO[0])]
    POS_IN = [int(i) for i in input().split()] #...posicão inicial... 
    MAPA[POS_IN[0]][POS_IN[1]] = "+" #...deixa o mapa todo preenchido...
    QNTD_COLUNAS = TAMANHO[1] #...e pega a qntd de colunas
    return MAPA, POS_IN, QNTD_COLUNAS #depois retorna todos os valores importantes
def CHECK_IF_IN_RANGE(V_1, V_2, LIST): #função para checar se a linha/coluna (dps de serem atualizadas), existem.
    if V_1 in range(len(LIST)):
        if V_2 in range(len(LIST[0])): return True #se existerem, retorna True
def CONDICOES(parametro_1, MAPA, ALTURA_ATUAL, LARGURA_ATUAL) : #função principal utilizada na main
    if (parametro_1 == "N"): #vou verificar qual foi a direção digitada pelo usuário
        ALTURA_ATUAL -= 1 #vou atualizar a linha/coluna de acordo com a condição
        if CHECK_IF_IN_RANGE(ALTURA_ATUAL, LARGURA_ATUAL,MAPA): #já verifico se dps de atualizar, o indice existe
            #coloca "+" somente se não existe um "#" na posição
            if(MAPA[ALTURA_ATUAL][LARGURA_ATUAL]) != "#": MAPA[ALTURA_ATUAL][LARGURA_ATUAL] = "+" 
    elif (parametro_1 == "S"): #se for pro sul
        ALTURA_ATUAL += 1
        if (CHECK_IF_IN_RANGE(ALTURA_ATUAL, LARGURA_ATUAL,MAPA)):
            if(MAPA[ALTURA_ATUAL][LARGURA_ATUAL]) != "#": MAPA[ALTURA_ATUAL][LARGURA_ATUAL] = "+"
    elif parametro_1 == "L": #se for pro leste
        LARGURA_ATUAL += 1
        if (CHECK_IF_IN_RANGE(ALTURA_ATUAL, LARGURA_ATUAL,MAPA)):
            if(MAPA[ALTURA_ATUAL][LARGURA_ATUAL]) != "#": MAPA[ALTURA_ATUAL][LARGURA_ATUAL] = "+"
    elif parametro_1 == "O": #se for pro oeste
        LARGURA_ATUAL -= 1
        if (CHECK_IF_IN_RANGE(ALTURA_ATUAL, LARGURA_ATUAL,MAPA)):
            if (MAPA[ALTURA_ATUAL][LARGURA_ATUAL]) != "#": MAPA[ALTURA_ATUAL][LARGURA_ATUAL] = "+"
    return ALTURA_ATUAL, LARGURA_ATUAL, MAPA
def main():
    MAPA, POSICAO_INICIAL, COLUNAS = INICIO() #recebe os valores necessários da função "INICIO"
    ALTURA_ATUAL, LARGURA_ATUAL = POSICAO_INICIAL[0], POSICAO_INICIAL[1] #atribui o valor da posição inicial
    ENTRADA = [0] #cria uma lista com 0 na posição "0" somente para entrar dentro do while
    while (ENTRADA[0] != "F"): #enquanto o usuário não digitar "F".
        ENTRADA = [i for i in input().split()] #input vai rodar a cada laço
        if (len(ENTRADA)==1): #se só tiver um parâmetro...
            if (ENTRADA[0] == "F"): break #veja se é "F", se for encerre o laço.
            elif (ENTRADA[0] == "A"): MAPA[ALTURA_ATUAL][LARGURA_ATUAL] = "#" #ou se "encontrou uma árvore".
        elif (len(ENTRADA)==2): #caso exista 2 parâmetros               
            for KM in range(int(ENTRADA[1])): #vai rodar até percorrer a distancia digitada pelo usuário
                ALTURA_ATUAL, LARGURA_ATUAL, MAPA = CONDICOES(ENTRADA[0], MAPA, ALTURA_ATUAL, LARGURA_ATUAL)               
    PRINTAR(MAPA, COLUNAS) #printar a matriz organizada!
main()