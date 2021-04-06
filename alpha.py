#capturar o 'aspecto de cada linha do dataset e armazena-lo em um arquivo

#lembretes########################
#implentar o testador global     #
#implementar pre processamento   #
##################################

import ast

dataset = open('dataset.json','r')
data = open('aspectos.think','w')

print('Arquivo aberto;')
for linha in dataset:

    dicio = ast.literal_eval(linha)#Cada linha do arquivo eh um dicionario

    for e in dicio.values():#Iterar pelos valores do dicionario, que na verdade eh 1 ja que somente ha um valor. Vale ressaltar que 'e' EH UMA TUPLA QUE CONTEM UM TEXTO E POSSIVELMENTE UMA LISTA DE OPINIOES logo:

        if len(e[1]) > 0 and e[1] != ['']:#Se o seu tamanho eh maior que um, entao tem uma ou mais opinioes
            for tupla in e[1]:#'e[1]' eh a lista de tuplas opinioes e 'tupla' eh uma tupla da lista de tuplas

                aspecto = tupla[0]#o aspecto eh o primeiro item da tupla

                data.write(aspecto+'\n')

data.close()
dataset.close()
