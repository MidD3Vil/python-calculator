import time

print(' ')
print(' ')
print(' ')
print('Calculadora Simples em Python: ')
time.sleep(1)
print('Tool by Dr Midnight')
time.sleep(1.5)
print(' ')
print('01 - para Adição')
time.sleep(0.3)
print('02 - para Subtração')
time.sleep(0.3)
print('03 - para Multiplicação')
time.sleep(0.3)
print('04 - para Divisão')
time.sleep(0.3)
print('05 - para Potenciação')
time.sleep(0.3)
print('06 - para Porcentagem')
time.sleep(0.3)
print('07 - para Todos')
time.sleep(0.3)
print(' ')
operation = input('Escolha o Tipo de Cálculo: ')
time.sleep(1)
print(' ')
pri = float(input('Digite um número: '))
time.sleep(0.3)
seg = float(input('Digite outro número: '))

soma = pri + seg
sub = pri - seg
multi = pri * seg
divi = pri / seg
raiz = pri ** seg
s1 = seg / 100
s2 = s1 * pri
porcenA = pri + s2
porcenB = pri - s2
time.sleep(0.3)
print('Aguarde...')
time.sleep(2)
print(' ')
if operation == '1':
    print('------------------------------------------------\n')
    print('O Resultado da Soma de {} mais {}'.format(pri, seg))
    print('= {}\n'.format(soma))
    print('------------------------------------------------')

elif operation == '2':
    print('------------------------------------------------\n')
    print('O Resultado da Subtração de {} menos {}'.format(pri, seg))
    print('= {}\n'.format(sub))
    print('------------------------------------------------')

elif operation == '3':
    print('------------------------------------------------\n')
    print('O Resultado da Multiplicação de {} vezes {}'.format(pri, seg))
    print('= {}\n'.format(multi))
    print('------------------------------------------------')

elif operation == '4':
    print('------------------------------------------------\n')
    print('O Resultado da Divisão de {} dividido por {}'.format(pri, seg))
    print('= {}\n'.format(divi))
    print('------------------------------------------------')

elif operation == '5':
    print('------------------------------------------------\n')
    print('O Resultado da Potencição de {} elevado a {}'.format(pri, seg))
    print('= {}\n'.format(raiz))
    print('------------------------------------------------')

elif operation == '6':
    print('------------------------------------------------\n')
    print('O Valor do produto com o acrescimo de {}%'.format(seg))
    print('= {}'.format(porcenA))
    print('O valor do produto com o desconto de {}%'.format(seg))
    print('= {}\n'.format(porcenB))
    print('------------------------------------------------')

elif operation == '7':
    print('------------------------------------------------\n')
    print('O Resultado da Soma de {} mais {}'.format(pri, seg))
    print('= {}\n'.format(soma))
    print('------------------------------------------------\n')
    print('O Resultado da Subtração de {} menos {}'.format(pri, seg))
    print('= {}\n'.format(sub))
    print('------------------------------------------------\n')
    print('O Resultado da Multiplicação de {} vezes {}'.format(pri, seg))
    print('= {}\n'.format(multi))
    print('------------------------------------------------\n')
    print('O Resultado da Divisão de {} dividido por {}'.format(pri, seg))
    print('= {}\n'.format(divi))
    print('------------------------------------------------\n')
    print('O Resultado da Potenciação de {} elevado a {}'.format(pri, seg))
    print('= {}\n'.format(raiz))
    print('------------------------------------------------\n')
    print('O Valor do produto com o acrescimo de {}%'.format(seg))
    print('= {}'.format(porcenA))
    print('O valor do produto com o desconto de {}%'.format(seg))
    print('= {}\n'.format(porcenB))
    print('------------------------------------------------')
else:
    print('Você não selecionou uma operação válida :(')
