print("Helo word")# = conosle.log("Helo word");
#comment in python

#variables
name = "mauricio" #let name = 'mauricio';
name = 12 #let name = 'mauricio';

print(name)
age = 100
#if else statement

if age <100:
    print('dont orry your not that old')
    print("im not into the if statement")
    #this is on the same level
    #also on the same level
elif age == 100:
    print("wow youre a century")
else:
    print("well seemsthat youre a little bit old")

#function(){}
def say_Hello():
    print("Hello there")

#call function
say_Hello()

print("my age is "+str(age)+" years old")

#array -- list

colors = ["yellow","green","blue"]

print(colors)
#add
colors.append("pink")

print(colors)
#remove

colors.remove("yellow")

print(colors)
#remove using index
colors.pop(0)
print(colors)

print(colors[1])

#for(let i=0; i<colors.length;i++){}
for color in colors:
    print(color)

#Diccionary

me = {"first_name":"Mauricio",
      "last_Name":"Navarro",
      "age":26
}

print(me)
print(me["first_name"])
me["first_name"] = "Adrian"
print(me["first_name"])
print(me)