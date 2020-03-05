
import re
import sys

print(sys.argv)


def doreplace (m) :

    return m.group(1) + "INTEGER" + m.group(3)

searchstr = re.compile(r'".*"')
searchint = re.compile(r'(?<!")(0|[1-9][0-9]*)(?!")')

#filename = input("Please enter file name to search for integers: ")
filename = sys.argv[1]

fp = open(filename, "r")
text = fp.read()
fp.close()

'''
intlist = searchobj.findall(text)

newlist = []

for integer in intlist :
    if not int(integer) in newlist :
        newlist.append(int(integer))

newlist.sort()
print(newlist)
'''

newtext = searchstr.sub("STRING", text)
newtext = searchint.sub("INTEGER", newtext)
print(newtext)


