# TREE IN PYTHON
# version - 01
"""
arr = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
i = 1
while(i <= len(arr)+1):
	if(i ==0): pass
	for j in range(i//2, i):
		print(arr[j-1], end=" ")
	i *=2
	print("")
for i in range((i//2)-1,len(arr)):
	print(arr[i], end=" ")
	
print("\n\n")"""

# version - 02
"""
arr = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61]
i = 1
data=[]
while(i <= len(arr)+1):
	data.append([i])
	for j in range(i//2, i):
		if(i == 1): continue
		else:
			if((j)%2 == 0): print("\t",end="")
			print(arr[j-1], end=" ")
			
	i *=2
	print("")
for i in range((i//2)-1,len(arr)):
	print(arr[i], end=" ")
	
print(f"\n{data}\n")
"""

# version - 03
"""
arr = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61]
data = []
for i in range(1,len(arr)):
	print(arr[i-1]," => ",(2*arr[i-1])+1,",",(2*arr[i-1])+3,"")
	data.append([arr[i-1],(2*arr[i-1])+1,(2*arr[i-1])+3])

print(data)
"""


# version - 04
n=10
data = []
for i in range(1,n+1,2):
	print(i," => ",(2*i)+1,",",(2*i)+3,"")
	data.append([i,(2*i)+1,(2*i)+3])

print(data)



n=10






















