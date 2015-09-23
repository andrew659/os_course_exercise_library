#!/usr/bin/python
#coding=utf-8

from optparse import OptionParser
import sys
import os
import re

reload(sys)  
sys.setdefaultencoding('utf8')


usage="usage: %prog DIRECTORY [options]"
parse = OptionParser(usage=usage)
#parse.add_option("-p", "--path", default="", help="题库目录", action="store", type="string", dest="path")
parse.add_option("-t", "--type", default="", help="题目类型，多个类型之间用英文逗号分割", action="store", type="string", dest="type")
parse.add_option("-q", "--question", default="", help="题干关键字，多个关键字之间用英文逗号分割", action="store", type="string", dest="question")
parse.add_option("-o", "--option", default="", help="选择项关键字，多个关键字之间用英文逗号分割", action="store", type="string", dest="option")
parse.add_option("-a", "--answer", default="", help="答案解释关键字，多个关键字之间用英文逗号分割", action="store", type="string", dest="answer")
parse.add_option("-s", "--source", default="", help="出处关键字，多个关键字之间用英文逗号分割", action="store", type="string", dest="source")
(options, args)=parse.parse_args()


if len(sys.argv)<2:
   print "missing operand"
   print "Try --help for more information."
   exit(-1)


count=0
pa1=options.type.split(',')
pa2=options.question.split(',')
pa3=options.option.split(',')
pa4=options.answer.split(',')
pa5=options.source.split(',')
print pa1,pa2,pa3,pa4,pa5
try:
    for parent,dirnames,filenames in os.walk(sys.argv[1]):
        for filename in filenames:
            if filename.find(".md")==-1 or filename=='examples.md' or filename.find(".md~")!=-1:
               continue
            else:
               i=""
               tg=""
               xx=""
               cc=""
               js=""
               kn=""
               result=1
               fr=open(sys.argv[1]+'/'+filename, 'rb')
   
               
               for line in fr.readlines():   
                   if re.search(u'^(- \[)', line)!=None or re.search('^(- \()', line)!=None:
                       # print line
                        xx+=line.strip('\n')
                   elif re.search('^(> 出处：)', line)!=None:
                        #print cc
                        cc=line.strip('\n')
    
                   elif re.search('^(> 知识点：)', line)!=None:
                        kn=line.strip('\n')
                        #print kn
                   elif re.search('^(> )', line)!=None:
                        js+=line.strip('\n')
                   elif re.search('^(\d\n)$', line)!=None:
                        i=line.strip('\n')
                   elif line.strip('\n')!='':
                        tg+=line.strip('\n')


               #print cc
               fr.close()
               if options.type!='':
                  flag=0
                  for j in range(len(pa1)):
                    if i.find(pa1[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue

               if options.question!='':
                  flag=0
                  for j in range(len(pa2)):
                    if tg.find(pa2[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if options.option!='':
                  flag=0
                  for j in range(len(pa3)):
                    if xx.find(pa3[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if options.answer!='':
                  flag=0
                  for j in range(len(pa4)):
                    if js.find(pa4[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue
               if options.source!='':
                  flag=0
                  for j in range(len(pa5)):
                    if cc.find(pa5[j])!=-1:
                        flag=1
                        result=1
                  if flag==0:
                    continue

               if result==1:
                  count=count+1
                  print filename
                  #shutil.copyfile(parent+'/'+filename, "./result/"+filename)
    print count,"个文件"
except Exception,e:
   print e

