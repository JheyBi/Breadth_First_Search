#(8 1 2 7 6 0 4 5 3)
#(a b c d e f g h i)



# A → B D
# B → A C E
# C → B F
# D → A E G
# E → B D F H
# F → C E I 
# G → D H
# H → G I E
# I → H F


import datetime
import itertools
import networkx as nx

grafo = nx.Graph()


def puzzle_grafo():
    # Gerar todas as permutações possíveis dos números de 0 a 8 sem repetição
    permutations = list(itertools.permutations(list(range(9)), 9))
    # Percorrer as permutações e atribuir os valores às variáveis
    for perm in permutations:
        a, b, c, d, e, f, g, h, i = perm
        # Verificar se não há números repetidos
        if len(set((a, b, c, d, e, f, g, h, i))) == 9:
            #movimentos de A
            if b == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (b, a, c, d, e, f, g, h, i))
            if d == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (d, b, c, a, e, f, g, h, i))
            #movimentos de B
            if a == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (b, a, c, d, e, f, g, h, i))
            if c == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, c, b, d, e, f, g, h, i))
            if e == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, e, c, d, b, f, g, h, i))
            #movimentos de C
            if b == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, c, b, d, e, f, g, h, i))
            if f == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,f,d,e,c,g,h,i))
            #movimentos de D
            if a == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (d, b, c, a, e, f, g, h, i))
            if e == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, e, d, f, g, h, i))
            if g == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, g, e, f, d, h, i))
            #movimentos de E
            if b == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, e, c, d, b, f, g, h, i))
            if d == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,e,d,f,g,h,i))
            if f == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,f,e,g,h,i))
            if h == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,h,f,g,e,i))
            #movimentos de F
            if c == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,f,d,e,c,g,h,i))
            if e == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,f,e,g,h,i))
            if i == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,i,g,h,f))
            #movimentos de G
            if d == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, g, e, f, d, h, i))
            if h == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, h, g, i))
            #movimentos de H
            if e == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, h, f, g, e, i))
            if g == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, h, g, i))
            if i == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a, b, c, d, e, f, g, i, h))
            #movimentos de I
            if f == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,i,g,h,f))
            if h == 0:
                grafo.add_edge((a,b,c,d,e,f,g,h,i), (a,b,c,d,e,f,g,i,h))
    return grafo


        
    
def busca_em_extensão(grafo, inicio, objetivo):
    #Define a fila de busca
    fila = [inicio]

    #Define os nós visitados
    visitados = [inicio]

    #Define o caminho a percorrer
    parentes = {}

    #Enquanto a fila não estiver vazia
    while fila:
        no = fila.pop(0)

        if no == objetivo:
            caminho = [objetivo]

            while objetivo != inicio:
                caminho.insert(0, parentes[objetivo])
                objetivo = parentes[objetivo]
            return caminho
        
        #Para cada vizinho do nó
        for vizinho in grafo[no]:
            if vizinho not in visitados:
                #Adiciona o nó como visitado
                visitados.append(vizinho)

                #Adiciona na fila
                fila.append(vizinho)

                #Adiciona o pai do vizinho sendo o nó
                parentes[vizinho] = no
            
    return False



def grafo_to_dict(grafo):
    return nx.to_dict_of_lists(grafo)
    
#Printa data e hora de início
print("Início do grafo: ", datetime.datetime.now())
puzzle_grafo()
#Printa data e hora de término
print("Término do grafo: ", datetime.datetime.now())

dic = grafo_to_dict(grafo)
#Busca em extensão
#(4, 5, 3, 2, 6, 0, 8, 1, 7)
origem = (8, 5, 4, 2, 7, 1, 3, 6, 0)
objetivo = (1,2,3,4,5,6,7,8,0)

#Printa data e hora de início
print("Início da busca: ", datetime.datetime.now())
if busca_em_extensão(dic, origem, objetivo) == False:
    print("Caminho não encontrado!")
else:
    print("Caminho: ", busca_em_extensão(dic, origem, objetivo))
#Printa data e hora de término
print("Término da busca: ", datetime.datetime.now())
