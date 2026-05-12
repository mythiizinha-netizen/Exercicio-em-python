#listas
lista = [15, 20, 40, 80, 18]

#soma dos elementos da lista
total_vendas = sum(lista)
print("o total de vendas dos mês foi: ", total_vendas)

#tamanho da lista
quantidade_vendas = len(lista)
print("a quantidade de vendedores foi: ", quantidade_vendas)

#max e min
maior_venda = max(lista)
print("o maior valor de venda da lista foi: ", maior_venda)
posição_min_venda = min(lista)
print("o menor valor de venda da lista foi: ", posição_min_venda)

#pegar posição na lista
posição_max_venda = lista.index(maior_venda)
print("o vendedor com a maior venda foi: ", posição_max_venda)
posição_min_venda = lista.index(posição_min_venda)
print("o vendedor com a menor venda foi: ", posição_min_venda)

lista_produtos = ("geladeira", "fogão", "máquina de lavar", "microondas", "liquidificador")
produto_procurado = input("por favor, digite o nome do produto que deseja procurar: ")
produto_procurado = produto_procurado.lower()  # Convertendo para minúsculas para facilitar a comparação

print(produto_procurado in lista_produtos)

