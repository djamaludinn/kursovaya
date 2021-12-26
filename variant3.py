print('Модель подсистемы управления процессами с вытесняющей многозадачностью')
print('prod. by DJAMAL')
desc_list = []
dell_list = []

def CreateProc(quant):
	description = {
		'id': len(desc_list),
		'quant': int(quant)
	}
	desc_list.append(description)
	

def Start():
	max_quant = 0
	for x in desc_list:
		if x['quant'] > max_quant:
			max_quant = x['quant']
	dell_list = []
	for x in range(1, int(max_quant)+1):
		print('_________________ИТЕРАЦИЯ №', x,'_________________')
		for y in desc_list:
			y['quant'] -= 1
			print('Выполнение процесса №', y['id'], '. Осталось итераций: ', y['quant'])
			if y['quant'] == 0:
				print('Процесс №', y['id'], ' завершен')
				dell_list.append(y)

		for q in dell_list:
			desc_list.remove(q)
			dell_list.remove(q)
		print('_______________________________________________')

while True:
	command = input('>>> ')

	if command == 'add':
		quant = input('Введите время выполнения: ')
		CreateProc(quant)

	if command == 'start':
		Start()

	if command == 'list':
		print('________________________________')
		for x in desc_list:
			print(x)

	if command == 'exit':
		break

	if command == 'help':
		print('add - добавление процессов')
		print('list - вывод списка процессов')
		print('start - запуск программы')
		print('help - вывод списка команд')