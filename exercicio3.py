#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-02-piso-escola
#######################################################################
def main():
    # ATRIBUO QUE O VALOR DAS VARIAVEIS VAI SER INSERIDO PELO USUARIO
    LARGURA, COMPRIMENTO = int(input()), int(input())
    # DEFINO A AREA TOTAL DA FIGURA
    AREA_TOTAL = COMPRIMENTO*LARGURA 
    # DETERMINO A QUANTIDADE DE LAJOTAS DO TIPO 2 DA SEGUINTE FORMA:
    # AS LAJOTAS DO TIPO 2 SÓ SE ENCONTRAM NAS LATERAIS E SÃO SEMPRE 1 A MENOS DO VALOR DO COMPRIMENTO E DA LARGURA
    # DEPOIS DETERMINO QUE A ÁREA TOTAL OCUPADA PELAS LAJOTAS DO TIPO 2 MULTIPLICANDO O TOTAL DE LAJOTAS PELO VALOR
    # INDIVIDUAL DE SUA ÁREA
    LAJES_2 = (COMPRIMENTO-1)*(2)+(LARGURA-1)*(2); AREA_TOTAL_LAJES_2 = (LAJES_2)*(1/4)
    # DETERMINO A QUANTIDADE DE LAJOTAS DO TIPO 3 E A AREA TOTAL QUE OCUPAM
    LAJES_3 = 4; AREA_TOTAL_LAJES_3 = 0.5
    # DETERMINO QUE A AREA RESTANTE É A SUBTRACAO DA AREA TOTAL PELAS AREAS TOTAIS DAS LAJOTAS 2 E 3
    AREA_RESTANTE = (AREA_TOTAL)-(AREA_TOTAL_LAJES_3)-(AREA_TOTAL_LAJES_2)
    # DEFINO QUE A QUANTIDADE DE LAJOTAS DO TIPO 1 VAI SER A AREA RESTANTE DIVIDIDA PELA AREA DE UMA LAJOTA DO TIPO 1
    LAJES_1 = int((AREA_RESTANTE)/(1/2))
    # PRINTO A QUANTIDADE DE LAJOTAS DO TIPO 1 E 2, RESPECTIVAMENTE
    print(LAJES_1); print(LAJES_2)
main()