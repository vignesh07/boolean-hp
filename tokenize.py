from nltk.tokenize.punkt import PunktWordTokenizer
import os.path

chap_numbers=[[]]
for n in range(0,16):
	chap_numbers.append(str(n))
i=1
chap_words=[]
for chapter in chap_numbers:
	name=chapter+".txt"
	f=open(os.path.join("chapters",name),'r')
	for line in f:
		#print line
		chap_words.append(PunktWordTokenizer().tokenize(line))
	f.close()
	i=i+1

print chap_words[2]