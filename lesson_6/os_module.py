import os
import shutil


# os
# getcwd, chdir(./..),

# print(os.getcwd())  # pwd in linux
#
# os.chdir('./..')  # піти на рівень вище
# os.chdir('lesson_5')  # go to folder
# os.chdir(r'F:\AQA_classes_120124\lesson_3')  # raw
# os.chdir('F:\\AQA_classes_120124\\lesson_4')
#
# print(os.getcwd())


# listdir, mkdir, rmdir, makedirs
# список файлів
# print(os.listdir('./..'))
# print([f for f in os.listdir('./..') if f.endswith('.json')])

# print(os.listdir())
# os.mkdir('test_folder')
# print(os.listdir())
# os.rmdir('test_folder')
# print(os.listdir())

# os.makedirs(r'F:\AQA_classes_120124\lesson_2\test_folder\test_folder2')

# remove
# print(os.listdir())
# os.remove('111.txt')
# print(os.listdir())

# shutil remove tree
# os.makedirs(r'F:\AQA_classes_120124\lesson_2\test_folder\test_folder2')
# print(os.listdir(r'F:\AQA_classes_120124\lesson_2'))
#
# shutil.rmtree(r'F:\AQA_classes_120124\lesson_2\test_folder')
# print(os.listdir(r'F:\AQA_classes_120124\lesson_2'))


# print(type(os.environ))
#
# # print(os.environ.get("PROCESSOR_ARCHITECTURE"))
# os.environ['CUSTOM_VAR'] = 'ASD'
# print([k for k in os.environ])
# print(os.environ.get('CUSTOM_VAR'))
#
# url = os.environ.get('os.environ')
#
# envv = dict(os.environ)
# pass
# environ run by using cmd
# environ getenv


# system

# os.system('set ENV_VAR_V2=env_test_123')
# print([k for k in dict(os.environ) if k == 'ENV_VAR_V2'])
# print(os.system('set')) # але не проставило змінну чомусь
# os.system('sh bash_script.sh')

# os.system('dir')
# walk
#
# for dirpath, dirnames, filenames in os.walk('./..'):
#     # current_path = dirpath
#     # current_folder = dirnames
#     # current_files = filenames
#     # pass
#     for filename in filenames:
#         print(os.path.join(dirpath, filename), sep='\n', end='\n****************************\n')



# os.path
# join

# print(os.path.join(os.path.join(r"F:\AQA_classes_120124", 'lesson_6'), 'files.py'))



# isdir, isfile, exists

# print(os.path.isdir(r'F:\AQA_classes_120124\lesson_6'))
# print(os.path.isfile(r'F:\AQA_classes_120124\lesson_6'))
# print(os.path.isdir(r'F:\AQA_classes_120124\lesson_6\main.py'))
# print(os.path.isfile(r'F:\AQA_classes_120124\lesson_6\main.py'))
#
# print(os.path.exists(r'F:\AQA_classes_120124\lesson_6\main.py'))
# print(os.path.exists(r'F:\AQA_classes_120124\lesson_6\main1.py'))


# print(os.path.abspath('.'))
# print(os.path.dirname(os.path.abspath('.')))

# abspath
# dirname
