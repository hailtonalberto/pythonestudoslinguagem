produtos = ["tv","sofa","mesa","cama","guarda roupa","som","fogão"]
estoque = ["100","50","20","40","60","90","86","120"]
# e agora como que faço pra descobrir quantos de produtos sofa tem no estoque?

i = produtos.index("sofa")
quantidade_estoque = estoque[i]

print("quantidade que tem de sofa no estoque é de {}".format(quantidade_estoque))
#crie um programa para fazer uma consulta de estoque.

produtos = input("insira o nome em letras minusculas")
if produtos in produtos:
    i = produtos.index(produtos)
    quantidade_estoque = estoque[i]
    print("temos {} inidades de {} no estoque".format(quantidade_estoque,produtos))
else:
    print("NÃO existe no estoque!")
