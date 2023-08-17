class UniformedSearchStrategies:
	def generate_sequence(self,n,color):
		if (color == "r"):
			sequence = [i for i in range(1,n+1,2)]
			return sequence
		if (color == "g"):
			sequence = [i for i in range(2,n+1,2)]
			return sequence
			

	def normalPrint(self, color, sequence):
		print("color:", color,"\nSequence: ",end="")
		for i in range(len(sequence)):
		    print(sequence[i],end=", ")
		print("\n")

	
	def generate_BSTsequence(self,n,color):
		if(color =="r"):
			print("color: RED","\nTree Sequence ")
			for i in range(1,n+1,2):
				print(i," => ",(2*i)+1,",",(2*i)+3,"")
		if(color =="g"):
			print("color: GREEN","\nTree Sequence ")
			for i in range(2,n+1,2):
				print(i," => ",(2*i),",",(2*i)+2,"")
			



color = input("Enter the Color of the ball (r:g): ")
n = int(input("Enter the number of balls: "))

uss = UniformedSearchStrategies()
sequence = uss.generate_sequence(n,color)
uss.normalPrint(color, sequence)
uss.generate_BSTsequence(n,color)

