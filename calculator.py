import time

print('Calculadora Simples em Python: ')
time.sleep(1)
print('Tool by Dr Midnight')
time.sleep(2)
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
time.sleep(0.3)
print('Aguarde...')
time.sleep(2)
print(' ')
if operation == '1':
    print('O Resultado da Soma de {} mais {}'.format(pri, seg))
    print('= {}'.format(soma))

elif operation == '2':
    print('O Resultado da Subtração de {} menos {}'.format(pri, seg))
    print('= {}'.format(sub))

elif operation == '3':
    print('O Resultado da Multiplicação de {} e {}'.format(pri, seg))
    print('= {}'.format(multi))

elif operation == '4':
    print('O Resultado da Divisão de {} e {}'.format(pri, seg))
    print('= {}'.format(divi))

elif operation == '5':
    print('O Resultado da Potencição de {} elevado a {}'.format(pri, seg))
    print('= {}'.format(raiz))

else:
    print('Você não selecionou uma operação válida :(')
