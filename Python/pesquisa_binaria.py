def pesquisaBinaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


minhaLista = [1, 3, 5, 7, 9]

print(pesquisaBinaria(minhaLista, 3))  # => 1
print(pesquisaBinaria(minhaLista, -1))  # => none

"""
1 - Baixo e alto acompanham a parte da lista que você está procurando

2 - Enquanto ainda não conseguiu chegar a um unico elemento

3 - verifica o elemento central

4 - acha o item 

5 - o chute foi alto

6 - o chute foi baixo

7 - o item não existe 

8 - Vamos testá-lo

9 - Se as listas começam no 0 o proximo elemento tem indice de 1

10 - "None" significa nulo em Python. ele indica que o item não foi encontrado

"""
