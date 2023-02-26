# Following section is old version

# temperature = int(101.2)
# print(temperature)
# print(type(temperature))
 
# print("----------")

# temperature = float(101.2)
# print(temperature)
# print(type(temperature))
 
# print("----------")

# temperature = bool(101.2)
# print(type(temperature))
 
# print("----------")

# temperature = str(101.2)
# print(type(temperature))

# Following section is new version

temperature = 101.2

def show_temp_type(temp):
    print(temp)
    print(type(temp))
    print("---------------")

show_temp_type(int(temperature))
show_temp_type(float(temperature))
show_temp_type(bool(temperature))
show_temp_type(str(temperature))
