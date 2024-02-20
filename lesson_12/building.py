class Stage:

    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    # def __str__(self):
    #     return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'


class Building:
    def __init__(self, name):
        self.name = name
        self.__stages = dict()

    @property
    def stages(self):
        return self.__stages

    @stages.setter
    def stages(self, stage_name: str):
        floor_number = len(self.__stages) + 1
        self.__stages[floor_number] = Stage(name=stage_name, floor=floor_number)  # dct['key'] = 'value'

    def __len__(self):
        return len(self.__stages)

    def __add__(self, other):
        return list(self.__stages.values()) + list(other.stages.values())

    def __eq__(self, other):
        return len(self.stages) == len(other.stages)


    # def __getitem__(self, key):
    #     return self.__stages.get(key)
    #
    # def __setitem__(self, key, value):
    #     self.__stages[key] = value

    # print(house_in_center[1].name)
    #
    # house_in_center[5] = Stage(name='shops', floor=5)
    #
    # print(house_in_center[1].name)
    # print(house_in_center[5].name)



house_in_center = Building('CenterHouse')
house_in_center.stages = 'basement'

house_not_in_center = Building('NonCenterHouse')
house_not_in_center.stages = 'shops'

stages_list = house_in_center + house_not_in_center

print(house_in_center == house_not_in_center)
print(stages_list)

#
#

# class ContexManagerForFiles:
#
#     def __init__(self, file_path, open_mode):
#         self.file_path = file_path
#         self.open_mode = open_mode
#
#     def __enter__(self):
#         self.returns_file = open(self.file_path, self.open_mode)
#         return self.returns_file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Exit function')
#         self.returns_file.close()
#
#
#
# with ContexManagerForFiles('test.txt', 'w') as f:
#     f.write(';Some text')
#     raise AttributeError('Our error')
# context manager

# __enter__
# __exit__


class SequenceIter:

    # def __init__(self, seq):
    #     self.seq = seq
    #     self.index = 0

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     if self.index < len(self.seq):
    #         cur_item = self.seq[self.index]
    #         self.index += 1
    #         return cur_item
    #     else:
    #         raise StopIteration

    def __init__(self, max_num):
        self.max_num = max_num
        self.cur_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_number < self.max_num:
            return_value = self.cur_number
            self.cur_number += 1
            return return_value
        else:
            raise StopIteration


my_seq = SequenceIter(100000000)

seq_iter = iter(my_seq)
print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
# print(next(seq_iter))
#
# for k in my_seq:
#     print(k)

for k in SequenceIter(10000000000):
    print(k)

