import csv

with open('data.csv', 'r') as csvfile:
    read_v = csv.reader(csvfile)
  #  print(read_v)
    for row in read_v:
       print(row)