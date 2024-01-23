# set add(obj) update(iter) union(return new object)

# names_set = {'Alex', 'Joe'}
# print(names_set)
#
# new_set = names_set.union({1, 2, 'Alex'})
#
# print(new_set)

#
# names_set.add('Katia')
# print(names_set)
#
# names_set.update(['Alex1', 'Den'])
# print(names_set)
#
# names_set.update('Den')
# print(names_set)


# remove(with error) discard(without error)
# names_set = {'Alex', 'Joe'}

# print(names_set)
# names_set.remove('Alex1')
# print(names_set)
# names_set.discard('Joe1')
# print(names_set)
#
# if 'Alex' in names_set:
#     names_set.remove('Alex')


# intersection, symmetric_difference

# names_set = {'Alex', 'Joe'}
# names_set2 = ['Alex', 'Joe1']
#
# sset = names_set.intersection(names_set2)
#
# print(sset)

# print(names_set.difference(names_set2))
# print(names_set.symmetric_difference(names_set2))

# frozenset

# names_set = frozenset(('Alex', 'Joe'))
#
# print(names_set.union())



# dict [], get, різниця

# dict = {
#     key: value,
#     key: value,
#     ...
# }

# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }

# descr1, descr2 = positions.get('AQA1', 'Unknown position'), positions.get('AQA', 'Unknown position')
# print(descr1, descr2, sep='|  ||  |')

# update, []

# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }

# positions.update({'QA': 'test the app', 'mobile': 'crete your mobile app'})
# print(positions)
#
# positions['AQA'] = 'create your mobile app'
#
# print(positions)



# pop, pop item
# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }

# print(positions)

# a = positions.popitem()
# print(positions)
# positions.pop('AQA')
# print(positions)


# keys, values, items

# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }
#
# print(type(positions.keys()))
# print(positions.keys())
#
# print(list(positions.keys()))
# print(list(positions.values()))
# print(list(positions.items()))


# list append, +

# a = [1, 2]
# a.append(3)
#
# a = a + ['a', 'b']
# print(a)




