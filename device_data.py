import re
import csv
import itertools
import os.path
import time

def max_consumption_properties(csv_name):

    f = open(csv_name)
    csv_f = csv.reader(f)

    location = []
    device_name = []
    consumption = []
    time = []
    rate = []

    for row in csv_f:
        location.append (row[0])
        device_name.append (row[1])
        consumption.append (row[2])
        time.append (row[3])
        rate.append (row[4])
   
    consumption_numbers = (consumption[1:])       
    consumption_float = list(map(float, consumption_numbers))
   
    index_val = (consumption_float.index (max(consumption_float)))+1

    max_location = (location [index_val])
    max_machine = (device_name [index_val])
    max_consumption = (consumption [index_val])

    rate_numbers = (rate[1:])
    rate_float = list(map(float, rate_numbers))

    fixed_rate = float (rate_float[0])
    max_cost = fixed_rate * float(max_consumption)

    return ([max_machine, max_location, max_cost/1000])

def suggestion (csv_name):
  
    f = open(csv_name)
    csv_f = csv.reader(f)
  
    hour = []
    location = []
    device_name = []
    consumption = []

    for row in csv_f:
        location.append (row[0])
        device_name.append (row[1])
        consumption.append (row[2])
        hour.append (row[5])
    
    consumption_numbers = (consumption[1:])       
    consumption_float = list(map(float, consumption_numbers))

    index_val = (consumption_float.index (max(consumption_float)))+1  
    max_machine = (device_name [index_val])
    max_consumption = (consumption [index_val])
  
    on_time = (13.2 * float(max_consumption)/1000)
    mid_time = (9.4 * float(max_consumption)/1000)
    off_time = (6.5 * float(max_consumption)/1000)
  
    if (int(hour[1]) >= 11 and int(hour[1]) <=16):
        suggest = ["You are using " + max_machine + " in the " + location [index_val] + " during on-peak hours. Consider changing use to after 7:00 PM. Your current cost is: " + str(13.2 * float(max_consumption)/1000) + " cents per hour. You would save " + str (on_time - off_time) + " cents per hour by using " + max_machine + " after 7:00 PM."]
  
    elif (int (hour[1]) >= 5 and int (hour[1]) <=19):
        suggest = ["You are using " + max_machine + " in the " + location [index_val] + " during mid-peak hours. Consider changing use to after 7:00 PM. Your current cost is: " + str (9.4 * float(max_consumption)/1000) + " cents per hour. You would save " + str (mid_time - off_time) + " cents per hour by using " + max_machine + " after 7:00 PM."]
    
    elif (int (hour[1]) >=7 and int (hour[1]) <11):
        suggest = ["You are using " + max_machine + " in the " + location [index_val] + " during mid-peak hours. Consider changing use to after 7:00 PM. Your current cost is: " + str(9.4 * float(max_consumption)/1000) + " cents per hour. You would save " , (mid_time - off_time) , " cents per hour by using " + max_machine + " after 7:00 PM."]
  
    return suggest

def devices_in_use (csv_name):

    f = open(csv_name)
    csv_f = csv.reader(f)

    device_names = []

    for row in csv_f:
        device_names.append (row[1])
  
    return (device_names[1:])


# main function 

while True:
    for fname in os.listdir('.'):
        if fname.endswith('.csv') and "device_data" in fname:
            print("File exists: ", fname)

            # do stuff on the file
            with open('devices_in_use.csv', mode='w') as parsed_file:
                parsed_writer = csv.writer(parsed_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                parsed_writer.writerow ("[Devices in use]")
                parsed_writer.writerow(devices_in_use(fname))
                print ("Your file has been created")

            # ----------
            with open('max_consumption.csv', mode='w') as parsed_file:
                parsed_writer = csv.writer(parsed_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                parsed_writer.writerow (["Name", "Location", "Cost per Hour (cents)"])
                parsed_writer.writerow(max_consumption_properties(fname))
                print ("Your file 2 has been created")
                
            with open('suggestion.csv', mode='w') as parsed_file:
                parsed_writer = csv.writer(parsed_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                parsed_writer.writerow (["Suggestion"])
                parsed_writer.writerow(suggestion(fname))
                print ("Your 3 has been created")

                os.remove(fname)
                print(fname + " has been removed") 
                brk = True
            break

        
    

