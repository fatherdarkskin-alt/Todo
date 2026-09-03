import os
todo = []

done = []

while True: 
	task = input("what do you want to do:",)
	tasksimple = task.str.to_lowercase().str.replace_all(' ','',literal=True)
	if tasksimple == "exit":
		break
	elif task in todo:
		todo.remove(task)
		done.append(task)
	elif task in done:
		done.remove(task)
	else: 
		todo.append(task)
	os.system("clear")
	for task in todo:
		print("[]", task, )
	for task in done:
		print ("[X]", task, )
