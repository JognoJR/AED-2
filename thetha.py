#DUPLA:
#LUCAS DOS ANJOS
#JOGNO VEZU JUNIOR

#VERSAO PYTHON 3.7


#OPCOES:
#1-QUICKSORT
#2-HEAPSORT
#3-BUCKETSORT
#4-PADRAO PYTHON


import ast
from Item import Lista_DL#classe que representa uma lista duplamente licada de aspectos e valores

import json
import gzip
import time
somabucket=[]#Listas para salvar quantidade de trocas de cada método.
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

quantidades = open('quantidades.think','r')

c = quantidades.readline()

quantidades.close()

c = ast.literal_eval(c)#agora 'c' eh um dicionario
lista = []
for k in c:#iteracao do dicionario pelas chaves
    lista.append([c[k],k])


#IMPLEMENTAR AS FUNCOES AOO QUICK HEAP E BUCKET
RUN = 32 
    
# This function sorts array from left index to  
# to right index which is of size atmost RUN  
def insertionSort(arr, left, right):  
   
    for i in range(left + 1, right+1):  
       
        temp = arr[i]  
        j = i - 1 
        while arr[j] > temp and j >= left:  
           
            arr[j+1] = arr[j]  
            j -= 1
           
        arr[j+1] = temp  
    
# merge function merges the sorted runs  
def merge(arr, l, m, r): 
   
    # original array is broken in two parts  
    # left and right array  
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
    
    i, j, k = 0, 0, l 
    # after comparing, we merge those two array  
    # in larger sub array  
    while i < len1 and j < len2:  
       
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
           
        else: 
            arr[k] = right[j]  
            j += 1 
           
        k += 1
       
    # copy remaining elements of left, if any  
    while i < len1:  
       
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    # copy remaining element of right, if any  
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1
      
# iterative Timsort function to sort the  
# array[0...n-1] (similar to merge sort)  
def timSort(arr, n):  
   
    # Sort individual subarrays of size RUN  
    for i in range(0, n, RUN):  
        insertionSort(arr, i, min((i+31), (n-1)))  
    
    # start merging from size RUN (or 32). It will merge  
    # to form size 64, then 128, 256 and so on ....  
    size = RUN 
    while size < n:  
       
        # pick starting point of left sub array. We  
        # are going to merge arr[left..left+size-1]  
        # and arr[left+size, left+2*size-1]  
        # After every merge, we increase left by 2*size  
        for left in range(0, n, 2*size):  
           
            # find ending point of left sub array  
            # mid+1 is starting point of right sub array  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
    
            # merge sub array arr[left.....mid] &  
            # arr[mid+1....right]  
            merge(arr, left, mid, right)  
          
        size = 2*size 
           
# utility function to print the Array  
def printArray(arr, n):  
   
    for i in range(0, n):  
        print(arr[i], end = " ")  
    print()  
   
    
# Driver program to test above function  
if __name__ == "__main__": 
   
  
    n = len(lista)  
    print("Given Array is")  
    print(lista, n)  
    
    timSort(lista, n)  
    
    print("After Sorting Array is")  
    printArray(lista, n) 
