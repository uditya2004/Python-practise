from matplotlib import pyplot as plt


"""
- color= "k"         -> black color
- color= "b"         -> blue color
- color= "HEXVALUE"  -> can pass hex code as well
- linestyle = "-"    -> solid line   (by defalt it is set to solid line)
- linestyle = "--"   -> dashed line 
- linewidth= 3       -> width of the line (by default it is 1)
- label = "TEXT"     -> Used for Adding Legend
- marker = ""        -> Add points in graph 

Ref:- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

Note:- Lines are ploted in the ordere , it is coded (i.e 1st -> Python, 2nd -> Javascript, 3rd -> All devs)

"""
#------------------------------
# print(plt.style.available)       # Run this to get all the available styles
# plt.xkcd()           #This will make your plot look like it's hand drawn

plt.style.use("fivethirtyeight")


ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]                        # Ages on x axis
                  

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.plot(ages_x, py_dev_y, color= "#5a7d9a", linewidth= 3 ,linestyle= "-", label = "Python")


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(ages_x, js_dev_y, color= "#adad3b", label = "JavaScript")


# Median All Developer Salaries by Age
dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]         #Salary on y axis
plt.plot(ages_x, dev_y, color= "#444444", linestyle= "--" , marker= "." , label = "All Devs")       

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
plt.grid(True)             # some plt.style has it's grid by default

#-------------------
plt.show()         # printing the plot