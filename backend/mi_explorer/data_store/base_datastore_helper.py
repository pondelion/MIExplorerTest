from abc import ABCMeta, abstractmethod


class BaseDatastoreHelper(metaclass=ABCMeta):

    @abstractmethod
    def save(self, data):
        raise NotImplementedError
