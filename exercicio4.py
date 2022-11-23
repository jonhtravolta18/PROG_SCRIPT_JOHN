#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-03-bruto-liquido
#######################################################################

# ATRIBUINDO VALOR DO SALÁRIO BRUTO ATRAVÉS DO INPUT
salario_bruto = float(input())

# CRIANDO AS CONDIÇÕES DE ACORDO COM O VALOR DO SALÁRIO BRUTO
if salario_bruto <= 1045:
    taxa_inss = 0.075  # ESTABELECENDO VALOR DA TAXA DO INSS DE ACORDO COM A FAIXA SALARIAL
    # ESTABELECENDO VALOR DO DESCONTO DE INSS
    desconto_inss = float((taxa_inss)*(salario_bruto))
elif 1045.01 <= salario_bruto <= 2089.6:
    taxa_inss = 0.09
    desconto_inss = float((taxa_inss)*(salario_bruto))
elif 2089.61 <= salario_bruto <= 3134.4:
    taxa_inss = 0.12
    desconto_inss = float((taxa_inss)*(salario_bruto))
elif 3134.41 <= salario_bruto <= 6101.06:
    taxa_inss = 0.14
    desconto_inss = float((taxa_inss)*(salario_bruto))
elif salario_bruto > 6101.06:
    taxa_inss = 0.14
    desconto_inss = float((taxa_inss)*(6101.06))

# ESTABELECENDO VALOR DO SALÁRIO BRUTO - ABATIMENTO DO INSS
salario_menos_inss = float((salario_bruto)-(desconto_inss))

# CRIANDO AS CONDIÇÕES DE ACORDO COM O VALOR DO SALÁRIO APÓS ABATIMENTO DO INSS

if salario_menos_inss <= 1903.98:
    taxa_ir = 0  # ESTABELECENDO VALOR DA TAXA DO IR DE ACORDO COM A FAIXA SALARIAL PÓS ABATIMENTO DO INSS
    parcela_ir = 0  # ESTABELECENDO VALOR DA PARCELA DO IR
elif 1903.99 <= salario_menos_inss <= 2826.65:
    taxa_ir = 0.075
    parcela_ir = 142.8
elif 2826.66 <= salario_menos_inss <= 3751.05:
    taxa_ir = 0.15
    parcela_ir = 354.8
elif 3751.06 <= salario_menos_inss <= 4664.68:
    taxa_ir = 0.225
    parcela_ir = 636.13
elif salario_menos_inss > 4664.68:
    taxa_ir = 0.275
    parcela_ir = 869.36

# ESTABELECENDO VALOR DE DESCONTO DO IR
desconto_ir = float((salario_menos_inss*taxa_ir)-(parcela_ir))
# ESTABELECENDO VALOR DO SALÁRIO LIQUIDO
salario_liquido = float((salario_menos_inss)-(desconto_ir))

# PRINTANDO TODOS OS VALORES E REALIZANDO A TROCA DO "." PELO ","
print("Bruto: R$", format(salario_bruto, ".2f").replace(".", ","))
print("INSS: R$", format(desconto_inss, ".2f").replace(".", ","))
print("IR: R$", format(desconto_ir, ".2f").replace(".", ","))
print("Liquido: R$", format(salario_liquido, ".2f").replace(".", ","))

