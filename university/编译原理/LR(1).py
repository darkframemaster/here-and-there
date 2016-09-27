#!/usr/bin/env python3.4
#!-*- coding:utf-8 -*-
import re

#function:
def s(ope,num):#将操作符和状态压入
	global Stack
	global list_input
	global COUNT
	if COUNT<len(list_input):
		COUNT=COUNT+1
	Stack.append(ope)
	Stack.append(num)	
	if COUNT<len(list_input):
		print("移进:"+ope+'\t\t',   Stack ,'\t'+'next'+list_input[COUNT])
	else:	
		print("移进:"+ope+'\t\t',   Stack ,'\t'+'next'+list_input[COUNT-1])

def r(num):			
	global Stack
	global list_input
	global LR_Table
	if(num==6):		#计算pop的次数
		pop_time=1
	else:
		pop_time=len(method[str(num)])-3
	while(pop_time>0):	#弹出
		Stack.pop()
		Stack.pop()
		pop_time=pop_time-1
	Stack.append(method[str(num)][0])#压入非终结符
	if(LR_Table[str(Stack[-2])][str(Stack[-1])] is not None):
		Stack.append(LR_Table[str(Stack[-2])][str(Stack[-1])])#压入状态
	else:
		print("归约:error")
	print("归约:"+method[str(num)]+'\t\t',   Stack   ,'\t'+'next'+list_input[COUNT])
#data
method={'1':'E->E+T','2':'E->T','3':'T->T*F','4':'T->F','5':'F->(E)','6':'F->id'}

Stack=['0']	
LR_Table={
'0':{'id':'s(5)','+':None,'*':None,'(':'s(4)',')':None,'$':None,'E':'1','T':'2','F':'3'},
'1':{'id':None,'+':'s(6)','*':None,'(':'s(4)',')':None,'$':'acc','E':None,'T':None,'F':None},
'2':{'id':None,'+':'r(2)','*':'s(7)','(':None,')':'r(2)','$':'r(2)','E':None,'T':None,'F':None},
'3':{'id':None,'+':'r(4)','*':'r(4)','(':None,')':'r(4)','$':'r(4)','E':None,'T':None,'F':None},
'4':{'id':'s(5)','+':None,'*':None,'(':'s(4)',')':None,'$':None,'E':'8','T':'2','F':'3'},
'5':{'id':None,'+':'r(6)','*':'r(6)','(':None,')':'r(6)','$':'r(6)','E':None,'T':None,'F':None},
'6':{'id':'s(5)','+':None,'*':None,'(':'s(4)',')':None,'$':None,'E':None,'T':'9','F':'3'},
'7':{'id':'s(5)','+':None,'*':None,'(':'s(4)',')':None,'$':None,'E':None,'T':None,'F':'10'},
'8':{'id':None,'+':'s(6)','*':None,'(':None,')':'s(11)','$':None,'E':None,'T':None,'F':None},
'9':{'id':None,'+':'r(1)','*':'s(7)','(':None,')':'r(1)','$':'r(1)','E':None,'T':None,'F':None},
'10':{'id':None,'+':'r(3)','*':'r(3)','(':None,')':'r(3)','$':'r(3)','E':None,'T':None,'F':None},
'11':{'id':None,'+':'r(5)','*':'r(5)','(':None,')':'r(5)','$':'r(5)','E':None,'T':None,'F':None},
}


#main program
Input=input('input a sentence:')
list_input=[]
for i in Input:		#chuli shuru
	if i=='i':
		continue
	elif i=='d':
		list_input.append('id')
	else:
		list_input.append(i)

print(list_input)
COUNT=0
while(True):		#循环检查
	if COUNT<len(list_input):	
		i=list_input[COUNT]#i是下一个操作符
		#print(Stack[-1],i)
	if(LR_Table[Stack[-1]][i]==None):#查栈顶元素和下一个操作符的操作 如果是none那么错误 如果是acc结束 否则看具体进行什么操作。
		print('error!')
		COUNT=COUNT+1
	elif(LR_Table[Stack[-1]][i]=='acc'):#正确结束的标志
		print('accept!')
		exit()
	else:#分析进行什么操作，并计算出操作符和操作的状态
		if((LR_Table[Stack[-1]][i][0])=='s'):
			if LR_Table[Stack[-1]][i][3]==')':
				s(i,LR_Table[Stack[-1]][i][2])
			else:
				s(i,LR_Table[Stack[-1]][i][2]+LR_Table[Stack[-1]][i][3])
		elif((LR_Table[Stack[-1]][i][0])=='r'):
			r(int(LR_Table[Stack[-1]][i][2]))
