import cmath

# Menu da calculadora
print("Selecione a operação.")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")
print("5.Modulo")
print("6.Argumento")

# Recebendo entrada do usuário
escolha = input("Digite a sua escolha (1/2/3/4/5/6): ")

# Verificando a escolha do usuário
if escolha in ('1', '2', '3', '4'):
    # Recebendo os números complexos do usuário
    num1 = complex(input("Digite o primeiro número complexo: "))
    num2 = complex(input("Digite o segundo número complexo: "))

    # Condições para operações matemáticas
    if escolha == '1':
        resultado = num1 + num2
        print("Resultado: ", resultado)

    elif escolha == '2':
        resultado = num1 - num2
        print("Resultado: ", resultado)

    elif escolha == '3':
        resultado = num1 * num2
        print("Resultado: ", resultado)

    elif escolha == '4':
        resultado = num1 / num2
        print("Resultado: ", resultado)

elif escolha in ('5', '6'):
    # Recebendo o número complexo do usuário
    num = complex(input("Digite o número complexo: "))

    # Condições para operações matemáticas
    if escolha == '5':
        resultado = abs(num)
        print("Resultado: ", resultado)

    elif escolha == '6':
        resultado = cmath.phase(num)
        print("Resultado: ", resultado)

else:
    print("Opção inválida")
