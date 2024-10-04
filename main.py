# steam level calculator

import math

xpPerBadge = 100
badgesPerCardType = 5

# user input
print("Steam level calculator")
xpPerLevel = int(input("What is the xp required per level? "))
levelsDesired = int(input("How many times do you want to level your profile? "))
costOfBadge = float(input("according to steamcardexchange.net, how much does the badges cost on average? "))

# calc xp and badge sets needed
xpNeeded = xpPerLevel * levelsDesired
badgesNeeded = xpNeeded / xpPerBadge

# report back to user
print(f"You need {xpNeeded} to gain {levelsDesired} levels")
print(f"You need {badgesNeeded} badges to get to {levelsDesired}")

totalCost = math.ceil(costOfBadge * badgesNeeded)

print(f"if the average badge price is {costOfBadge}, you will need to spend roughly ${totalCost}.")