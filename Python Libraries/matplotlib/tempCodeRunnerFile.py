from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Ages 18 to 55
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]     


# Median All Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(ages_x, dev_y, color= "#444444", linestyle= "-" , label = "All Devs")

#---------------------------------
#FORMATTING

#Labeling X and Y axis
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

#Adding title to the plot
plt.title("Median salary (USD) by age")       

#Adding Legend to the plot
plt.legend()

#Adding Grids to the graph background
plt.grid(True)           

#-------------------
plt.show()