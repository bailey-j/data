#section 1

f = open("data.csv","r")        #accessing the file
print(f)                        #display the I/O header   
stations = f.read()             #assign the contents of the file to the variable stations
print(stations)                 #display the contents

#section 2

station_list = stations.split('\n')     #split the stations list by  the new line character (by line)
first_five = station_list[:5]           # create a new list of 5 items which is a sublist of station_list

#section 3
nested_list = []                      #initialise nested_list

for x in station_list:                #iteration statement with x as iterator variable
  comma_list = x.split(',')           #split each row and assign this newly split row to variable comma_list
  nested_list.append(comma_list)      #append each new split row to nested_list

print(nested_list[0:5])               #display the first five elements of nested_list

#section 4
rainfall_list = []

for row in nested_list;
  station = row[0]
  rain = float(row[1])
  float_list = [station, rain]
  rainfall_list.append(float_list)
  
print(rainfall_list[:5])

#section 5
less_than_60 = []
for x in rainfall_list:
  if x[1] < 60
    less_than_60.append(x[0])
print(less_than_60)

f.close()
