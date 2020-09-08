from configparser import ConfigParser
CP = ConfigParser()
CP.read('ini_file.ini')
text1 = CP['Texts']['Text1']
text2 = CP['Texts']['Text2']
text3 = CP['Texts']['Text3']
print (text1)
print (text2)
print (text3)
