Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> xxx = Employee("xuelei",40,161,"nan")
>>> xxx.s

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    xxx.s
AttributeError: Employee instance has no attribute 's'
>>> xxx.speakEnglish
<bound method Employee.speakEnglish of <__main__.Employee instance at 0x019F3968>>
>>> xxx.name
'xuelei'
>>> xxx.canPrograme
<bound method Employee.canPrograme of <__main__.Employee instance at 0x019F3968>>
>>> aaa =Employee('xue',40,161,'nan')
>>> aaa.canPrograme
<bound method Employee.canPrograme of <__main__.Employee instance at 0x019F38A0>>
>>> aaa.stu_no
40
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> aaa = ('xue',40,161,'nan')
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> xxx = Employee("xuelei",40,161,"nan")
>>> xxx.
SyntaxError: invalid syntax
>>> xxx.canPrograme
<bound method Employee.canPrograme of <__main__.Employee instance at 0x01AD3968>>
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> xxx = Employee("xuelei",40,161,"nan")
>>> xxx.c

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    xxx.c
AttributeError: Employee instance has no attribute 'c'
>>> xxx.canPrograme
<bound method Employee.canPrograme of <__main__.Employee instance at 0x01E88698>>
>>> xxx.canPrograme()
name  xuelei  can programe
>>> xxx.stu_no()

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    xxx.stu_no()
TypeError: 'int' object is not callable
>>> xxx.st

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    xxx.st
AttributeError: Employee instance has no attribute 'st'
>>> xxx.stu_no()

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    xxx.stu_no()
TypeError: 'int' object is not callable
>>> xxx.canPrograme()
name  xuelei  can programe
>>> xxx.speakEnglish()
name xuelei can speak english
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> xxx = Employee("xuelei",40,161,"nan")
>>> xxx.stu_no()

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    xxx.stu_no()
TypeError: 'int' object is not callable
>>> xxx.canPrograme()
name: xuelei  can programe
>>> 
==================== RESTART: D:\40薛磊\新建文件夹\123.py ====================
>>> xxx = Employee("xuelei",40,161,"nan")
>>> xxx.canSwim
<bound method Employee.canSwim of <__main__.Employee instance at 0x01B33968>>
>>> xxx.canSwim()
name: xuelei can swim 
>>> xxx.name
'xuelei'
>>> xxx.stu_no
40
>>> xxx.gender
'nan'
>>> xx= Employee("xuelei",40,161,"man")
>>> xx.gender
'man'
>>> 
