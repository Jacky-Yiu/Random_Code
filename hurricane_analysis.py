# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
converstion={'M':1000000, 'B':1000000000}

def damage_update(lst):
  new_lst=[]
  for damage in lst:
    if damage == 'Damages not recorded':
      new_lst.append(damage)
    else:
      prefix=damage[-1]
      new_lst.append(float(damage.strip('MB'))*converstion.get(prefix))
  return new_lst    

damages=damage_update(damages)
#print(damages)


# write your construct hurricane dictionary function here:
def hur_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  new_dict={}
  for i in range(len(names)):
    name_dict={}
    name_dict["Name"]=names[i]
    name_dict["Month"]=months[i]
    name_dict["Year"]=years[i]
    name_dict["Max Sustained Wind"]=max_sustained_winds[i]
    name_dict["Areas Affected"]=areas_affected[i]
    name_dict["Damage"]= damages[i]
    name_dict["Death"]=deaths[i]
    new_dict[names[i]] = name_dict
  
  return new_dict
  
dictionary = hur_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

#print(dictionary["Cuba I"])

# write your construct hurricane by year dictionary function here:
def hur_dict_year(dictionary):
  year_dict={}
  name_list=list(dictionary.keys())
  year_list=[]

  for name in name_list:
    year_list.append(dictionary.get(name).get("Year"))

  for year in year_list:
    lst = []
    for name in name_list:
      if dictionary.get(name).get("Year") == year:
        lst.append(dictionary.get(name))
    year_dict[year]=lst
  
  return year_dict


year_dict = hur_dict_year(dictionary)
#print(year_dict.get(1932))


# write your count affected areas function here:
def hur_dict_area(dictionary):
  area_dict={}
  name_list=list(dictionary.keys())
  area_list=[]

  for name in name_list:
    areas = dictionary.get(name).get("Areas Affected")
    for area in areas:
      if area not in area_list:
        area_list.append(area)
  #print(area_list)
  
  for item in area_list:
    counter=0
    for name in name_list:
      areas_affected = dictionary.get(name).get("Areas Affected")
      for area in areas_affected:
        if area == item:
          counter+=1
    
    area_dict[item]=counter
  
  return area_dict

area_dict=hur_dict_area(dictionary)
#print(area_dict["United States Gulf Coast (especially Florida Panhandle)"])


# write your find most affected area function here:
def most_affected_area(area_dict):
  area_list=list(area_dict.keys())
  max_area=''
  max_value=0

  for area in area_list:
    if area_dict[area] > max_value:
      max_area = area
      max_value = area_dict[area]
  
  return f"The area affected by the most hurricanes is {max_area}, it was hit {max_value} times."

#print(most_affected_area(area_dict))


# write your greatest number of deaths function here:
def most_death(dictionary):
  name_list=list(dictionary.keys())
  max_name=''
  max_death=0

  for name in name_list:
    death = dictionary[name]["Death"]
    if death > max_death:
      max_name = name
      max_death = death
  
  return f"The hurricane that caused the greatest number of deaths is {max_name}, it killed {max_death} people."

#print(most_death(dictionary)) 


# write your catgeorize by mortality function here:
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def death_rate(dictionary):
  death_dict={}
  name_list=list(dictionary.keys())

  for i in range(6):
    lst = []
    for name in name_list:
      death=dictionary.get(name).get("Death")
      try:
        if death >= mortality_scale[i] and death < mortality_scale[i+1]:
          lst.append(dictionary.get(name))
      except KeyError:
        if i==4 and mortality_scale[i] and death >= mortality_scale[i-1]:
          lst.append(dictionary.get(name))
        elif i == 5 and death > 10000:
          lst.append(dictionary.get(name))

    death_dict[i]=lst
  
  return death_dict


death_dict = death_rate(dictionary)

#for i in range(6):
  #print(f"{i}: {len(death_dict[i])}")



# write your greatest damage function here:
def most_damage(dictionary):
  name_list=list(dictionary.keys())
  max_name=''
  max_damage=0.0

  for name in name_list:
    damage = dictionary[name]["Damage"]
    if damage != 'Damages not recorded':
      if damage > max_damage:
        max_name = name
        max_damage = damage

  
  return f"The hurricane that caused the greatest number of damage is {max_name}, it cost ${max_damage}"


# write your catgeorize by damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def damage_rate(dictionary):
  damage_dict={}
  name_list=list(dictionary.keys())

  for i in range(6):
    lst = []
    for name in name_list:
      damage=dictionary.get(name).get("Damage")
      if damage != 'Damages not recorded':
        try:
          if damage >= damage_scale[i] and damage < damage_scale[i+1]:
            lst.append(dictionary.get(name))
        except KeyError:
          if i == 4 and damage_scale[i] and damage >= damage_scale[i-1]:
            lst.append(dictionary.get(name))
          elif i == 5 and damage > 50000000000:
            lst.append(dictionary.get(name))

    damage_dict[i]=lst
  
  return damage_dict


damage_dict = damage_rate(dictionary)
#for i in range(6):
  #print(f"{i}: {len(damage_dict[i])}")


