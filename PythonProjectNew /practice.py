# %% [markdown]
# 3-1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.

# %%
Names =[" Osi", "Tariq", "Leke", "Jaiye"]
print(Names[0])
print(Names[3])


# %% [markdown]
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the 
# person’s name

# %%
Names =[" Osi", "Tariq", "Leke", "Jaiye"]
for invites in Names:
    print(f"I am friends with {invites}")


# %% [markdown]
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”
# 

# %%
Brands = ["Chanel", "Prada", "Fendi", " Louis Vuitton"]
chanel = "I absoluley love "+ Brands[0].title()+"."
Prada = Brands[1]+","+"is one of my favorite brands"+ "."
LV = "Life is amazing"+","+ Brands[3] +" makes it better"+ "."
print(Prada)
print(chanel)
print(LV)

# %% [markdown]
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting 
# them to dinner.

# %%
GuestList = ["Mom", "lilly", "Osi"]
message = "Dear "+ GuestList[0]+ ","+ "youre invited for dinner"+ "."
print(message)
message2 = GuestList[2]+ " you are formaly invited to dinner"+ "."
print(message2)
message3 = "No invite for you "+ GuestList[1]+ " sorry"+ "!"
print(message3)


# %% [markdown]
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the 
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still 
# in your list.

# %%
GuestList = ["Mom", "lilly", "Osi"]
GuestList.append('Jiaye')
print(GuestList)
del GuestList[1]
GuestList.insert(1, "Bob")
print(GuestList)
message = " Hiii "+ GuestList[1]+ " youre invited to Dinner"+ ("!")
print(message)
#only did the message that had the new invitee, im not writting a bunch of new invites


# %% [markdown]
# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a 
# bigger dinner table.
# •	 Use insert() to add one new guest to the beginning of your list.
# •	 Use insert() to add one new guest to the middle of your list.
# •	 Use append() to add one new guest to the end of your list.
# •	 Print a new set of invitation messages, one for each person in your list.

# %%
GuestList = ["Mom", "lilly", "Osi", "Bob"]
GuestList.insert(0, "Bianca")
GuestList.insert(3, "Tariq")
GuestList.append("Leke")
print(GuestList)
#no wayyyy im doing 3 more invites 


# %% [markdown]
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.
# •	 Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# •	 Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print 
# a message to that person letting them know you’re sorry you can’t invite 
# them to dinner.
# •	 Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# •	 Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end 
# of your program.

# %%
GuestList = ["Mom", "lilly", "Osi", "Bob"]
print(" sorry guys, i can only invite 2 people from my Guestlist.")
print (GuestList)
popped_Guestlist = GuestList.pop()
print(GuestList)
print(popped_Guestlist)
popped_Guestlist2 = GuestList.pop(0)
firstG = GuestList.pop(0)
print( 'Hey '+ firstG + " I have to take back my invite, sorry!")
secondG = GuestList.pop(0)
print("Hey " + secondG + " I have to take back my invite, sorry!")








# %% [markdown]
# 3.8. Seeing the World: Think of at least five places in the world you’d like to 
# visit.
# •	 Store the locations in a list. Make sure the list is not in alphabetical order.
# •	 Print your list in its original order. Don’t worry about printing the list neatly, 
# just print it as a raw Python list.
# •	 Use sorted() to print your list in alphabetical order without modifying the 
# actual list.
# •	 Show that your list is still in its original order by printing it.
# •	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
# •	 Show that your list is still in its original order by printing it again.
# •	 Use reverse() to change the order of your list. Print the list to show that its 
# order has changed.
# •	 Use reverse() to change the order of your list again. Print the list to show 
# it’s back to its original order.
# •	 Use sort() to change your list so it’s stored in alphabetical order. Print the 
# list to show that its order has been changed.
# •	 Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.

# %%
Travel = ["Rio", "Tanzania", "Jamaica", "Chile", "Seychells"]
print(Travel)
Travel.sort()
print(Travel)
Travel.reverse()
print(Travel)

# %% [markdown]
# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
# through 3-7 (page 46), use len() to print a message indicating the number 
# of people you are inviting to dinner

# %%
Guests = ["Tariq","Leke","Osi","Mom","Jaiye"]
NumofG = "Hi everyone "+ "," + "there will be a total of" ,len(Guests) ,"guets at dinner tonight" +"."
print(NumofG)
len(Guests)
print(len(Guests))
#save


