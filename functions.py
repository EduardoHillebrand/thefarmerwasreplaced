def rotacionar(matriz):
	if not matriz or not matriz[0]:
		return []

	altura = len(matriz)
	largura = len(matriz[0])

	nova = []
	y_linha = 0
	while y_linha < largura:
		linha = []
		x_coluna = 0
		while x_coluna < altura:
			linha.append(matriz[altura - 1 - x_coluna][y_linha])
			x_coluna += 1
		nova.append(linha)
		y_linha += 1

	return nova