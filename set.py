class ArraySet:
    def __init__(self):
        self.the_set = []

    def __iter__(self):
        return iter(self.the_set)
    
    def __str__(self):
        result = "{"
        for x in self.the_set:
            result += str(x) + ", "
        return result.rstrip(", ") + "}"

    def get_size(self):
        return len(self.the_set)

    def add(self, v):
        if not v in self.the_set:
            self.the_set.append(v)

    def discard(self, v):
        try:
            self.the_set.remove(v)
        except:
            return

    def contains(self, v) -> bool:
        return v in self.the_set

    def union(self, other):
        for value in other:
            if value not in self.the_set:
                self.the_set.append(value)

        return self.the_set

    def intersection(   self, other):
        new_set = []

        for value in other:
            if value in self.the_set:
                new_set.append(value)

        return new_set

    def difference(self, other):
        for value in other:
            if value in self.the_set:
                self.the_set.remove(value)

        return self.the_set


# groceries = ArraySet()
# groceries.add(4)
# groceries.add(7)
# groceries.add(3)
# groceries.add(9)

# food = ArraySet()
# food.add(4)
# food.add(28)
# food.add(7)
# food.add(19)

# groceries = groceries.union(food)
# print(groceries)

def name_driver():
    """
        Description of Function:
            reads two files of names and outputs the number of similiar names among the two files
            and a set of the similiar names
        Parameters:
            None
        Return:
            None
    """
    #creating ArraySet Objects
    female_names = ArraySet()
    male_names = ArraySet()

    #reading files and appending names
    with open("Data_Struct/notes/femaleNames2016.txt", "r") as a_file:
        for line in a_file:
            data = line.strip().split(' ')

            name = data[0]

            female_names.add(name)

    with open("Data_Struct/notes/maleNames2016.txt", "r") as a_file:
        for line in a_file:
            data = line.strip().split(' ')

            name = data[0]

            male_names.add(name)

    #creating a new set of similiar names
    baby_names = female_names.intersection(male_names)

    #outputting the number of similiar names and the set
    print(len(baby_names))
    print(baby_names)

name_driver()
