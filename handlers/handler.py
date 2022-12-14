import abc
from data_base.dbalchemy import DBManager
from markup.markup import Keyboards


class Handler(metaclass=abc.ABCMeta):

    def __int__(self, bot):
        self.bot = bot
        self.keyboards = Keyboards()
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
