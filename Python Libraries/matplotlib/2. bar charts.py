"""
Note:- 
- We can overlay multiple type of charts (like bar charts, line charts etc.) on one another 
- when plotting data the x axis and y axis data must have the same length.
"""


from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# Ages 18 to 55
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]     

# Median All Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(ages_x, dev_y, color= "#444444", linestyle= "-" , label = "All Devs")

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, color= "#5a7d9a", linewidth= 3 ,linestyle= "-", label = "Python")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color= "#adad3b", label = "JavaScript")

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