class TorKham:    
	def __init__(self):
		self.words = []
	def restart(self):
		self.words.clear()
		return "game restarted"
	def play(self, word):
		if len(self.words)==0:
				self.words.append(word)
				return  "'"+word+"' -> "+str(self.words)
		elif self.words[-1][-1].upper()==word[1].upper() and self.words[-1][-2].upper()==word[0].upper():
				self.words.append(word)
				return  "'"+word+"' -> "+str(self.words)
		else:    			
				return "'"+word+"' -> game over"

torkham = TorKham()
print("*** TorKham HanSaa ***")
S = input("Enter Input : ").split(',')
State = " "
for e in S:
	if e[0] in "PRX":
		State=e[0]	
		if State=="x":
			break
	else:
		print("'"+e+"' is Invalid Input !!!")
		break
			
	if State == 'P':
		temp = e[2:]
		print(torkham.play(temp))
	elif State =='R':
		print(torkham.restart())