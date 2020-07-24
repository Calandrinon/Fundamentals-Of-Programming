class MyList:
    def __init__(self, list=[]):
        self.__list = list

    def get_container(self):
        return self.__list

    def append(self, object):
        self.__list.append(object)

    def len(self):
        return len(self.__list)

    def __comparison_function_increasing(self, a, b):
        return a > b

    def sort(self, comparison_function=None):
        if comparison_function == None:
            comparison_function = self.__comparison_function_increasing

        array_length = len(self.__list)
        gap = array_length // 2

        while gap > 0:
            for index in range(gap, array_length):
                old_element = self.__list[index]

                current_index = index
                while  current_index >= gap and comparison_function(self.__list[current_index - gap], old_element):#self.__list[current_index - gap] > old_element:
                    self.__list[current_index] = self.__list[current_index - gap]
                    current_index -= gap

                self.__list[current_index] = old_element
            gap //= 2

    def filter(self, function):
        new_list = []
        for index in range(0, len(self.__list)):
            if not function(self.__list[index]):
                new_list.append(self.__list[index])

        self.__list[:] = new_list

    def __iter__(self):
        self.__position = 0
        return self

    def __next__(self):
        if self.__position == len(self.__list):
            raise StopIteration
        object = self.__list[self.__position]
        self.__position += 1
        return object

    def __setitem__(self, position, data):
        self.__list[position] = data

    def __getitem__(self, position):
        return self.__list[position]

    def __delitem__(self, position):
        del self.__list[position]
