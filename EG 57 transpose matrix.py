lst=eval(input("enter matrix:="))

#transpose the 2D list using list comprehension
tm=[[row[i]for row in lst]
    for i in range(len(lst[0]))]

#print the originate and transposed matrices
print("")
