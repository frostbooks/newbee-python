Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> dict1 = {}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict1.fromkeys((1,2,3),'number')
{1: 'number', 2: 'number', 3: 'number'}
>>> dict1.fromkey((1,2),'number')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    dict1.fromkey((1,2),'number')
AttributeError: 'dict' object has no attribute 'fromkey'
>>> dict1.fromkeys((1,2),'number')
{1: 'number', 2: 'number'}
>>> dict1= =dict1.fromkeys(range(32),'赞')
SyntaxError: invalid syntax
>>> dict1 = dict1.fromkeys(range(32),'赞')
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> for each_key in dict1.keys()
SyntaxError: invalid syntax
>>> for each_key in dict1.keys():
	print(each_key)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
>>> for each_value in dict1.values():
	print(each_value)

	
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
赞
>>> for each_items in dict1.items():
	print(each_items)

	
(0, '赞')
(1, '赞')
(2, '赞')
(3, '赞')
(4, '赞')
(5, '赞')
(6, '赞')
(7, '赞')
(8, '赞')
(9, '赞')
(10, '赞')
(11, '赞')
(12, '赞')
(13, '赞')
(14, '赞')
(15, '赞')
(16, '赞')
(17, '赞')
(18, '赞')
(19, '赞')
(20, '赞')
(21, '赞')
(22, '赞')
(23, '赞')
(24, '赞')
(25, '赞')
(26, '赞')
(27, '赞')
(28, '赞')
(29, '赞')
(30, '赞')
(31, '赞')
>>> dict1[32]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict1[32]
KeyError: 32
>>> dict1[31]
'赞'
>>> dict.get(32)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict.get(32)
TypeError: descriptor 'get' requires a 'dict' object but received a 'int'
>>> dict1.get(32)
>>> print(dict1.get(32))
None
>>> print(dict1.get(31))
赞
>>> print(dict1[31])
赞
>>> 32 in dict1
False
>>> dict1
{0: '赞', 1: '赞', 2: '赞', 3: '赞', 4: '赞', 5: '赞', 6: '赞', 7: '赞', 8: '赞', 9: '赞', 10: '赞', 11: '赞', 12: '赞', 13: '赞', 14: '赞', 15: '赞', 16: '赞', 17: '赞', 18: '赞', 19: '赞', 20: '赞', 21: '赞', 22: '赞', 23: '赞', 24: '赞', 25: '赞', 26: '赞', 27: '赞', 28: '赞', 29: '赞', 30: '赞', 31: '赞'}
>>> dict1.clear()
>>> dict1
{}
>>> dict1 = {}
>>> a = {'name':'eddy'}
>>> b = a
>>> b
{'name': 'eddy'}
>>> a
{'name': 'eddy'}
>>> a = {}
>>> b
{'name': 'eddy'}
>>> a
{}
>>> a = b
>>> a
{'name': 'eddy'}
>>> b
{'name': 'eddy'}
>>> b.clear()
>>> b
{}
>>> a
{}
>>> a = {'name':'eddy'}
>>> b= a
>>> b
{'name': 'eddy'}
>>> a
{'name': 'eddy'}
>>> b.clear()
>>> a
{}
>>> b
{}
>>> a = {'eddy':'wow'}
>>> b = a.copy()
>>> c= a
>>> b
{'eddy': 'wow'}
>>> c
{'eddy': 'wow'}
>>> id(a)
86092560
>>> id(b)
95448688
>>> id(c)
86092560
>>> c[4] = 'four'
>>> a
{'eddy': 'wow', 4: 'four'}
>>> b
{'eddy': 'wow'}
>>> c
{'eddy': 'wow', 4: 'four'}
>>> a.pop(4)
'four'
>>> a
{'eddy': 'wow'}
>>> c
{'eddy': 'wow'}
>>> b
{'eddy': 'wow'}
>>> a[4] = 'dour'
>>> 
>>> a[5] = 'five'
>>> a[6] = 'six'
>>> a
{'eddy': 'wow', 4: 'dour', 5: 'five', 6: 'six'}
>>> a.popitem()
(6, 'six')
>>> a.popitem()
(5, 'five')
>>> a
{'eddy': 'wow', 4: 'dour'}
>>> a.setdefault(10:'tem')
SyntaxError: invalid syntax
>>> a.setdefault(10,'ten')
'ten'
>>> a
{'eddy': 'wow', 4: 'dour', 10: 'ten'}
>>> b = {10:'dog'}
>>> a.update(b)
>>> a
{'eddy': 'wow', 4: 'dour', 10: 'dog'}
>>> c = {'war':'nazi'}
>>> a.update(c)
>>> a
{'eddy': 'wow', 4: 'dour', 10: 'dog', 'war': 'nazi'}
>>> a['was']  ='qaq'
>>> a
{'eddy': 'wow', 4: 'dour', 10: 'dog', 'war': 'nazi', 'was': 'qaq'}
>>> a = {1,2,3,4,5}
>>> a[2]
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a[2]
TypeError: 'set' object does not support indexing
>>> set1 = set([1,2,3,4,5,5])
>>> set1
{1, 2, 3, 4, 5}
>>> num1 = [1,2,3,4,5,3,1]
>>> temp = []
>>> for each in num1:
	if each not in temp:
		temp.append(each)

		
