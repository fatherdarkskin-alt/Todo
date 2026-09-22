
precode = input("What do you want your messsgae to be?") 

cypher = "abcdefghijklmnopqrstuvwxyz"



for c in precode:
	num = cypher.index(c) 
	i = num + 6
	if i > 25:
		i -=  25
	post_code = cypher[i] 
	print(post_code)

	# if precode[c] == cypher[n]:
	# 	cypher.index[+5]
	# 	if cypher.index[] > 25:
	# 		cypher[-25]

