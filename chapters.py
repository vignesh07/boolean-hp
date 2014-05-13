#extract contents from each chapter and organise it into chapters 

import os.path

chap_numbers =["ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN",
				"ELEVEN","TWELVE","THIRTEEN","FOURTEEN","FIFTEEN","SIXTEEN","SEVENTEEN","EIGHTEEN"]


number =0
chap="CHAPTER "

while(number<17):
	name = chap+chap_numbers[number]
	name_f = str(number)+".txt"
	next=chap+chap_numbers[number+1]
	curr=open(os.path.join("chapters",name_f),'w')
	f= open("st.txt",'r')
	for line in f:
		if(name in line):
			
			for line in f:
				curr.write(line)
				if(next in line):
					break
			break		
	
	number=number+1






			
	




