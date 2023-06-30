
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

def ldfs(grafo, origem, destino, limite,visitado=None, parentes=None, profundidade=0):
    if visitado == None:    
        visitado = [origem]
    if parentes == None:
        parentes = {}
    if profundidade == limite:
        return False

    for vizinho in grafo[origem]:
        if vizinho not in visitado:
            visitado.append(vizinho)
            parentes[vizinho] = origem
            if vizinho == destino:
                return parentes
            resultado = ldfs(grafo, vizinho, destino, limite, visitado, parentes, profundidade+1)
            if resultado != False:
                return resultado
            visitado.remove(vizinho)
    return False





origem = 'Neamt'
objetivo = 'Fagaras'
solucao = ldfs(grafo, origem, objetivo, 5)
caminho = [objetivo]
if solucao == False:
    print("Não achou!")
    exit()
while origem != objetivo:
    caminho.insert(0, solucao[objetivo])
    objetivo = solucao[objetivo]

print("caminho: ", caminho)