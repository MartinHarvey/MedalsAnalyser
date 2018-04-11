import matplotlib.pyplot as plt
import csv
import bs4 as bs
import requests
countryName = []
medalCount = []
population = []
popMedIndex = []

with open('input.csv') as inputFile:
    inputRow = csv.reader(inputFile)
    for row in inputRow:
        countryName.append(row[0])
        medalCount.append(int(row[1]))
    

for x in range(len(countryName)):
    print(countryName[x])
    found = False
    countryWiki = requests.get('http://en.wikipedia.org/wiki/' + countryName[x], params={'action': 'raw'})
    countryWiki = countryWiki.text
    #print (countryWiki)
    for lines in countryWiki.splitlines():
        if "population_census" in lines and found == False:
            line = lines.split("=")
            line = line[1].split("{")
            line = line[0].split('<')
            population.append(int(line[0].replace(',', '')))
            found = True
            print(countryName[x] + ": " + str(population[x]))



print(countryName)
print(medalCount)
print(population)

for x in range(len(countryName)):
    popMedIndex.append(round(medalCount[x]/population[x] * 100000, 2))

print(popMedIndex)

plt.bar(countryName, popMedIndex, 1/1.5, color = "green", antialiased = True)
plt.show()
