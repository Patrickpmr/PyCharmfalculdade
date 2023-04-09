def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x
def fatorial(num):
    """
    Calcula a Fatorial
    :param num: valor q vai ser calculado
    :return: resultado
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num+1, 1):
        fat = fat * i
    return fat

#programa principal
x = valida_int('digite um valor para calcular a fatorial:',0, 9999)
print('fatorial de {} = {}'.format(x,fatorial(x)))