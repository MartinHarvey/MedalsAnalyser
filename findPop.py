import requests # requests is used to fetch the wikipedia pages we scrape for population data

def findPop(countryN):
    countryWiki = requests.get('http://en.wikipedia.org/wiki/' + countryN, params={'action': 'raw'})
    countryWiki = countryWiki.text #The requests object at countryWiki is translated into plaintext and assigned back to countryWiki
    for lines in countryWiki.splitlines(): #A loop is Initialised that iterates through each line of countryWiki
        if "population_census" in lines: #If "population_census" is found in the string 'line'
            line = lines.split("=") # We split line by '=' (i.e. population_census = 1,231,231 {})
            line = line[1].split("{") # We split the second part of line by '{' (i.e. 1,231,231 {})
            line = line[0].split('<') #We split the first part of line by '<' if such a character exists (i.e. 1,231,231 <ref>)
            '''
            We get the rid of the commas in the string in the first part of line and convert it to an int (like "1,231,231" ----> 1231231), before
            returning it.
            '''
            return_val = int(line[0].replace(',', ''))
            return return_val
