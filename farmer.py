import farmer_recipies

WS = get_world_size()
#print(WS)
plotList = farmer_recipies.PlotPlans['O']

SIZE = len(plotList)
LenPP = len(farmer_recipies.PlotTerms)
counter = -1
#set_farm_size(SIZE)

pet_the_piggy()
while get_pos_y() > 0:
	move(South)
while get_pos_x() > 0:
	move(West)

do_a_flip()

while True:
	
	y = get_pos_y()
	x = get_pos_x()
	
	if x == 0 and y == 0:
		counter +=1
		if counter >  LenPP-1 :
			counter = 0
		pt = farmer_recipies.PlotTerms[counter]
		plotList = farmer_recipies.PlotPlans[pt]
		print(counter,farmer_recipies.PlotTerms[counter])
	
	if can_harvest():
		harvest()
	

	if(x > SIZE or y > SIZE):
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Sunflower)
		
	elif plotList[x][y] == "C" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Carrot)

	elif plotList[x][y] == "B" :
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Bush)


	elif plotList[x][y] == "T" :
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Tree)


	elif plotList[x][y] == "P" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Pumpkin)


	elif plotList[x][y] == "S" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Sunflower)


	elif plotList[x][y] == "K" :
		if get_ground_type() == Grounds.Grassland:
			till()
		plant(Entities.Cactus)
	else:
		if get_ground_type() != Grounds.Grassland:
			till()

	
	if y < WS-1:
		move(North)
	else:
		move(North)
		move(East)


	
