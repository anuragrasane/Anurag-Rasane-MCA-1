singlestring=('WELCOMETOATESTC')
#String Reversing
print(singlestring[::-1])
print("".join(reversed(singlestring)))
#String Slicing
s1=slice(2,6,1)
s2=slice(1,5,2)
s3=slice (-1,-12,-2)
print(singlestring[slice(2,8)])
print(singlestring[slice (-1,-12,-2)])
#String slicing using List
print(singlestring[:3])
#[start:stop:steps]
print(singlestring[1:6:1])
#Using islice()
import itertools
#prints given indices charactrers
#itertools.islice(iterable.start,stop,step)
print("".join(itertools.islice(singlestring,1,8,2)))
#Updating or Deleting String
list1=list(singlestring)
list1[2]='P'
String2="".join(list1)
print(String2)
#Escape Sequence
#Using Triple quote to Escape single and double qoute
print('''I'm using "Python"''')
#Using Backslash for sngle Quote
print('I\'m using Python')
#Using Backslash for Double Quote
print('I\'m using \"Python\"')
'''
Format Method

String10= "{] {} {}".format(List1)
'''
#Python List
List1=[20,21.20,3+4j,'Life',('Python','Java','Javascript')]
print(List1)
print(List1[0])
print(List1[1])
print(List1[4])
print("\nList items: ",List1[0],List1[1],List1[3])
#Multi Dimentional List
List2=[[20,21.20],[3+4j,2+2j,7+2j],['Life','Python','Java','Javascript']]
print(List2[1][2])
print(List2[0][1])
print(List2[0][0])
