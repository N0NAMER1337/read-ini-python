from configparser import ConfigParser #Include library
CP = ConfigParser() 
CP.read('ini_file.ini') #Read ini file
text1 = CP['Texts']['Text1'] #Write data from ini file to variables
text2 = CP['Texts']['Text2']
text3 = CP['Texts']['Text3']
print (text1) #Print variables
print (text2)
print (text3)
print ('Donate: https://www.donationalerts.com/r/n0namer1337')