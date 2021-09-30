import abc


class FbsBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make(self):
        pass
