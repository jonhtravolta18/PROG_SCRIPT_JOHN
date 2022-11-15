#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-05-super-sete
#############################################################################################################
#####################- DEFININDO ALGUMAS FUNÇÕES AUXILIARES -################################################

def PRINT_HOME(A, B, C, D): #print das strings necessárias para o começo do programa.
	print(f"Primeira: {A}") 
	print(f"Terceira: {B}")
	print(f"Quarta: {C}")
	print(f"Sexta: {D}")
	print(f"Lista de apostas:")
#############################################################################################################
def VERIFY_CONDITION(A): #verifica se a variável A é multipla de 7 e/ou 13, retornando True apenas se não for.
    if (A%7!=0 and A%13!=0):
        return True
    else:
        return False
#############################################################################################################
def REQUEST_INPUT(): #retorna um input de valor inteiro.
    ENTRADA = int(input())
    return ENTRADA
#############################################################################################################
def INCREMENTO(A): #incrementa em 1 o valor da variavel A.
    A += 1
    return A
#####################- DEFININDO FUNÇÃO PRINCIPAL -##########################################################    
def main():
    #atribuo os valores digitados pelo usuário em sua variavel correspondente.
    PRIMEIRO = REQUEST_INPUT(); TERCEIRO = REQUEST_INPUT(); QUARTO = REQUEST_INPUT(); SEXTO = REQUEST_INPUT()
    #solicito a função para printar todas as strings do começo.
    PRINT_HOME(PRIMEIRO, TERCEIRO, QUARTO, SEXTO)
    #atribuo o valor inicial da variavel responsavel pelo incremento no primeiro laço.
    I = 0
    #ENQUANTO A SOMA DO "PRIMEIRO" COM O INCREMENTO "I" FOR MENOR QUE O "TERCEIRO".
    while ((PRIMEIRO+I) <= (TERCEIRO)): 
        SEGUNDO = (PRIMEIRO + I)
        J = 0
        #ENQUANTO A SOMA DO "QUARTO" COM O INCREMENTO "J" FOR MENOR QUE O "SEXTO".
        while ((QUARTO+J) <= (SEXTO)):
            QUINTO = (QUARTO + J)
            K = 0
            #ENQUANTO A SOMA DO "SEXTO" COM O INCREMENTO "K" FOR MENOR QUE "9".
            while ((SEXTO+K) <= (9)):
                SETIMO = (SEXTO + K)
                K = INCREMENTO(K)
                #CHAMA A FUNÇÃO QUE IRA VERIFICAR SE O RESULTADO DA SOMA ATENDE A CONDIÇÃO DO PROBLEMA.
                SOMA = (PRIMEIRO + SEGUNDO + TERCEIRO + QUARTO + QUINTO + SEXTO + SETIMO)
                if (VERIFY_CONDITION(SOMA)):
                    print(f"{PRIMEIRO} - {SEGUNDO} - {TERCEIRO} - {QUARTO} - {QUINTO} - {SEXTO} - {SETIMO}") 
            J = INCREMENTO(J)
        I = INCREMENTO(I)
#############################################################################################################
main()
