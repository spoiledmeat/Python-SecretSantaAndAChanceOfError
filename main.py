#Author: James Sweeten Jr.
#NOTE: This version is the version that was used for a real
#      game in 2016, but note that it is flawed! On extensive testing,
#      I found that there is around a 5% chance that someone 
#      will be matched incorrectly or not at all.
#NOTE: If you want a fully working, easier to understand, but also boring version,
#      go back to my Github and get it :)

#// Uncomment this line when you want to do a real run
#import yagmail #Library for sending email
import random

#// When you want to do a real run, fill and uncomment this line!
#yag = yagmail.SMTP('[Your Email Address Here]','[Your Email Password Here')

#Elf class. These are the people!
class Elf:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.hasPicked = False
        self.wasPicked = False

#NPole class. Where else should secret santa take place? Matches up the elves.
class NPole:
    def __init__(self):
        self.elves = []

    def addElf(self, name, email):
        elf = Elf(name, email)
        self.elves.append(elf)
    def numElves(self):
        return len(self.elves)
        
	#// Method intended to shuffle elves arround randomly
    def shuffleElves(self, n):
        for x in range(0, n):
        
            # Think of two random positions in the array
            l_elf_one_index = random.randint(0, len(self.elves)-1)
            l_elf_two_index = random.randint(0, len(self.elves)-1)
        
            # Prevent the two positions from being the same!
            while (l_elf_two_index == l_elf_one_index):
                l_elf_two_index = random.randint(0, len(self.elves)-1)
        
            # Hold the value of the first index
            l_placeHolder = self.elves[l_elf_one_index]
        
            # Change the value of the first index to that of the second
            self.elves[l_elf_one_index] = self.elves[l_elf_two_index]
        
            # Change the value of the second index to what the first was originally
            self.elves[l_elf_two_index] = l_placeHolder
        
            # The two values have exchanged places.

	# Method intended to match up elves and perform error checking. LOL it's bad.
    def pullMatch(self):
        
        print("Self-Checking Statuses of Elves")
        if (self.checkAllClear() == True):
            print("All elves matched. No need to search.")
            return -1
        print("There's at least one unmatched elf. Searching...")
        # Think of two random positions in the array
        l_elf_one_index = random.randint(0, len(self.elves)-1)
        l_elf_two_index = random.randint(0, len(self.elves)-1)
        print ("Picked two elves at random")

        # Make sure the pickee hasn't been already picked
        n = 0
        x = 0
        while (self.elves[l_elf_two_index].wasPicked == True):
            
            print ("Elf 2 was picked already")
            l_elf_two_index = random.randint(0, len(self.elves)-1)
            print ("Picked another Elf 2 at random")
            n += 1
            # If we've been searching randomly for too long, look sequentially for
            # an unpicked Elf
            found = False
            if (n > 5):
                print ("We've been picking at random too long. Now checking sequentially.")
                for x in range(0, len(self.elves)-1):
                    if (self.elves[x].wasPicked == False):
                        print ("We found an unpicked Elf!")
                        l_elf_two_index = x
                        print ("Set Elf 2 to the unpicked Elf.")
                        found = True
                        break
                if (found == True): #Bugfix: Had to break twice! 
                    break
                #No unpicked Elf found.    
                print ("We could not find an unpicked Elf 2. This should mean that everyone was picked.")
                return -1
                
        print ("Now to find an Elf 1 that hasn't picked.")
        # Make sure the picker hasn't already picked someone
        n = 0
        x = 0
        while (self.elves[l_elf_one_index].hasPicked == True):
            print ("Elf 1 picked someone already.")
            l_elf_one_index = random.randint(0, len(self.elves)-1)
            print ("Picked another Elf 1 at random")
            n += 1
            # If we've been searching randomly for too long, look sequentially for
            # an Elf that hasn't picked
            found = False
            if (n > 5):
                print ("We've been picking at random too long. Now checking sequentially.")
                for x in range(0, len(self.elves)-1):
                    if (self.elves[x].hasPicked == False): #Fixed was -> has
                        print ("We found an Elf that hadn't picked!")
                        l_elf_one_index = x #Fixed two -> one
                        found = True
                        break
                if (found == True):
                    break
                #No hasn't-picked Elf found    
                print ("We could not find an Elf 1 that hasn't picked. This should mean that everyone picked someone else.")
                return -1
                
        print ("Okay, we should have two elves that are compatible.")
        # Prevent the two positions from being the same!
        if (l_elf_two_index == l_elf_one_index):
            print ("They're the same. Not matching them.")
            return 2
            
        # DO THE EMAIL THING -- Uncomment the line below (and modify if you want) when you want to do a real run
        #yag.send(self.elves[l_elf_one_index].email, "2016 Secret Santa [Sent by Program]", "Congratulations "+ str(self.elves[l_elf_one_index].name) + ", the person you will be getting a gift for has been randomly chosen! That person is " + str(self.elves[l_elf_two_index].name))

        print ("Let's match them together.")    
        self.elves[l_elf_one_index].hasPicked = True
        self.elves[l_elf_two_index].wasPicked = True

        
        
        return 1
    
	#// Method intended to check that each elf has been given another elf, and has been assigned to another.
    def checkAllClear(self):
        for x in range(0, len(self.elves)-1):
            if (self.elves[x].hasPicked == False or self.elves[x].wasPicked == False):
                return False
        return True
		
	#// Method intended to completely reset the matching.
    def reset(self):
        #Reset the Pole!        
        for i in range(0, len(pole.elves) - 1):
            pole.elves[i].hasPicked = False
            pole.elves[i].wasPicked = False


        

