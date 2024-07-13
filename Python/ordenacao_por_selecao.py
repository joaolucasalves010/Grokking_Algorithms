# Ordenação por seleção

def buscaMenor(arr):
  menor = arr[0]
  menor_indice = 0
  for i in range(1, len(arr)):
    if (arr[i] < menor):
      menor = arr[i]
      menor_indice = i
  return menor_indice

def ordenacaoPorSelecao(arr):
  novoArr = []
  for i in range(len(arr)):
    menor = buscaMenor(arr)
    novoArr.append(arr.pop(menor))
  return novoArr


teste_arr = [5, 2, 6, 3]
print(ordenacaoPorSelecao(teste_arr))