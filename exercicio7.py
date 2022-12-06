#############################################################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-06-vacinacao
#############################################################################################################
#função focada na coleta das informações e criação da lista com a qntd de vacinas por mês
def COLETA_DADOS(): 
    qntd_vacinas = []
    n = int(input())
    for i in range(n):
        qntd_vacinas.append(int(input()))
    return qntd_vacinas, n
#função criada para calcular a soma total de vacinados com primeira e segunda dose, além das doses devolvidas
def ANALISE_DADOS(a, b, c, d):
    soma1, soma2, soma3 = 0, 0, 0
    for item in range(d):
        soma1 += a[item]
        soma2 += b[item]
        soma3 += c[item]
    return soma1, soma2, soma3
def main():
    qntd_vacinas, n = COLETA_DADOS()
    vacinados_1, vacinados_2, devolvidas = [], [], []

    for j in range(n):
        #caso a soma do mês atual com 4 seja maior que o tamanho da lista qntd_vacinas (para n dar erro de list index range)
        if j+4>len(qntd_vacinas):
            #acrescenta a qntd de primeiras doses do mês, q vai ser igual a qntd de vacinas  
            vacinados_1.append(qntd_vacinas[j])
            #acrescenta a qntd de doses devolvidas, q vai ser igual a zero 
            devolvidas.append(0)
            #if para a condição ser só a partir do 4° mÊs 
            if j>=3:
                #acrescenta a qntd de vacinados com segunda dose, q vai ser igual a qntd de vacinados com primeira dose de 3 meses atrás
                vacinados_2.append(vacinados_1[j-3])  
                #ele altera o valor de vacinados com primeira dose porque existem segundas doses
                vacinados_1[j] = qntd_vacinas[j]-vacinados_2[j] 
            #caso o mês ainda n seja pelo menos o quarto, não irão ter segundas doses
            else: vacinados_2.append(0)
        #caso exista pelo menos o 4° mês 
        else:
            #para ver se a qntd de vacinas disponiveis do mês atual é maior que a qntd de 3 meses depois 
            if qntd_vacinas[j] > qntd_vacinas[j+3]:
                #vacinados com primeira dose do mês vai ser igual a qntd de vacinas de 3 meses depois 
                vacinados_1.append(qntd_vacinas[j+3])
                #e a quantidade de doses devolvidas vai ser a qntd de vacinas do mês menos a quantidade de vacinas de 3 meses depois
                devolvidas.append(qntd_vacinas[j]-qntd_vacinas[j+3])
            # caso a qntd de vacinas do mês atual seja menor q de 3 meses depois
            else:
                #vacinados com primeira dose do mês vai ser igual a qntd de vacinas do msm mês
                vacinados_1.append(qntd_vacinas[j])
                #e a quantidade de doses devolvidas vai ser 0
                devolvidas.append(0)
            if j>=3:
                #a qntd de vacinados com segunda dose vai ser igual a qntd de vacinados com primeira dose de 3 meses atrás
                vacinados_2.append(vacinados_1[j-3]) 
                #e a quantidade de doses devolvidas do mês atual vai ser tornar a subtração da qntd de vacinas do mês pela qntd de 3 meses depois e 
                #da qntd de vacinados com segunda dose do mês
                devolvidas[j] = (qntd_vacinas[j]-qntd_vacinas[j+3]-vacinados_2[j])
                #caso o valor de devolvidas[j] fique negativo, é importante zerar o valor para não ocorrer calculo incorreto logo na linha 64
                if devolvidas[j]<0: devolvidas[j] = 0
                vacinados_1[j] = (qntd_vacinas[j]-vacinados_2[j]-devolvidas[j])
            else:
                vacinados_2.append(0)


        print(f"Mes {j+1}:\nVacinados com a primeira dose: {vacinados_1[j]}\nVacinados com a segunda dose: {vacinados_2[j]}\nVacinas devolvidas: {devolvidas[j]}")
    #chamo a função de analise de dados e atribuo as variaveis correspondentes
    soma_1_dose, soma_2_dose, soma_doses_devolvidas = ANALISE_DADOS(vacinados_1, vacinados_2, devolvidas, n)
    #defino que o valor de quem tomou apenas a primeira dose é a soma da primeira dose menos a soma da segunda
    apenas_primeira = (soma_1_dose-soma_2_dose)

    print(f"Total:\nVacinados apenas com a primeira dose: {apenas_primeira}\nVacinados com as duas doses: {soma_2_dose}\nVacinas devolvidas: {soma_doses_devolvidas}")
     
    
    
main()