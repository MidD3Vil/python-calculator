import time
import os

esc = '\033[m'
red = '\033[31m'
gre = '\033[32m'
yel = '\033[33m'
blu = '\033[36m'

os.system('cls')
restart = 'S'

while restart == 'S':
    print('Calculadora Simples em Python: ')
    time.sleep(1)
    print('Tool by Dr Midnight')
    time.sleep(1.5)
    print('\n01 - para Adição')
    time.sleep(0.3)
    print('02 - para Subtração')
    time.sleep(0.3)
    print('03 - para Multiplicação')
    time.sleep(0.3)
    print('04 - para Divisão')
    time.sleep(0.3)
    print('05 - para Potenciação')
    time.sleep(0.3)
    print('06 - para Raiz')
    time.sleep(0.3)
    print('07 - para Porcentagem')
    time.sleep(0.3)
    print('08 - para Todos')
    time.sleep(0.3)
    operation = input('\nEscolha o Tipo de Cálculo: ')
    time.sleep(1)
    pri = float(input('\nDigite um número: '))
    time.sleep(0.3)
    seg = float(input('Digite outro número: '))

    soma = pri + seg
    sub = pri - seg
    multi = pri * seg
    divi = pri / seg
    pote = pri ** seg
    raiz = pri ** 0.5
    s1 = seg / 100
    s2 = s1 * pri
    porcenA = pri + s2
    porcenB = pri - s2
    time.sleep(0.3)
    print('Aguarde...\n')
    time.sleep(2)

    def somax():
        print('------------------------------------------------\n')
        print('O Resultado da Soma de {} mais {}'.format(pri, seg))
        print('= {}\n'.format(soma))
        print('------------------------------------------------')

    def subx():
        print('------------------------------------------------\n')
        print('O Resultado da Subtração de {} menos {}'.format(pri, seg))
        print('= {}\n'.format(sub))
        print('------------------------------------------------')

    def multix():
        print('------------------------------------------------\n')
        print('O Resultado da Multiplicação de {} vezes {}'.format(pri, seg))
        print('= {}\n'.format(multi))
        print('------------------------------------------------')

    def divix():
        print('------------------------------------------------\n')
        print('O Resultado da Divisão de {} dividido por {}'.format(pri, seg))
        print('= {}\n'.format(divi))
        print('------------------------------------------------')

    def potex():
        print('------------------------------------------------\n')
        print('O Resultado da Potencição de {} elevado a {}'.format(pri, seg))
        print('= {}\n'.format(pote))
        print('------------------------------------------------')

    def raizx():
        print('------------------------------------------------\n')
        print('O Resultado da raiz {} de {}'.format(seg, pri))
        print('= {}\n'.format(raiz))
        print('------------------------------------------------')

    def porcenx():
        print('------------------------------------------------\n')
        print('O valor de {}% sobre {}'.format(seg, pri))
        print('= {}\n'.format(s2))
        print('O Valor do produto com o acrescimo de {}%'.format(seg))
        print('= {}'.format(porcenA))
        print('O valor do produto com o desconto de {}%'.format(seg))
        print('= {}\n'.format(porcenB))
        print('------------------------------------------------')

    def allx():
        print('------------------------------------------------')
        somax()
        subx()
        multix()
        divix()
        potex()
        raizx()
        porcenx()
        print('------------------------------------------------')


    if operation == '1':
        somax()
    elif operation == '2':
        subx()
    elif operation == '3':
        multix()
    elif operation == '4':
        divix()
    elif operation == '5':
        potex()
    elif operation == '6':
        raizx()
    elif operation == '7':
        porcenx()
    elif operation == '8':
        allx()
    else:
        print('Você não selecionou uma operação válida :(')
    restart = str(input('\nDeseja realizar outra conta? ')).strip().upper()[0]
    print('')
    os.system('cls')
