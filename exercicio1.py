#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = 00-warmup
#######################################################################
def main():
    # ESTOU DEFININDO QUE AS VARIÁVEIS "a" e "b", INDIVIDUALMENTE, RECEBERÃO
    # UM VALOR INTEIRO DIGITADO PELO USUÁRIO
    a, b = int(input()), int(input())
    # DEFINI QUE VARIÁVEL "soma" TERÁ COMO VALOR A SOMA MATEMÁTICA DO VALOR INTEIRO DE "a" + "b".
    soma = a+b
    # ESTAREI PRINTANDO O TEXTO "X = " CONCATENADO COM O VALOR DA VARIAVEL SOMA
    print(f"X = {soma}")

main()