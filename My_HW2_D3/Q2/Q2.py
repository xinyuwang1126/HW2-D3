#!/usr/bin/env python
import csv
f = open('nepal.csv')
csv_f = csv.reader(f)
for row in csv_f:
        print row[0]+",",row[1]+",",row[2]+",",row[3]+",",row[4]
