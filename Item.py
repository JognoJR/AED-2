
#Aqui sao implementadas as classes No e Lista_DL. A classe No representa um no duplamente ligado de uma lista encadeada duplamente ligada. A classe Lista_DL representa a Lista encadeada duplamente ligada


class No:
    def __init__(self,valor = None,nome = None,anterior = None,proximo = None,index = 0):
        self.valor = valor
        self.nome = nome
        self.anterior = anterior
        self.proximo = proximo
        self.index = 0
        
#Lista duplamente ligada
class Lista_DL:
    def __init__(self):
        self.head = self.tail = None
        self.size = 0
        self.pin = None
    
    def get_size(self):
        return self.size

    def add(self, valor, nome):
        new_no = No(valor,nome,None,None)

        if self.head == None and self.tail == None :
            self.head = new_no
            self.tail = new_no
        else:
            ponteiro = self.tail
            
            ponteiro.proximo = new_no
            new_no.anterior = ponteiro
            
            self.tail = new_no
            self.tail.index = self.tail.anterior.index + 1

        self.size += 1
    
    def delete(self,index=None):
        if index is None:
            return self._delete(self.size-1)
        else:
            return self._delete(index)
    def _delete(self,index):
        if index < self.size:
            
            p = self.head
            for e in range(index):
                p = p.proximo
            if self.size < 2:
                self.head = self.tail = None
            elif index == 0:
                self.head = p.proximo
                p.proximo.anterior = p.anterior

            elif index == self.size-1:
                self.tail = p.anterior
                p.anterior.proximo = p.proximo
            
            else:
                p.proximo.anterior = p.anterior
                p.anterior.proximo = p.proximo

        else:
            print('ERROR: '+str(index)+' do not exist at the list!')
            return 0

        self.size -= 1
        return p.dados #retorna o dado do no

    def get_element(self,index):
        p = self.head
        
        for e in range(index):
            p = p.proximo
        return p.dados

    def is_empty(self):
        return self.head == None and self.tail == None
    

    # REFORMULACAO
    # def iterable_x(self,index=None):
    #     if index is None:
    #         return self._iterable_x(self.size-1)
    #     return self._iterable_x(index)
    # def _iterable_x(self,index):
    #     iterable = []
    #     p = self.head
        
    #     for e in range(index+1):
    #         iterable.append(p.dados)
    #         p = p.proximo

    #     return iterable

    # def iterable_y(self,l_index=None,r_index=None):
    #     if (l_index is not None) and (r_index is not None):
            
    #         return self._iterable_y(l_index,r_index)

    #     if l_index is None:
    #         l_index = 0
    #     if r_index is None:
    #         r_index = self.size


    #     return self._iterable_y(l_index,r_index)
    # def _iterable_y(self,l_index,r_index):
    #     iterable = Lista_DL()
    #     p = self.head

    #     for r in range(r_index): 
    #         if r >= l_index:
    #             iterable.add(p.dados)
    #         p = p.proximo

    #     return iterable

# lista = Lista_DL()
# lista.add(1)
# # lista.add(2)
# # lista.add(3)
# # lista.add(4)
# # lista.add(5)
# lista.delete(0)
# # print(lista.get_element(0))
# print(lista.iterable_x())
# # print(lista.iterable_y(0,None).iterable_x())
