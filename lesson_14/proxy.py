# Proxy
# read-writer


class Reader:

    def __init__(self, file_path):
        self.__file_path = file_path
        self.data = None

    def read_file(self):
        with open(self.__file_path, 'r') as f:   # 'r' -  мод читання
            self.data = f.read()


class Writer:  # write realisation
    pass


class ProxyReaderWriter:

    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = Reader(file_path)
        self.data = None

    def read(self):
        """
        1) Не читати файл, а просто повертати значення ЯКЩО файл не було змінено
        :return: None
        """
        if self.data:
            return
        self.reader.read_file()
        self.data = self.reader.data

    def write(self, row):  # write realisation
        """
        2) Він повинен записувати інформацію в кінець файлу(не переписуе, а доповлюе, дивись mode = 'a')
        3) Якщо інформація на запис надсилаеться повторно, то не записувати другий раз поспіль одне і те саме
        Важливо. Для перевірки чи МИНУЛИЙ раз ми записували цю ж строку що і зараз в файл читати не треба
        :return: None
        """
        pass


proxy_rw = ProxyReaderWriter(file_path='tst_file.txt')

proxy_rw.read()
proxy_rw.read()
proxy_rw.read()

proxy_rw.write('asd')  # буде запис
proxy_rw.write('asd')  # не буде запису
proxy_rw.write('asd2')  # буде запис
proxy_rw.write('asd')  # буде запис


print(proxy_rw.data)























    # class Bank:
#
#     def __init__(self, balance, secret_token):
#         self.balance = balance
#         self._secret_token = secret_token
#
#     def bank_deposit(self, amount):
#         self.balance += amount
#
#
# class ProxyBank:
#
#     def __init__(self, bank_obj: Bank):
#         self.bank_obj = bank_obj
#         self.__secret_token = bank_obj._secret_token
#
#     @property
#     def secret_token(self):
#         return self.__secret_token
#
#     def proxy_deposit(self, amount):
#         if amount <= 0:
#             print('Wrong amount')
#             return
#         self.bank_obj.bank_deposit(amount)
#
#     def get_balance(self, secret_token):
#         if self.secret_token != secret_token:
#             print('Wrong_key')
#             return
#         return self.bank_obj.balance
#
#
#
# real_bank = Bank(100, 'asd')
# proxy_bank = ProxyBank(real_bank)
# proxy_bank.proxy_deposit(50)
# print(proxy_bank.get_balance('asd'))
# proxy_bank.proxy_deposit(0)
# print(proxy_bank.get_balance('asd1'))