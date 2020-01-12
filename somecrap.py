class Somelist:
	def __init__(self, list=[]):
		self.__list = list

	def __getitem__(self, index):
		return self.__list[index]

somelist = Somelist([8, 2])

print(somelist[0])
