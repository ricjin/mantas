# Create dictionary of swimmer
# Name => best time
besttimes = {}
import csv

includeFirst = True

with open('input.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    previousEvent = ""
    besttime = 10000

    for row in csv_reader:
        
        key = row["name"].strip()
        event = row["event"].strip()
        record = row["time"].strip()

        #convert record to seconds
        arr = record.split(':')

        if (len(arr) > 1):
            record =  float(arr[0])*60 + float(arr[1])
        else:
            record = float(arr[0])


        if key in besttimes:
            if (previousEvent == event):
                if (record < besttime):
                    besttime = record
                    besttimes[key] += 1
            else:
                if (includeFirst):
                    besttimes[key] += 1
                besttime = record        
        else:
            besttimes[key] = 0
            besttime = record
        
        previousEvent = event     
        

    with open('output.csv', 'w') as f:
        for key in besttimes.keys():
            f.write("%s,%s\n"%(key,besttimes[key]))