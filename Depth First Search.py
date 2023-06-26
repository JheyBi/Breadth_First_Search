
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


def busca_em_profundidade(grafo, origem, objetivo, visitado=None, parentes=None):
    if visitado == None:
        visitado = []

    if parentes == None:
        parentes = {}

    visitado.append(origem)
    borda = [origem]
    no = borda.pop()
    for vizinho in grafo[no]:
        if vizinho not in visitado:
            parentes[vizinho] = no
            if vizinho == objetivo:
                return parentes
            else:
                visitado.append(vizinho)
                borda.append(vizinho)

    return busca_em_profundidade(grafo, borda.pop(), objetivo, visitado, parentes)

origem = 'Arad'
objetivo = 'Bucharest'
parentes = busca_em_profundidade(grafo, origem, objetivo)
caminho = [objetivo]
while origem != objetivo:
    caminho.insert(0, parentes[objetivo])
    objetivo = parentes[objetivo]

print(caminho)


                


