A = float(input("Qual a sua altura em m? "))
P = int(input("Qual o seu peso em kg? "))
idoso = str.lower(input("Você é idoso? Responda s para sim e n para não: "))

def eh_idoso(idoso):# Função para definir se usuário é idoso ou não
    if idoso == "s":
        return True
    elif idoso == "n":
        return False
    else:
        print("Resposta inválida")
        pass

r_eh_idoso = eh_idoso(idoso)

def calcular_imc(A, P):# Função para calcular o IMC
    return P/(A**2)

r_calcular_imc = calcular_imc(A, P)

def obter_risco(r_eh_idoso, r_calcular_imc):# Função que avalia o IMC levando em consideração se o usuário é idoso ou não.
    if r_eh_idoso is False and 17 < r_calcular_imc < 25:
        return True
    elif r_eh_idoso is True and 22 < r_calcular_imc < 26.9:
        return True
    else:
        return False

r_obter_risco = obter_risco(r_eh_idoso, r_calcular_imc)

if r_obter_risco is False:
    print ("Existe risco")
elif r_obter_risco is True:
    print ("Tudo ok")
