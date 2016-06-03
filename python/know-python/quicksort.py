#!/usr/bin/env python3

def quicksort(lst):
	print(lst)
	if len(lst) in (0,1):
		return lst
	else:
		return quicksort([x for x in lst[1:] if x<lst[0]])+[lst[0]]+quicksort([x for x  in lst[1:] if x>lst[0]])

if __name__=='__main__':
	lst=[5,46,1,-1,534,10,23,4]
	print(quicksort(lst))
