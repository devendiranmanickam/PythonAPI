#!/usr/bin/python3


# open the log file
with open(r'imblog.log') as logFile:
    count = 0
    for logline in logFile:
        # look for 'source ip' address
        if logline.lower().__contains__('source address'):
            # if "source address" in logline.lower(): # another method
            # count = count + 1
            count += 1
            # print to the file
            # print(logline)
            print(logline.split(' ')[-1], end="")  # best method to exclude \n at the EOL
            with open('imblog.out', "a") as outputFile:  # a for append mode as we are inside the loop
                print(logline.split(' ')[-1], end="", file=outputFile)  # print to file instead of stdout

print("\n \t source ip address exists", count, "times")

with open('imblog.out') as outFile:
    print(set(outFile.readlines()))  # set is to remove duplicate lines
