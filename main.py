from time import sleep
import os

esc = '\033[m'
red = '\033[31m'
redp = '\033[1;31m'
gre = '\033[32m'
yel = '\033[33m'
blu = '\033[36m'
rox = '\033[35m'
roxp = '\033[1;35m'
invert = '\033[7m'

restart = 'S'
print('')

while restart == 'S':
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    print('{}-=-'.format(redp) * 10)
    sleep(.3)
    print('Calculadora Simples em Python: ')
    sleep(.3)
    print('    Tool by Dr Midnight')
    sleep(.3)
    print('-=-' * 10)
    sleep(.3)
    print('\n{}[ {}00 {}] {}Sair.'.format(rox, redp, rox, yel))
    sleep(.3)
    print('{}[ {}10 {}] {}Todos.'.format(rox, redp, rox, yel))
    sleep(.3)
    print('\n{}[ {}01 {}] {}Adição.'.format(rox,redp, rox, red))
    sleep(.3)
    print('{}[ {}02 {}] {}Subt.'.format(rox, redp, rox, red))
    sleep(.3)
    print('{}[ {}03 {}] {}Mult.'.format(rox, redp, rox, red))
    sleep(.3)
    print('{}[ {}04 {}] {}Divi.'.format(rox, redp, rox, red))
    sleep(.3)
    print('{}[ {}05 {}] {}Poten.'.format(rox, redp, rox, red))
    sleep(.3)
    print('{}[ {}06 {}] {}Raiz.'.format(rox, redp, rox, red))
    sleep(.3)
    print('{}[ {}07 {}] {}Porcen.{}'.format(rox, redp, rox, red, esc))
    sleep(.3)

    operation = input('\n{}Escolha uma forma de operação:{} '.format(invert, esc))
    sleep(.3)
    print('')
    print('{}={}'.format(roxp, esc) * 45)
    pri = float(input('{}Digite o primeiro número: '.format(red)))
    sleep(.3)
    seg = float(input('Digite o segundo número número:{} '.format(red)))

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
    sleep(.3)

    def somax():
        print('\n{}O Resultado da Soma de {}{} {}mais {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, soma))
        print('{}='.format(rox) * 45)
    def subx():
        print('\n{}O Resultado da Subtração de {}{} {}menos {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, sub))
        print('{}='.format(rox) * 45)

    def multix():
        print('\n{}O Resultado da Multiplicação de {}{} {}vezes {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, multi))
        print('{}='.format(rox) * 45)

    def divix():
        print('\n{}O Resultado da Divisão de {}{} {}dividido por {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, divi))
        print('{}='.format(rox) * 45)

    def potex():
        print('\n{}O Resultado da Potencição de {}{} {}elevado a {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, pote))
        print('{}='.format(rox) * 45)

    def raizx():
        print('\n{}O Resultado da raiz {}{} {}de {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, raiz))
        print('{}='.format(rox) * 45)

    def porcenx():
        print('\n{}O valor de {}{}% {}sobre {}{}{}'.format(redp, yel, pri, redp, yel, seg, esc))
        print('{}= {}{}\n'.format(redp, yel, s2))
        print('{}O Valor do produto com o acrescimo de {}{}%{}'.format(redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, porcenA))
        print('{}O valor do produto com o desconto de {}{}%{}'.format(redp, yel, seg, esc))
        print('{}= {}{}'.format(redp, yel, porcenB))
        print('{}='.format(rox) * 45)

    def allx():
        print('{}='.format(rox) * 45)
        somax()
        subx()
        multix()
        divix()
        potex()
        raizx()
        porcenx()

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
    elif operation == '10':
        allx()
    elif operation == '0':
        exit()
    else:
        print('Você não selecionou uma operação válida :(')
    restart = str(input('''\n{}{}Deseja realizar outra conta?{} 
Sim.
Não.
{}R: '''.format(esc, invert, esc, redp))).strip().upper()[0]

    while restart not in 'SN':
        sleep(.3)
        restart = str(input('''\n{}{}Digite um dado válido. Deseja realizar outra conta?{} 
Sim.
Não.
{}R: '''.format(esc, invert, esc, redp))).strip().upper()[0]
    print('')
