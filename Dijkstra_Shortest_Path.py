

#Define o grafo
grafo = {
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Dobreta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

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

#teste de Zerind a Sibiu
#print("O caminho mais curto é: ", busca_custo_uniforme(grafo, 'Zerind', 'Sibiu'))

#teste de Rimnicu Vilcea a Lugoj
#print("O caminho mais curto é: ", busca_custo_uniforme(grafo, 'Rimnicu Vilcea', 'Lugoj'))

#teste de Oradea a Sibiu
#print("O caminho mais curto é: ", busca_custo_uniforme(grafo, 'Oradea', 'Sibiu'))

#Usuário define a origem e o destino
origem = input("Digite a cidade de origem: ")
destino = input("Digite a cidade de destino: ")
print("O caminho mais curto é: ", busca_custo_uniforme(grafo, origem, destino))





            
            