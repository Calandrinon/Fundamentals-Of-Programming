import unittest
from mylist import *

class Tests(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testConstructor__ConstructorWithListAsParameter__ValidMylist(self):
        list_as_parameter = [1, 5, 22, 7, 18, 2, 9, 11, 92]
        mylist = MyList(list_as_parameter)
        self.assertEqual(mylist.get_container(), list_as_parameter)

    def testAppend__someObject__mylistWithSomeNewObject(self):
        mylist = MyList()
        mylist.append(5)
        self.assertEqual(mylist.get_container(), [5])

    def testLen__validMylist__lengthOfMylist(self):
        mylist = MyList([8, 4])
        self.assertEqual(mylist.len(), 2)

    def testIter__iterOfMylist__validObjectsReturnedByNext(self):
        mylist = MyList([8, 4])
        myiterator = iter(mylist)
        test_list = [next(myiterator), next(myiterator)]
        self.assertEqual(test_list, mylist.get_container())

    def testIter__iterOfMylist__stopIteratorException(self):
        mylist = MyList([2, 3])
        myiterator = iter(mylist)
        first_element = next(myiterator)
        second_element = next(myiterator)

        with self.assertRaises(StopIteration):
            third_element = next(myiterator)

    def testGetItem__Mylist__validItemReturned(self):
        mylist = MyList([2, 3, 9, 5, 2])
        self.assertEqual(mylist[2], 9)

    def testSetItem__Mylist__UpdatedItem(self):
        mylist = MyList([2, 3, 9, 5, 2])
        mylist[2] = 10
        self.assertEqual(mylist[2], 10)

    def testDelItem__MylistObject__UpdatedList(self):
        mylist = MyList([2])
        del mylist[0]
        self.assertEqual(0, mylist.len())

    def testShellSort__MylistObject__SortedList(self):
        mylist = MyList([9, 5, 2, 8, 3, 6, 4, 7, 0, 1])
        mylist.sort()
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], mylist.get_container())

    def testShellSort__MylistObjectAndIncreasingComparisonFunction__ListInAscendingOrder(self):

        def comparison_function_increasing(a, b):
            return a > b

        mylist = MyList([9, 5, 2, 8, 3, 6, 4, 7, 0, 1])
        mylist.sort(comparison_function_increasing)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], mylist.get_container())

    def testShellSort__MylistObjectAndDecreasingComparisonFunction__ListInDescendingOrder(self):

        def comparison_function_increasing(a, b):
            return a < b

        mylist = MyList([9, 5, 2, 8, 3, 6, 4, 7, 0, 1])
        mylist.sort(comparison_function_increasing)
        self.assertEqual([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], mylist.get_container())

    def testFilter__MyListObjectWithFilterFunction__FilteredList(self):
        def func(element):
            if element == 2:
                return True
            return False

        mylist = MyList([1, 5, 2, 4, 3, 2, 2, 2, 2, 2, 2, 2])
        mylist.filter(func)
        self.assertEqual([1, 5, 4, 3], mylist.get_container())
