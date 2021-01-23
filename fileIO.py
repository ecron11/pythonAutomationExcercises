f = open('inputFile.txt', 'r')
passFile = open('passFile.txt', 'w')
failFile = open('failFile.txt', 'w')
passCount = 1
failCount = 1
for line in f:
        line_split = line.split()
        if line_split[2] == 'P':
            passFile.write(str(passCount) + ' ' + line)
            passCount = passCount + 1
        else: 
            failFile.write(str(failCount) + ' ' + line)
            failCount = failCount + 1
passFile.close()
failFile.close()
f.close()



