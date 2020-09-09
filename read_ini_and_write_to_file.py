from configparser import ConfigParser
CP = ConfigParser()
CP.read('ini_file.ini')
text1 = CP['Texts']['Text1']
text2 = CP['Texts']['Text2']
text3 = CP['Texts']['Text3']
text1_file = open('text1.txt', 'w')
text2_file = open('text2.txt', 'w')
text3_file = open('text3.txt', 'w')
all_in_one = open('all_in_one.txt', 'w')
text1_file.write(text1)
text2_file.write(text2)
text3_file.write(text3)
all_in_one.write(text1 + '\n' + text2 + '\n' + text3)
print (text1)
print (text2)
print (text3)
print ('Donate: https://www.donationalerts.com/r/n0namer1337')