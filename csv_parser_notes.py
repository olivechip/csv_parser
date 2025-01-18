import csv

print('running')

# reading csv files
with open('data.csv', 'r') as csv_file:
        
    # create DictReader object in memory w/ all data
    csv_reader = csv.DictReader(csv_file)
    
    # print all lines
    for line in csv_file:
        print(line)
    
    # writing csv files
    with open('new_file', 'w') as new_file:
        
        # field names must be provided, can be removed according to needs
        fieldnames = ['first_name', 'last_name', 'salary']
        
        # create DictWriter object in memory for writing
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        
        # writes the header
        csv_writer.writeheader()
        
        csv_file.seek(0)
        csv_reader = csv.DictReader(csv_file)
        
        # write rows to new file
        for line in csv_reader:
            csv_writer.writerow(line)