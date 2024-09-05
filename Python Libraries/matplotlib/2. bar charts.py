import csv
from collections import Counter   # to count the occurance of each Language in the csv data
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

#---------------------------------
#Reading and Organising the data before we plot it
with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)       #Reading file as dictionary

    language_counter = Counter()              #It will help us count the occurance of each language in complete data

    # We will create a dictionary named "language_counter", with key = "languages" , value = "count of occurance in the complete data"
    for row in csv_reader:         #Iterating through each row
        language_counter.update(row["LanguagesWorkedWith"].split(";"))       


#Now separating "languages" and "count " into separate list , so we can make it x and y axis of graph
languages = []
popularity = []

for item in language_counter.most_common(15):        #We want most common 15 languages only from complete data 
    languages.append(item[0])
    popularity.append(item[1])


#-------------------------------
#Plotting the data


#Reversing the data 
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity, label = "All languages")

#---------------------------------
#FORMATTING

#Labeling X and Y axis
plt.xlabel("Number of people who use")
# plt.ylabel("languages")

#Adding title to the plot
plt.title("Most Popular Languages")       

#Adding Legend to the plot
plt.legend()

#Adding Grids to the graph background
plt.grid(True)           

#It will compress the graph into smaller size
plt.tight_layout()
#-------------------
plt.show()        