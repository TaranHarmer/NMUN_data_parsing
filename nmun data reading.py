import csv
data = []
continent = {}
testPov = 0
globalPercent = 0
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pov = row['FactValueNumeric']
        cont = row['ParentLocation']
        data.append(pov)
        globalPercent += float(pov)
        if not(cont in continent):
            continent[cont] = [0,0]
        continent[cont][0] += 1
        continent[cont][1] += float(pov)

for cont in continent:
    continent[cont][1] /= continent[cont][0]
    testPov += continent[cont][1]
print(continent)
print(testPov/len(continent))
print(globalPercent)
print(f'Data Length = {len(data)}| Global Percentage = {globalPercent/len(data)}')
        
