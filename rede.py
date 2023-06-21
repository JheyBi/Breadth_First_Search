import networkx as nx
import random

grafo = {
    'No 0': {'No 28':  4, 'No 22':  10},
         'No 1': {}, 
         'No 2': {'No 24': {'jorge': 2}}, 
         'No 3': {'No 8': {'jorge': 6}, 'No 15': {'jorge': 1}}, 
         'No 4': {'No 18': {'jorge': 1}}, 
         'No 5': {}, 
         'No 6': {'No 25': {'jorge': 1}}, 
         'No 7': {}, 
         'No 8': {'No 3': {'jorge': 6}, 'No 14': {'jorge': 9}}, 
         'No 9': {}
         }

# Definindo a seed para que os resultados sejam sempre os mesmos
random.seed(1)

# Busca de custo uniforme
def busca_custo_uniforme(grafo, origem, objetivo):
    #Define a origem em borda
    borda = [origem]

    #Inicializa o vetor de explorado vazio
    explorado = []

    #Custo dos caminhos
    custo = {origem: 0}

    #Caminho
    caminho = {origem: [origem]}

    #Loop principal
    while borda:
       #Retiro o primeiro da borda
       #print(borda)
       no = borda.pop(0)
       #Se o no não for explorado
       if no not in explorado:
            #Se o no for o objetivo termina
            if no == objetivo:
               return caminho[no], custo[no]
            #Se ele não for o objetivo
            #Marca ele como explorado e expande
            explorado.append(no)

            #expandir
            for vizinho in grafo[no]:
                #Se o custo não estiver no dicionário ainda, ou
                #Se o custo precisar ser atualizado, pelo novo caminho ser menor
                if vizinho not in custo or custo[vizinho] > custo[no] + grafo[no][vizinho]:
                    #Atualiza o custo
                    custo[vizinho] = custo[no] + grafo[no][vizinho]
                    #Atualiza o caminho
                    caminho[vizinho] = caminho[no] + [vizinho]
                    #Adiciona o vizinho na borda
                    borda.append(vizinho)
                #Ordena a borda pelo custo
                borda = sorted(borda, key=lambda x: custo[x])
            
    #Se não encontrar o objetivo retorna falso
    return False


# Criando um grafo aleatorio com 30 nos com nome
G = nx.Graph()
for i in range(30):
    G.add_node("Equipamento "+str(i))


# Criando 70 arestas aleatorias
for i in range(70):
    G.add_edge("Equipamento "+str(random.randint(0,29)), "Equipamento "+str(random.randint(0,29)))

#Adicionando pesos as arestas
for i in G.edges():
    G[i[0]][i[1]]['weight'] = random.randint(1,10)
    

# OSPF custo = 1000000000/peso
# for i in G.edges.data('weight'):
#     G[i[0]][i[1]][i[2]] = round(1000000000/G[i[0]][i[1]]['weight'],2)


# Transformando o grafo em um dicionario
dic = nx.to_dict_of_dicts(G)

#Removendo a palavra weight
for i in dic:
    for j in dic[i]:
        dic[i][j] = dic[i][j]['weight']

# Busca de custo uniforme
caminho, custo = busca_custo_uniforme(dic, 'Equipamento 0', 'Equipamento 4')
print("Caminho: ", caminho)
print("Custo: ", custo)



