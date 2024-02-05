#!/usr/bin/python3

class MyList(list):
    """Inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))

# Testing the class
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print("Original list:")
    print(my_list)
    print("Sorted list:")
    my_list.print_sorted()
    print("Original list after sorting:")
    print(my_list)
