from contextlib import contextmanager

# 1
@contextmanager
def connect_database(url):
    obj = open(url, 'r')
    try:
        print('enter the obj')
        yield obj
    finally:
        print('exit the obj')
        obj.close()

# 2
class Processer:
    def __init__(self, filename):
        self.file = filename

    def __enter__(self):
        try:
            print(f'initialize {self.file}')
            self.fileobj = open(self.file)
            return self.fileobj
        except FileNotFoundError as e:
            self.fileobj = None
            print('file not exists')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fileobj:
            self.fileobj.close()



# with open('./contextmanager.py') as file:
#     print(file.read())



# with Processer('./contextmanager.py') as file:
#     print(file.read())


# with connect_database('./contextmanager.py') as file:
#     print(file.read())