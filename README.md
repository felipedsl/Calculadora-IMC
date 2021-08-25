# Calculadora IMC

## About project:
This project receives 3 inputs from the user, calling isolated methods to answer the user regarding health based on height, weight and age.

## Methods Explained

- eh_idoso(string): Receives string input from the user returning True if user is of elder age or False if not. Also checks if an invalid input is given, printing an error message.
```python
def eh_idoso(idoso):# Função para definir se usuário é idoso ou não
    if idoso == "s":
        return True
    elif idoso == "n":
        return False
    else:
        print("Resposta inválida")
        pass
```

- calcular_imc(float, int): This method receives height and weight from the user and returns a simple BMI calculation. 
```python
def calcular_imc(A, P):# Função para calcular o IMC
    return P/(A**2)
```
- obter_risco(boolean, float): This method receives the results from previous 2 methods and uses conditionals to return if the user is at risk based on user's height, weight and age.
```python
def obter_risco(r_eh_idoso, r_calcular_imc):# Função que avalia o IMC levando em consideração se o usuário é idoso ou não.
    if r_eh_idoso is False and 17 < r_calcular_imc < 25:
        return True
    elif r_eh_idoso is True and 22 < r_calcular_imc < 26.9:
        return True
    else:
        return False
```
-----
# Thank you for reading!
