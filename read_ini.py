from configparser import ConfigParser
CP = ConfigParser()
CP.read('ini_file.ini')
text1 = config['Texts']['Text1']
text2 = config['Texts']['Text2']
text3 = config['Texts']['Text3']
print (text1)
print (text2)
print (text3)
