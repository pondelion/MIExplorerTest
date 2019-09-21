from abc import ABCMeta, abstractmethod


class BaseDatastoreHelper(metaclass=ABCMeta):

    @abstractmethod
    def save(self, data, path):
        raise NotImplementedError

    @abstractmethod
    def read(self, path):
        raise NotImplementedError