>>> temp
[1, 2, 3, 4, 5]
>>> num1
[1, 2, 3, 4, 5, 3, 1]
>>> a = list(set(num1))
>>> a
[1, 2, 3, 4, 5]
>>> num1
[1, 2, 3, 4, 5, 3, 1]
>>> se1
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    se1
NameError: name 'se1' is not defined
>>> set1
{1, 2, 3, 4, 5}
>>> set1.add(123)
>>> set
<class 'set'>
>>> set1
{1, 2, 3, 4, 5, 123}
>>> set.remove(1)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    set.remove(1)
TypeError: descriptor 'remove' requires a 'set' object but received a 'int'
>>> set1.remove(1)
>>> set1
{2, 3, 4, 5, 123}
>>> num1 = frozenset([1,2,3,4,5])
>>> num1.add(6)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    num1.add(6)
AttributeError: 'frozenset' object has no attribute 'add'
>>> num1 = frozenset({1,2,3,4,5})
>>> num1
frozenset({1, 2, 3, 4, 5})
>>> 
>>> 
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending (which on some Unix systems, means that all writes
    append to the end of the file regardless of the current seek position).
    In text mode, if encoding is not specified the encoding used is platform
    dependent: locale.getpreferredencoding(False) is called to get the
    current locale encoding. (For reading and writing raw bytes use binary
    mode and leave encoding unspecified.) The available modes are:
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
    
    The default mode is 'rt' (open for reading text). For binary random
    access, the mode 'w+b' opens and truncates the file to 0 bytes, while
    'r+b' opens the file without truncation. The 'x' mode implies 'w' and
    raises an `FileExistsError` if the file already exists.
    
    Python distinguishes between files opened in binary and text modes,
    even when the underlying operating system doesn't. Files opened in
    binary mode (appending 'b' to the mode argument) return contents as
    bytes objects without any decoding. In text mode (the default, or when
    't' is appended to the mode argument), the contents of the file are
    returned as strings, the bytes having been first decoded using a
    platform-dependent encoding or using the specified encoding if given.
    
    'U' mode is deprecated and will raise an exception in future versions
    of Python.  It has no effect in Python 3.  Use newline to control
    universal newlines mode.
    
    buffering is an optional integer used to set the buffering policy.
    Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
    line buffering (only usable in text mode), and an integer > 1 to indicate
    the size of a fixed-size chunk buffer.  When no buffering argument is
    given, the default buffering policy works as follows:
    
    * Binary files are buffered in fixed-size chunks; the size of the buffer
      is chosen using a heuristic trying to determine the underlying device's
      "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
      On many systems, the buffer will typically be 4096 or 8192 bytes long.
    
    * "Interactive" text files (files for which isatty() returns True)
      use line buffering.  Other text files use the policy described above
      for binary files.
    
    encoding is the name of the encoding used to decode or encode the
    file. This should only be used in text mode. The default encoding is
    platform dependent, but any encoding supported by Python can be
    passed.  See the codecs module for the list of supported encodings.
    
    errors is an optional string that specifies how encoding errors are to
    be handled---this argument should not be used in binary mode. Pass
    'strict' to raise a ValueError exception if there is an encoding error
    (the default of None has the same effect), or pass 'ignore' to ignore
    errors. (Note that ignoring encoding errors can lead to data loss.)
    See the documentation for codecs.register or run 'help(codecs.Codec)'
    for a list of the permitted encoding error strings.
    
    newline controls how universal newlines works (it only applies to text
    mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
    follows:
    
    * On input, if newline is None, universal newlines mode is
      enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
      these are translated into '\n' before being returned to the
      caller. If it is '', universal newline mode is enabled, but line
      endings are returned to the caller untranslated. If it has any of
      the other legal values, input lines are only terminated by the given
      string, and the line ending is returned to the caller untranslated.
    
    * On output, if newline is None, any '\n' characters written are
      translated to the system default line separator, os.linesep. If
      newline is '' or '\n', no translation takes place. If newline is any
      of the other legal values, any '\n' characters written are translated
      to the given string.
    
    If closefd is False, the underlying file descriptor will be kept open
    when the file is closed. This does not work when a file name is given
    and must be True in that case.
    
    A custom opener can be used by passing a callable as *opener*. The
    underlying file descriptor for the file object is then obtained by
    calling *opener* with (*file*, *flags*). *opener* must return an open
    file descriptor (passing os.open as *opener* results in functionality
    similar to passing None).
    
    open() returns a file object whose type depends on the mode, and
    through which the standard file operations such as reading and writing
    are performed. When open() is used to open a file in a text mode ('w',
    'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
    a file in a binary mode, the returned class varies: in read binary
    mode, it returns a BufferedReader; in write binary and append binary
    modes, it returns a BufferedWriter, and in read/write mode, it returns
    a BufferedRandom.
    
    It is also possible to use a string or bytearray as a file for both
    reading and writing. For strings StringIO can be used like a file
    opened in a text mode, and for bytes a BytesIO can be used like a file
    opened in a binary mode.

>>> f = open('E:\\test.txt','w')
>>> f.write('i love you')
10
>>> f.close()
>>> 
