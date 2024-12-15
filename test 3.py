import random
#name = {'adam': 'aushev', 'amina': 'bokova', 'mus':11}

#print (name, 11 in name.values())

#a = [10,00]
#a.append(1)
#print(a)
#while len(a) < 10:
#	a = a.append(1)
#	print(a)
def boxes():
	# Заполнение коробок
	prison = {}
	count = 1

	while len(prison)  < 100:
	    randnum = random.randint(1,100)
	    if randnum not in prison.values():
	        prison[count] = randnum
	        count += 1
	    else:    
	        continue
	return prison
	
print(boxes)