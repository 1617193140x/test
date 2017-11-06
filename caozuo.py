#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Employee:
   '所有学生的基类'
   
   empCount = 0
 
   def __init__(self, name, stu_no,class_no,gender):
      self.name = name
      self.stu_no = stu_no
      self.class_no = class_no
      self.gender = gender
      Employee.empCount += 1
   
   def speakEnglish(self):
      print "name:" ,self.name,"can speak english"
 
   def canPrograme(self):
      print "name:" , self.name," can programe"
      
   def canSwim(self):
      print "name:" , self.name,"can swim "
   
