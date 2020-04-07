# Função Velocidade Media
def v_media(distancia, tempo):
        
         velocidade = distancia/tempo
         print('Distancia: {}, tempo= {}'.format(distancia, tempo))
         print(velocidade)


v_media(100, 20)
v_media(150, 22)
v_media(200, 30)
v_media(50, 3)

# Função Soma
def soma(a, b):
         s = a +b
         print('Soma entre {} + {} = {} '.format(a, b, s))


num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
soma(num1, num2)

# Função Subtração
def subtracao(a, b):
         sub = a - b
         print('Subtração entre {} - {} = {} '.format(a, b, sub))


num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
subtracao(num1, num2)

# Função calculadora
def calc(a, b):
         mult = a * b
         print('Multiplicação entre {} * {} = {} '.format(a, b, mult))
         div = a/b
         print('Divisão entre {} / {} = {}'.format(a,b,div))


num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
calc(num1, num2)