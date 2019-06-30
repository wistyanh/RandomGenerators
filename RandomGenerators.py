#Random Business Name Generator
from random import*

listA = ["Bippi", "Boppy", "Loofah", "Hungry", "Humpty", "Vegan"]
listM = ["&", "is", "loves"]
listB = ["Hippo", "Blizzie", "Dumpty", "Kale", "Potato"]

RandomIndexA = randint(0, len(listA)-1)      #sets the range for index
RandomIndexM = randint(0, len(listM)-1)
RandomIndexB = randint(0, len(listB)-1)
#To see business name: print("Your business name is: " + listA[RandomIndexA] + " " + listM[RandomIndexM] + " " + listB[RandomIndexB])


#Menu Generator
sides = ["Egg Rolls", "Fried Rice", "Salad", "Onion Rings", "French Fries", "Kale Chips"]
mainCourses = ["Pho", "Bun Bo Hue", "Pasta", "Stir Fried Shrimp", "Chicken Cordon Bleu Wrap"]
desserts = ["Yogurt", "Cheesecake", "Red Velvet Cupcake", "Fruits", "Boba", "Ice Cream"]

aRandomIndexA = randint(0, len(sides)-1)
aRandomIndexM = randint(0, len(mainCourses)-1)
aRandomIndexB = randint(0, len(desserts)-1)

print("Hello ladies and gentlemen, welcome to " + (listA[RandomIndexA] + " " + listM[RandomIndexM] + " " + listB[RandomIndexB]) + ".")
print("Today's menu is: " + sides[aRandomIndexA] + ", " + mainCourses[aRandomIndexM] + ", & " + desserts[aRandomIndexB] + ".")
