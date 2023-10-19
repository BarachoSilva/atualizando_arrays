lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
novos_produtos = ['rímel', 'cremes hidratantes',]
 
lista_produtos[1] = novos_produtos[0]
lista_produtos[4] = novos_produtos[1]
lista_produtos.pop()
lista_produtos.append('desodorantes')
lista_produtos.append('espuma de barbear')


for i in range (len(lista_produtos)):
  print("Temos", lista_produtos[i], "á venda")
