class Log:
    def __init__(self, tag, msg, *args):
        self.__msg__ = str(msg).format(*args)
        self.__tag__ = tag

    @classmethod
    def d(cls, tag, msg, *args):
        print(cls._detail_msg('d', tag, msg, *args))

    @classmethod
    def e(cls, tag, msg, *args):
        print(cls._detail_msg("d", tag, msg, *args))

    @classmethod
    def i(cls, tag, msg, *args):
        print(cls._detail_msg("i", tag, msg, *args))

    @classmethod
    def w(cls, tag, msg, *args):
        print(cls._detail_msg("d", tag, msg, *args))

    @classmethod
    def _msg_generator(cls, fun, tag, msg):
        switch_map = {
            "d" : "Debug - ",
            "i" : "Info - ",
            "w" : "Warning - ",
            "e" : "Error - "
        }
        if str(fun) in switch_map.keys():
            return switch_map[fun] + str(tag) + " : " + str(msg)
        else:
            raise ValueError("Invalid function name of {}".format(fun))

    @classmethod
    def _detail_msg(cls, fun, tag, msg, *args):
        return Log._msg_generator(fun, tag, msg).format(*args)


if __name__ == "__main__":
   log = Log("tag", "msg")
   print(Log.d.__name__)
   Log.d("Tag", "wrong msg")