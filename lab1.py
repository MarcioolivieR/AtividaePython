''nome = input("nome: ")    #the fuction  'input' about return 
idade = int(input("idade: "))
print(f"Name: {nome}")
print(f"Old year: {idade} old")


estudar metodo e função!!!!

'''


'''
numeros = []
cont = 0
while cont < 3:
    numeros.append(int(input(f"Digite o {cont}º numero: ")))
    cont += 1
print(numeros)

soma = 0

i = 0      #conta quantos elemntos tem dentro de uma lista!
while i < len(numeros):
    soma += numeors[i]
    i += 1
print(f"A soma dos números é: {soma}")


'''
'''
soma = 0  #Range is (start, stop, step)
for cont in range (3):
    num = int(input(f"Digite o {cont}º numero: "))
    soma += num
print(f"A soma dos números é: {soma}")


'''
'''
a = "oi"
if a:
    print("1 -", a)

a = ""
if a:
    print("2 -", a)

a = 0
if not a:
    print("3 -", a)

b = []
if not b:
    print("4 - ", b)


c = False
if c:
    print("5 - ", c)

c = False
if c:
    print("6 - ", c)
'''
'''

a = 0
b = 5
if a or b < 10:
    print("verdade")
else:
    print("falso")

'''
'''

numeros = []                           #ACERTOOOUUUUUUUUUU
cont = 0
while True:
    numeros.append(float(int(input(f"Digite o {cont}º numero: "))))
    cont += 1
    if cont == 5:
        break
print(numeros)

nega = []
posi = []
i = 0
x = 0
for num in numeros:
    if num < 0:
        nega.append(num)
        i += 1
    else:
        posi.append(num)
        x = x + num
        
print(f"negativos: {i}")
print(f"soma dos positivos: {x}")
        

'''        
'''
numeros = []                        
cont = 0
while True:
    numeros.append(float(int(input(f"Digite o {cont}º numero: "))))
    cont += 1
    if cont == 5:
        break
print(numeros)


i = 0
qte_negativos = 0
soma_posit = 0
while True:
    if cont == len(numeros):
        break
    if numeros[cont] < 0:
        qte_negativos +=1
    else:
        soma_posit += numeros[cont]
    i += 1
print(f" A soma dos números positivos é: {soma_posit}")
print(f" A quantidade de negativos é: {qte_negativos}")
'''

'''
numeros = []                          
for i in range (5):
    numeros.append(float(int(input(f"Digite o {i + 1}º numero: "))))
    
print(numeros)


qte_negativos = 0
soma_posit = 0
for i in range (len(numeros)):
    if numeros[i] < 0:
        qte_negativos +=1
    else:
        soma_posit += numeros[i]
    i += 1
print(f" A soma dos números positivos é: {soma_posit}")
print(f" A quantidade de negativos é: {qte_negativos}")




'''

