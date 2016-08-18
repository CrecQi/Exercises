#This program recognizes out ANAGRAMS
def Enter():
	word_0 = raw_input("Enter the first word>>>")
	word_1 = raw_input("Enter the second word>>>")
	global word_0, word_1

def Anagram_analyse(w1,w2):
	for i in range(0,len(w1)):
		chr_list_0.append(w1[i])
	chr_list_0.sort()
	print chr_list_0

	for i in range(0,len(w2)):
		chr_list_1.append(w2[i])
	chr_list_1.sort()
	print chr_list_1

	if chr_list_0 == chr_list_1:
		print "The words are anagrams."
	else:
		print "The words aren't anagrams."

running = True
while running:
	chr_list_0 = []
	chr_list_1 = []
	Enter()
	Anagram_analyse(word_0,word_1)
