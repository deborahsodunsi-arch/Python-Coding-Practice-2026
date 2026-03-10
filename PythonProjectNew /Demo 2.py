# How we define list []
values = [ 1, 2, "simi",4, 5]
# list is data type that allows multiple values and can be different data types

print (values[0])  #1
print (values[3])  #4
print (values[-1])  #5
print (values[1:4])  # expect to see 2 simi & 4

values.insert(3,"shetty")
print(values)
values.append(6)  #[1, 2, 'simi', 'shetty', 4, 5, 6]
print(values)
values [2]="SIMI"  #Updating value
print(values)
del values [0]
print(values)

# How we define Tuple () is same as list data but immutable

val = ( 1, 2, "simi", 4.5)

# Dictionary
dic = {"a":2, 4: "simi", "c": "I love God"}
print(dic["a"])
print(dic[4])
print(dic["c"])

# insert values into dictionary and add key value pairs

dict = {}
dict ["first name"] = "SIMI"

dict["last name"] = "ODUNSI"

print(dict)

#if else condition in python with working examples

greeting = "Good Morning"
if greeting == "Good Morning":
    print ("condition matches")
    print ("second line")
else:
    print("condition does not match")
print ("if else condition code is completed")



#for loop

obj= [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# sum of first natural numbers  1+2+3+4+5 = 15
summation = 0
for j in range(1,6):
    summation = summation + j
    print(summation)
print("*****************************************")
for k in range(1, 10, 5):
    print(k)

print("****************SKIPPING FIRST INDEX**************************")

for m in range(10):
    print(m)

# while loops

it = 10

while it >1:
    if it == 9:
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print ("while loop execution is done")

# In Python, function is a group of related statements that perform a specific task.

def GreetMe():
    print("Good Morning")


GreetMe()

