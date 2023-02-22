class trash_can:
    def __init__(self):
        self.trash_space = []
        self.free_space = 10

        print('Trash free places: ', self.free_space)

    def put_some_objects(self, obj):
        if len(self.trash_space) < 10:
            self.trash_space.append(obj)
        else:
            print('Trash is full! Not enough space for your object!')

        self.free_space = 10 - len(self.trash_space)

        print('Trash free places: ', self.free_space)
        print(self.trash_space)

        return self.trash_space


trash = trash_can()


class some_bag:
    def __init__(self):
        self.bag_content = []
        self.bag_space = 7

        print('Bag free places: ', self.bag_space)

    def put_some_objects(self, obj):
        if len(self.bag_content) < 7:
            self.bag_content.append(obj)
        else:
            print('Bag is full! Not enough space for your object!')

        self.bag_space = 7 - len(self.bag_content)

        print('Bag free places: ', self.bag_space)
        print(self.bag_content)

        return self.bag_content

bag = some_bag()

class SomeClass:
    def __init__(self):
        some_param = 10
        something = 'actually something'

    def print_func(self):
        print('Its worked!')



some_obj = SomeClass()
bag.put_some_objects(some_obj)
bag.bag_content[0].print_func()