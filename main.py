'''
A simple script created to determine the ratio of medals won in a competition to population of that country. Written in Python, the
script reads a csv file called "input.csv" and scrapes wikipedia for the population data of that country. It then calculates the
ratio of medals to population and dislays that data in a graph.

Martin Harvey - 2018
Released under the MIT License
'''
from findPop import findPop
import matplotlib.pyplot as plt #matplotlib is used for creating and displaying the graph
import csv # csv is a standard library module and is used for reading the input.csv file


#Initialising any variable/lists
countryName = [] #Contains the names of each country loaded in
medalCount = [] #Contains the medal count fot each country
population = [] #Contains the population data for each country
totRatio = [] #Contains the medal to population ratio for each country

'''
We are now loading in the .csv file containg the country names and the medal counts in the order <countryName><medalCount>. Each
country has its own line in the file.

The script then loops through each line assigning the first part of each line to the countryName list and the the second part to the
medalCount list.
'''
with open('input.csv') as inputFile: #Opens input.csv and assigns it to inputFile. Initialises a loop for each line of inputFile
    inputRow = csv.reader(inputFile) #Using he reader function in the csv module, each line is split up according to the default csv delimiters
    for row in inputRow: #As inputRow is a list, we can iterate through it
        countryName.append(row[0]) #Append to the end of countryName the first element of row
        medalCount.append(int(row[1])) # Append to the end of medalCount the second element of row in type integer

for x in range(len(countryName)): #Loop through each element of countryName
    population.append(findPop(countryName[x]))


for x in range(len(countryName)): #We loop through countryName again
    '''
    We get the medalCount of a certain country and divide it by the population of that country. We multiply this by 100,000 as matplotlib can then create
    an easier to understand graph and round it to two decimal places. This value is added to the of totRatio, a list of medal to population ratios.
    '''
    totRatio.append(round(medalCount[x]/population[x] * 100000, 2))

'''
We now use matplotlib to create the bar graph. Creating bargraphs using matplotlib in python require the pyplot library, which we shortened to plt when we
imported it earlier. The bar() function uses the following syntax:
plt.bar(x_axis, y_axis, width_of_bars, color_of_bars)
'''
plt.bar(countryName, totRatio, 1/1.5, color = "green")
plt.show() #Show the bargraph in a new window. matplotlib uses TKinter to display the window and graph.
