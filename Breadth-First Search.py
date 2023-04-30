#Busca em extensão

#Define o grafo
grafo = {
    'Oradea': ['Zerind', 'Sibiu'],
    'Zerind': ['Oradea', 'Arad'],
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Sibiu': ['Oradea', 'Arad', 'Fagaras', 'Rimnicu Vilcea'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

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



print("Digite a cidade de origem: ")
origem = input()
print("Digite a cidade de destino: ")
destino = input()

if busca_em_extensão(grafo, origem, destino) == False:
    print("Caminho não encontrado!")
else:
    print("Caminho: ", busca_em_extensão(grafo, origem, destino))