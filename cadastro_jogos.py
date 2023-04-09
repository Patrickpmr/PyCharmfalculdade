# Funão de validação de valores inteiro
def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

# Função para criar o arquivo
def criarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo.')
    else:
        print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

# Função para ver si arquivo existe
def existeArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

# Função para listar o arquivo
def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler Arquivo..')
    else:
        print(a.read())
    finally:
        a.close()

# Função para cadastrar Jogo
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir arquivo')
    else:
        a.write('{} ; {}\n'.format(nomeJogo, nomeVideogame))
    finally:
        a.close()

#programa principal
arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente...')
    criarArquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastro')
    print('3 - sair')

    op = valida_int('escolha a opção desejada', 1,3)
    if op == 1:
        print('Opção Cadastrar novo item selecionada...')
        nomeJogo=input('Nome do Jogo:')
        nomeVideogame=input('Nome do Video Game:')
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)

    elif op == 2:
        print('Opção Listar selecionada...\n')
        listarArquivo(arquivo)

    elif op == 3:
        print('Encerrando o programa...')
        break