

class Logger:

    @staticmethod
    def d(tag: str, message: str):
        """debug log"""
        raise NotImplementedError

    @staticmethod
    def i(tag: str, message: str):
        """infomation log"""
        raise NotImplementedError

    @staticmethod
    def e(tag: str, message: str):
        """error log"""
        raise NotImplementedError
