
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

def dfs(grafo, inicial, objetivo, borda=None, visitado=None, parentes=None):
    if visitado == None:
        visitado = [inicial]

    if parentes == None:
        parentes = {}

    if borda == None:
        borda = [inicial]
    
    no = borda.pop()

    if no == objetivo:
        return parentes

    for vizinho in grafo[no]:
        if vizinho not in visitado:
            borda.append(vizinho)
            visitado.append(vizinho)
            parentes[vizinho] = no
            
            
    return dfs(grafo, inicial, objetivo, borda, visitado, parentes)

origem = 'Arad'
objetivo = 'Bucharest'
parentes = dfs(grafo, origem, objetivo)
caminho = [objetivo]
while origem != objetivo:
    caminho.insert(0, parentes[objetivo])
    objetivo = parentes[objetivo]

print("caminho: ", caminho)