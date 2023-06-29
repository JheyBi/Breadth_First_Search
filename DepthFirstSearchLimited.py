
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

def dfs_lim(grafo, origem, objetivo, limite, pilha=None, visitado=None, parentes=None, profundidade=0):
    
    if visitado == None:
        visitado = [origem]

    if parentes == None:
        parentes = {}

    if pilha == None:
        pilha = [(origem, profundidade)]

    # Se a pilha estiver vazia, não há solução
    if pilha == []:
        return "ERROR: borda vazia"
    
    # Se não tiver vazia, Remove o primeiro elemento da pilha
    no = pilha.pop()

    #no[0] = nome do no
    # Se o no for o objetivo, retorna a solução
    if no[0] == objetivo:
        return parentes
    
    #no[1] = profundidade
    # Se a profundidade for menor que o limite, expande o no
    if no[1] < limite:      
        for vizinho in grafo[no[0]]:
            if vizinho not in visitado:
                pilha.append((vizinho, no[1]+1))
                visitado.append(vizinho)
                parentes[vizinho] = no[0]
                    
        return dfs_lim(grafo, origem, objetivo, limite, pilha, visitado, parentes,  profundidade+1)
    
    # Se a profundidade for maior que o limite, remove o no da lista de visitados e continua a busca
    else:
        # Remove o no da lista de visitados
        visitado = list(filter(lambda x: x != no[0], visitado))
        return dfs_lim(grafo, origem,  objetivo, limite, pilha, visitado, parentes,  profundidade+1)


origem = 'Arad'
objetivo = 'Bucharest'
parentes = dfs_lim(grafo, origem, objetivo,3)
caminho = [objetivo]
if parentes == "ERROR: borda vazia":
    print("ERROR: borda vazia")
    exit()
while origem != objetivo:
    caminho.insert(0, parentes[objetivo])
    objetivo = parentes[objetivo]

print("Caminho:", caminho)