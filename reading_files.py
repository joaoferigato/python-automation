f = open('C:\\Users\\Joao\\Downloads\\Ex_Files_Python_Automation\\Exercise Files\\inputFile.txt', 'r')

passFile = open('.\\passFile.txt', 'w')
failFile = open('.\\failFile.txt', 'w')

for line in f:
    line_split = line.split()
    if line_split[2] == 'P':
        passFile.write(line)
    else:
        failFile.write(line)

f.close()
passFile.close()
failFile.close()