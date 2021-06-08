import numpy as np
import time
import csv

start_time = time.time()

f = open('sample.csv', errors='ignore')
csv_f = csv.reader(f)   
np.data = []

for row in csv_f: 
	np.data.append(row)
f.close()

#print (np.data[1:])

def convert_row(row):
    return """
    <azure:Movie> 
    <azure:ID>%s</azure:ID>
    <azure:name>%s</azure:name>
    <azure:insert_date>%s</azure:insert_date>
    <azure:obtain_price>%s</azure:obtain_price>
    <azure:quantity>%s</azure:quantity>
    <azure:room_ID>%s</azure:room_ID>
    <azure:actorID>%s</azure:actorID>
    </azure:Movie>""" % (row[0], row[1], row[2], row[3], row[4], row[5], row[6])

with open('import.xml', 'w') as f: f.write('\n'.join([convert_row(row) for row in np.data[1:]]))

print("--- %s seconds ---" % (time.time() - start_time))
