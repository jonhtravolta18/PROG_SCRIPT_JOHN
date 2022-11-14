#######################################################################
# NOME = JOÃO ALEXANDRE A. DE SA
# MATRICULA = 12211EAU020
# TRABALHO = ps-05-super-sete
#######################################################################

def print_home(a, b, c, d):#função para printar valores e strings que não vão se alterar
	print(f"Primeira: {a}")
	print(f"Terceira: {b}")
	print(f"Quarta: {c}")
	print(f"Sexta: {d}")
	print(f"Lista de apostas:")

def verify_condition(a): #função especifica para verificar se determinado valor da variavel é multiplo de 7 ou 13, retornando False caso seja multiplo de pelo menos um deles
    if a%7!=0 and a%13!=0:
    	return True
    else:
    	return False
    
def main():
    primeiro = int(input())
    terceiro = int(input())
    quarto = int(input())
    sexto = int(input())
    
    print_home(primeiro, terceiro, quarto, sexto)
#nesses laços, eu defini que ele começasse a modificar os valores da direita pra esquerda, testando todas as possibilidades e printando caso a condicão seja atendida. Quando os valores deles ficassem iguais ao valor seguinte, eles iriam pro while anterior, até ter testado todas as possibilidades. 
    i = 0
    while ((primeiro+i)<=terceiro):
        segundo = primeiro+i
        j = 0
        while ((quarto+j)<=sexto):
            quinto = quarto+j
            k = 0
            while ((sexto+k)<=9):
                setimo = sexto+k
                k+=1
                soma = primeiro+segundo+terceiro+quarto+quinto+sexto+setimo
                if (verify_condition(soma)):
                    print(f"{primeiro} - {segundo} - {terceiro} - {quarto} - {quinto} - {sexto} - {setimo}") 
            j+=1
        i+=1

main()
