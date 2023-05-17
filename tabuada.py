print('Bem-vindo ao programa: Tabuada agora!')
while True:
    n1 = int(input('Digite aqui o número da tabuada que deseja saber:'))
    print(f'A tabuada do {n1} é: ')
    print(f'\033[31m{n1}\033[m x 1 = \033[35m{n1 * 1}\033[m')
    print(f'\033[31m{n1}\033[m x 2 = \033[35m{n1 * 2}\033[m')
    print(f'\033[31m{n1}\033[m x 3 = \033[35m{n1 * 3}\033[m')
    print(f'\033[31m{n1}\033[m x 4 = \033[35m{n1 * 4}\033[m')
    print(f'\033[31m{n1}\033[m x 5 = \033[35m{n1 * 5}\033[m')
    print(f'\033[31m{n1}\033[m x 6 = \033[35m{n1 * 6}\033[m')
    print(f'\033[31m{n1}\033[m x 7 = \033[35m{n1 * 7}\033[m')
    print(f'\033[31m{n1}\033[m x 8 = \033[35m{n1 * 8}\033[m')
    print(f'\033[31m{n1}\033[m x 9 = \033[35m{n1 * 9}\033[m')
    print(f'\033[31m{n1}\033[m x 10 = \033[35m{n1 * 10}\033[m')
    print('Aprender com o Tabuada agora é muito mais fácil!')
    print('Até a próxima!')
    if n1 == 0:
        break
