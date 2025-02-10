from abc import ABC, abstractmethod

class Logger(ABC):

    @abstractmethod
    def write(self, data):
        pass

class FileLogger(Logger):

    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, 'a') as f:
            f.write(data + '\n')

class ConsoleLogger(Logger):

    def write(self, data):
        print(data)


def say_hello(l: Logger):
    l.write('Hello form KeyLogger')


is_debug = False

log: Logger

if is_debug:
    log = ConsoleLogger()
else:
    log = FileLogger('keylogger.log')

say_hello(log)
