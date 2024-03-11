import csv
t_data = ['Name', 'Age', 'City'], ['Alice',30, 'New York'], ['Bob', 25, 'Los Angeles']

with open('data.csv', 'w') as csvfile:
    write_v = csv.writer(csvfile)
    print(write_v)
    for data in t_data:
        write_v.writerow(data)
