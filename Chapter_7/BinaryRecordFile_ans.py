"""
>>> import shutil
>>> import sys

>>> S = struct.Struct("<15s")
>>> fileA = os.path.join(tempfile.gettempdir(), "fileA.dat")
>>> fileB = os.path.join(tempfile.gettempdir(), "fileB.dat")
>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> brf = BinaryRecordFile(fileA, S.size)
>>> for i, text in enumerate(("Alpha", "Bravo", "Charlie", "Delta",
...        "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
...        "Kilo", "Lima", "Mike", "November", "Oscar", "Papa",
...        "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
...        "Whisky", "X-Ray", "Yankee", "Zulu")):
...    brf[i] = S.pack(text.encode("utf8"))
>>> assert len(brf) == 26
>>> brf[len(brf) + 2] = S.pack(b"Extra at the end")
>>> assert len(brf) == 29
>>> shutil.copy(fileA, fileB)
'C:\\\\Users\\\\zhangjuh\\\\AppData\\\\Local\\\\Temp\\\\fileB.dat'
>>> del brf[12]
>>> assert len(brf) == 28
>>> brf.close()

>>> os.path.getsize(fileA) // S.size
28
>>> os.path.getsize(fileB) // S.size
29
>>> if ((os.path.getsize(fileA) + (S.size)) !=
...        os.path.getsize(fileB)):
...    print("FAIL#1: expected file sizes are wrong")
...    sys.exit()

>>> shutil.copy(fileB, fileA)
'C:\\\\Users\\\\zhangjuh\\\\AppData\\\\Local\\\\Temp\\\\fileA.dat'
>>> if os.path.getsize(fileA) != os.path.getsize(fileB):
...    print("FAIL#2: expected file sizes differ")
...    sys.exit()

>>> for name in (fileA, fileB):
...    try:
...        os.remove(name)
...    except EnvironmentError:
...        pass

>>> filename =  os.path.join(tempfile.gettempdir(), "test.dat")
>>> if os.path.exists(filename): os.remove(filename)
>>> S = struct.Struct("<8s")
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> test.close()
>>> os.path.getsize(filename)
40
>>> test = BinaryRecordFile(filename, S.size)
>>> len(test)
5
>>> while len(test) > 0:
...     del test[0]
>>> test.close()
>>> os.path.getsize(filename)
0
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> del test[2]
>>> test.close()
>>> os.path.getsize(filename)
32
>>> test = BinaryRecordFile(filename, S.size)
>>> test[0] = S.pack(b"Alpha")
>>> test[1] = S.pack(b"Bravo")
>>> test[2] = S.pack(b"Charlie")
>>> test[3] = S.pack(b"Delta")
>>> test[4] = S.pack(b"Echo")
>>> del test[0]
>>> for i in range(len(test)):
...     print(struct.unpack("<8s", test[i]))
>>> test.close()
>>> os.path.getsize(filename)
32
>>> os.remove(filename)
"""

import struct
import os
import tempfile

class OutOfIndexError(Exception):pass

class BinaryRecordFile:
    def __init__(self, filename, record_size, auto_flush = True):
        """A random access binary file that behaves rather like a list
        with each item a bytes or bytearray object of record_size.
        """
        self.__record_size = record_size
        mode = "w+b" if not os.path.exists(filename) else "r+b"
        self.__fh = open(filename, mode)
        self.auto_flush = auto_flush

    @property
    def record_size(self):
        "Return the record size of file"
        return self.__record_size

    @property
    def name(self):
        "Return the filename"
        return self.__fh.name

    @property
    def size(self):
        "Return the record number in the file"
        if self.auto_flush:
            self.__fh.flush()
        self.__fh.seek(0, os.SEEK_END)
        end = self.__fh.tell()
        return end // self.record_size

    def flush(self):
        """Flush writes to disk
        Done automatically if auto_flush is True
        """
        self.__fh.flush()

    def close(self):
        "Close the file"
        self.__fh.close()

    def append(self, record):
        "Append a record to the tail of file"
        assert len(record) == self.__record_size, \
               "the record size should be {0}".format(self.record_size)
        self.__fh.seek(0, os.SEEK_END)
        self.__fh.write(record)
    
    def __seek_to_index(self, index):
        if index > self.size:
            raise OutOfIndexError("no record at index position {0}".format(
                                    index))
        self.__fh.seek(index * self.record_size)

    def __setitem__(self, index, record):
        """Sets the item at position index to be the given record
        The inde position can not be beyond the current end of file.
        """ 
        assert isinstance(record, (bytes, bytearray)), "Binary data required"
        assert len(record) == self.__record_size, \
            "record must be exactly {0} bytes".format(self.record_size)
        # assert index <= self.size + 1, "Index is out of range, no data"
        self.__fh.seek(index * self.record_size)
        self.__fh.write(record)
        if self.auto_flush:
            self.__fh.flush()

    def __getitem__(self, index):
        """Returns the item at the given index position
        If there is no item at the given position, raises an Error
        """
        self.__seek_to_index(index)
        return self.__fh.read(self.record_size)

    def __delitem__(self, index):
        "Deletes the item at the given index position"
        for i in range(index, self.size - 1):
            self[i] = self[i+1]
        self.__fh.truncate((self.size - 1) * self.__record_size)

    def __len__(self):
        return self.size

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = False)

