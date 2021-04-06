import json
import gzip
import ast
import time


somabucket=[]
somaquick=[]
somaheap=[]

def swap(i, j,lista):                    
    lista[i], lista[j] = lista[j], lista[i] #Realiza as trocas de posições
    somaheap.append(1) # Calcula numero de trocas

def heapify(end,i,lista):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and lista[i][0] < lista[l][0]:   
        max = l   
    if r < end and lista[max][0] < lista[r][0]:   
        max = r   
    if max != i:   
        swap(i, max,lista)   
        heapify(end, max,lista)   

def heapsort(lista):     
    end = len(lista)   
    start = end // 2 - 1
    for i in range(start, -1, -1):   
        heapify(end, i,lista)   
    for i in range(end-1, 0, -1):   
        swap(i, 0,lista)   
        heapify(i, 0,lista)
    return(lista)


def quicksort(lista):
    somaquick.append(1)   #Calcula numero de trocas
    if len(lista) <= 1:
        return lista
    if(lista[0]<=lista[len(lista)//2]):      #Pega o elemento que tem 
                                             #valor mediano entre         
        if(lista[len(lista)//2]<=lista[-1]): #o primeiro elemento
            pivo=lista[len(lista)//2]        #lemento do meio
                                             #e o ultimo elemento
        else:                                #do array, e torna-o 
            pivo=lista[-1]                   # o pivo
    else:
        if(lista[0]<=lista[-1]):
            pivo=lista[0]
        else:
            pivo=lista[-1]
   
    return quicksort([i for i in lista if i < pivo]) + \
          [i for i in lista if i == pivo] + \
          quicksort([i for i in lista if i > pivo])



def insertionSort(b):#metodo usado para ordenar cada um dos Baldes
    soma=0
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        soma+=1
        b[j + 1] = up
    somabucket.append(soma)   #Calcular numero de trocas
    return b      

  
def bucketsort(lista): 
    arr = []
    maior=max(lista)
    divisor=(len(lista)//maior[0])**2
    if divisor==0:
        divisor=1
    slot_num =len(lista)//10 # Quantidade de baldes 
                  
    for i in range(slot_num): 
        arr.append([]) 
          
    
    for j in lista:# Passando os elementos para os baldes  
        index_b =int(j[0]**1/2)//divisor
        if index_b>=600:
            index_b=600
        arr[index_b].append(j) 
      
    
    for i in range(slot_num): # Ordenando os Baldes
        arr[i] = insertionSort(arr[i])
             
    
    k = 0
    for i in range(slot_num): #Junta os Baldes ja ordenados
        for j in range(len(arr[i])): 
            lista[k] = arr[i][j] 
            k += 1
    return lista


inicio = time.time()

limite=0
lista=[]
abrir_arquivo= open("dataset.json","r")

for l in abrir_arquivo:
    l=ast.literal_eval(l)
    for e in l:
        
        for adjetivo in l[e][1]:
            
            if(adjetivo!= ""):
                lista.append(adjetivo[0])
                
    limite+=1
    if(limite>=50000):
        break

l.clear()
fim = time.time()


print("TEMPO PARA RECUPERAR DADOS:",fim - inicio)

lista2=[]
lista3=[]

for i in range(0,len(lista)-1):
    if lista[i] not in lista2:
    
        lista2.append(lista[i])
        lista3.append([lista.count(lista[i]),lista[i]])

        


print("MODO:")
opcao=int(input())
if(opcao==1):
    print("===================================")
    inicioquicksort=time.time()
    quick=quicksortt(lista3)
    fimquicksort=time.time()
    print("TEMPO QUICKSORT:",fimquicksort-inicioquicksort)
    ranking=-1
    while(ranking!=-11):
        print(quick[ranking])
        ranking-=1
    print("TOTAL DE TROCAS:",sum(somaquick))
elif(opcao==2):
    print("===================================")
    inicioheapsort=time.time()
    heap=heapsort(lista3)
    fimheapsort=time.time()
    print("TEMPO HEAPSORT:",fimheapsort-inicioheapsort)
              
    ranking=-1
    while(ranking!=-11):
        print(heap[ranking])
        ranking-=1
    print("TOTAL DE TROCAS:",sum(somaheap))

elif(opcao==3):
    print("===================================")
    iniciobucketsort=time.time()
    bucket=bucketsort(lista3)
    fimbucketsort=time.time()
    print("TEMPO PARA BUCKETSORT:",fimbucketsort-iniciobucketsort)
    ranking=-1
    while(ranking!=-11):
        print(bucket[ranking])
        ranking-=1
    print("TOTAL DE TROCAS:",sum(somabucket))
        
else:
    print("===================================")
    iniciosort=time.time()
    lista3.sort()
    fimsort=time.time()
    print("TEMPO SORT PADRAO:",fimsort-iniciosort)
    ranking=-1
    while(ranking!=-11):
        print(lista3[ranking])
        ranking-=1