pole = NPole()

# Add the Elves
# Create an elf for each person in your secret santa game
pole.addElf("Placeholder Johnson", "Placeholder@Johnson.com")
pole.addElf("Steve Buscemi","TheBusc@stevebuscemi.com")

# Note: as I'm looking back at this in 2017, I'm noticing more mistakes.
#		For example, the line that sends the emails is in NPole.pullMatch.
#		This happens BEFORE I check that everyone's matched up alright.
#		2/10 logic. 3/10 with rice. 
#		Again, I don't recommend using this version.


# Perform a matching run
while (True):   
	pole.shuffleElves(5)
	matchResult = pole.pullMatch()
	
	# If all the Elves have been matched, stop trying to match people    
	if (matchResult == -1):
		print ("MR = -1")
		# If we really have matched all the elves, do the analysis
		if pole.checkAllClear() == True:
			print ("All Clear")
			break
		# If we haven't matched all the elves, reset and keep going.
		pole.reset()
		print ("Not Clear")

# The below code is for testing. I've had this secret santa matching program
# run literally millions of times. It's bad. I made a good version-- it's on my github! 
"""
desiredRunCount = 1
currentRunCount = 0

total_failures = 0
num_failed_runs = 0
failed_runs = []
avg_err_count = 0

while (desiredRunCount - 1) >= currentRunCount:
    
    currentRunCount += 1
    #Match the Elves
    counter = 0
    
    # Perform a matching run
    while (True):   
        pole.shuffleElves(5)
        matchResult = pole.pullMatch()
        
        # If all the Elves have been matched, stop trying to match people    
        if (matchResult == -1):
            print ("MR = -1")
            # If we really have matched all the elves, do the analysis
            if pole.checkAllClear() == True:
                print ("All Clear")
                break
            # If we haven't matched all the elves, reset and keep going.
            pole.reset()
            print ("Not Clear")
    

    problems = 0
    for i in range(0, len(pole.elves) - 1):
        if pole.elves[i].hasPicked == False:
            print("Oh no, "+str(pole.elves[i].name)+" never picked another!")
            problems += 1
        if pole.elves[i].wasPicked == False:
            print("Oh no, "+str(pole.elves[i].name)+" was never picked!")
            problems += 1

    if problems > 0:
        print("We have "+str(problems)+" problems. On run "+str(currentRunCount));
        total_failures += problems
        num_failed_runs += 1
        failed_runs.append(num_failed_runs)
        avg_err_count += problems
    print ("_")
    pole.reset()



print("TESTING COMPLETED. "+str(desiredRunCount)+" ITERATIONS.")
print("Found "+str(num_failed_runs)+" failed runs.")
print("Found "+str(total_failures)+" total elves with something False.")
perc_of_failure = float(num_failed_runs)/desiredRunCount *100
print("That's a "+str(perc_of_failure)+" percent chance of failure.")
if num_failed_runs != 0:
    avg_err_count /= float(num_failed_runs)
if num_failed_runs == 0:
    avg_err_count = 0
print("Average Error Count is "+str(avg_err_count))
"""

