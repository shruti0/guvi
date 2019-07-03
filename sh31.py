vowel=['a','e','i','o','u']
consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
ch = input(' ')
if ch in vowel:
	print('vowel')
elif ch in consonant:
	print('consonant')
else:
	print('Invalid')
