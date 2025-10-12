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
	
	
def CheckExpand():
	cost = get_cost(Unlocks.Expand)
	for item in cost:
		custo = cost[item]
	total = num_items(list(cost)[0])
	
	if total > custo * 1.3:
		print("!")
		unlock(Unlocks.Expand)

def GetLabel(str):
	if str == "C" :
		return "Carrot"
	elif str == "B" :
		return "Bush"
	elif str == "T" :
		return "Wood" 
	elif str == "P" :
		return "Pumpkin"
	elif str == "S" :
		return "Sunflower"
	elif str == "K" :
		return "Cactus"
	elif str == "O" :
		return "Optimized"
	elif str == "Z" :
		return "Love"
	else:
		return "Hay"