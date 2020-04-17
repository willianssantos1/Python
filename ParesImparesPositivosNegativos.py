lista_num = []
i = 0
f = 0
for i in range (i, 5):
    new_element = int(input())
    lista_num.append(new_element)
    i = i + 1
 

cont1 = 0  
cont2 = 0
cont3 = 0
cont4 = 0 

for f in range (len(lista_num)):
    
    if(lista_num[f] > 0):
        cont1 = cont1 + 1
    if(lista_num[f] < 0):
        cont2 = cont2 + 1
    if(lista_num[f] %2 == 0):
        cont3 = cont3 + 1
    if(lista_num[f] %2 == 1):
        cont4 = cont4 + 1
    
        
        
print(cont3, "valor(es) par(es)")
print(cont4, "valor(es) ímpar(es)")       
print(cont1, "valor(es) positivo(s)")
print(cont2, "valor(es) negativo(s)")


    
    