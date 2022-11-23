#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-04-street-figther
#######################################################################
def KenVitory(RyuG, KenG): #criando função para quando a vitória for do KEN
    print("LUTADOR VENCEDOR: KEN")  #nome do vencedor
    print(f"GOLPES RYU = {RyuG}") #qntd de golpes do ryu
    print(f"GOLPES KEN = {KenG}") #qntd de golpes do ken

def RyuVitory(RyuG, KenG): #criando função para quando a vitória for do Ryu
    print("LUTADOR VENCEDOR: RYU") #nome do vencedor
    print(f"GOLPES RYU = {RyuG}") #qntd de golpes do ryu
    print(f"GOLPES KEN = {KenG}") #qntd de golpes do ken

def SubtraiXdeY(y, x): #criando função para subtrair um valor x de outro y
    if x<0: #porém, se x for menor que 0, eu quero que ele se torne positivo antes dessa subtração
        x *= -1
    y -= x
    return y #depois de tudo, retorno o valor de y

def VerifyLifeNeg(HP_X): #criando uma função especifica para o código, que verifica se o parametro é menor que zero
    if HP_X<0:
        return True #retornado TRUE caso seja negativo
    elif HP_X>=0:
        return False #e FALSE caso seja positivo

def PrintHPS(RyuLife, KenLife): #outra função especifica focada somente em printar o HP dos lutadores
    print(f"HP RYU = {RyuLife}")
    print(f"HP KEN = {KenLife}")

def Incremento(x): #função genérica construida para incrementar em 1 o parametro fornecido e depois retornar ele
    x += 1
    return x

def main(): #criando função principal
    #informando quantidade inicial de golpes
    GOLPES_RYU = 0 
    GOLPES_KEN = 0 
    #input do hp do lutador 
    HP_RYU = int(input()) 
    HP_KEN = int(input())

    while (HP_RYU>0 and HP_KEN>0): #criando laço de acordo com o hp dos lutadores
        VALOR_ATAQUE = int(input()) #input do valor de ataque (repete até a condição do while ser aceita)
        if VALOR_ATAQUE>0:
    #nesse IF, caso o ataque tenha valor maior que 0, o ryu atacará, realizando um print da na tela
            print(f"RYU APLICOU UM GOLPE: {VALOR_ATAQUE}")
    #chamo a função e o retorno dela vai ser atribuido a vida do KEN
            HP_KEN = SubtraiXdeY(HP_KEN, VALOR_ATAQUE)
    #chamo a função que retornará TRUE caso o hp seja negativo e depois atribuo 0 ao hp do ken, outrem, nada acontece
            if VerifyLifeNeg(HP_KEN):
                HP_KEN=0
    #chamo a função que irá printar o hp dos lutadores
            PrintHPS(HP_RYU, HP_KEN)
    #chamo a função que irá incrementar o valor dos golpes de ryu e já atribuir à variavel golpes
            GOLPES_RYU = Incremento(GOLPES_RYU)
        
        elif VALOR_ATAQUE<0:
    #nesse ELIF, caso o ataque tenha valor menor que 0, o ken atacará, realizando um print da na tela
            print(f"KEN APLICOU UM GOLPE: {(VALOR_ATAQUE*-1)}")
    #chamo a função e o retorno dela vai ser atribuido a vida do RYU
            HP_RYU = SubtraiXdeY(HP_RYU, VALOR_ATAQUE)
    #chamo a função que retornará TRUE caso o hp seja negativo e depois atribuo 0 ao hp do ryu, outrem, nada acontece
            if VerifyLifeNeg(HP_RYU):
                HP_RYU=0
    #chamo a função que irá printar o hp dos lutadores
            PrintHPS(HP_RYU, HP_KEN)
    #chamo a função que irá incrementar o valor dos golpes de ryu e já atribuir à variavel golpes
            GOLPES_KEN = Incremento(GOLPES_KEN)
    else: #quando a condição do while não for mais válida, ele verificará qual foi o ganhador e 
          #chamará a função da vitória de acordo com o lutador correspondente
        if HP_RYU==0:
            KenVitory(GOLPES_RYU, GOLPES_KEN)
        elif HP_KEN==0:
            RyuVitory(GOLPES_RYU, GOLPES_KEN)
################################################
main()
