import requests
from bs4 import BeautifulSoup

def get_drivers_championship(year):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
            points = row.find_all('td')[5].get_text(strip=True)
            position = row.find_all('td')[1].get_text(strip=True)
            formatted_data.append({
                'position': position,
                'driver': full_name, 
                'points': int(points)
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_drivers_championship_no_points(year):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
            position = row.find_all('td')[1].get_text(strip=True)
            formatted_data.append({
                'position': position,
                'driver': full_name, 
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_driver_at_position(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[int(position)]  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts)
            points = row.find_all('td')[5].get_text(strip=True)  
            return {
                'driver': full_name,
                'points': int(points)
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
        except TypeError:
            return f"ensure that position is an integer"
    else:
        return f"no data available for the year {year}"
    
def get_driver_at_position_no_points(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[int(position)]  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts)
            return {
                'driver': full_name,
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
        except TypeError:
            return f"ensure that position is an integer"
    else:
        return f"no data available for the year {year}"
    

def get_constructors_championship(year):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:
            data = [row.find_all('td')[i].get_text(strip=True) for i in [1, 2, 3]]
            formatted_data.append({
                'position': data[0],
                'team': data[1], 
                'points': int(data[2])
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_constructors_championship_no_points(year):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:
            data = [row.find_all('td')[i].get_text(strip=True) for i in [1, 2]]
            formatted_data.append({
                'position': data[0],
                'team': data[1], 
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_constructor_at_position(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[int(position)]  
            data = [row.find_all('td')[i].get_text(strip=True) for i in [2, 3]]
            return {
                'team': data[0],
                'points': int(data[1])
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
        except TypeError:
            return f"ensure that position is an integer"
    else:
        return f"no data available for the year {year}"
    
def get_constructor_at_position_no_points(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[int(position)]  
            data = [row.find_all('td')[i].get_text(strip=True) for i in [2]]
            return {
                'team': data[0],
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
        except TypeError:
            return f"ensure that position is an integer"
    else:
        return f"no data available for the year {year}"
    
def get_races_by_year(year):
    url = f'https://www.formula1.com/en/results.html/{year}/races.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []

    if table:
        for row in table.find_all('tr')[1:]:  
            data = [row.find_all('td')[i].get_text(strip=True) for i in [1, 2]]
            formatted_data.append({
                'location': data[0],
                'date': data[1], 
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_race_url(year, location):
    url = f'https://www.formula1.com/en/results.html/{year}/races.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        for row in table.find_all('tr'):  
            td = row.find('td', class_='dark bold')
            if td and location in td.get_text(strip=True):
                a_tag = td.find('a', href=True)
                if a_tag:
                    return a_tag['href']
    
def get_winner_by_race(year, race):
    try:
        url = get_race_url(year, race)
    except:
        print("no such race exists")

    url = 'https://www.formula1.com' + url
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[1] 
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
            car = row.find_all('td')[4].get_text(strip=True)
            return ({
                'driver': full_name,
                'car': car, 
                })
        except IndexError:
            return f"no driver data available for race {race} in the year {year}"
    else:
        return f"no data available for the year {year}"
    
def get_race_result(year, race):
    url = get_race_url(year, race)
    url = 'https://www.formula1.com' + url
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []

    if table:
        try:
            row = table.find_all('tr')[1] 
            position = row.find_all('td')[1].get_text(strip=True)
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts)
            car = row.find_all('td')[4].get_text(strip=True)
            time = "interval"
            formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time
                    })
            for row in table.find_all('tr')[2:]:  
                position = row.find_all('td')[1].get_text(strip=True)
                name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
                full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
                car = row.find_all('td')[4].get_text(strip=True)
                time = row.find_all('td')[6].get_text(strip=True)
                formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time
                    })
            return formatted_data
        except IndexError:
            return f"no driver data available for race {race} in the year {year}"
    else:
        return f"no data available for the year {year}"
    
def get_pole_pos(year, race):
    url = get_race_url(year, race).strip('race-result.html')
    url = 'https://www.formula1.com' + url + 'qualifying.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')
        
    if table:
        try:
            row = table.find_all('tr')[1] 
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts)
            car = row.find_all('td')[4].get_text(strip=True)
            time = row.find_all('td')[7].get_text(strip=True)
            return ({
                'driver': full_name,
                'car': car, 
                'time': time
                })
        except IndexError:
            return f"no driver data available for {race} in the year {year}"
    else:
        return f"no data available for the year {year}"
    
def get_qualifying_result_from_2006(year, race):
    url = get_race_url(year, race).strip('race-result.html')
    url = 'https://www.formula1.com' + url + 'qualifying.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []

    if table:
        try:
            for row in table.find_all('tr')[1:11]:  
                position = row.find_all('td')[1].get_text(strip=True)
                name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
                full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
                car = row.find_all('td')[4].get_text(strip=True)
                time = row.find_all('td')[7].get_text(strip=True)
                formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time + "(Q3)"
                    })
            for row in table.find_all('tr')[11:16]:  
                position = row.find_all('td')[1].get_text(strip=True)
                name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
                full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
                car = row.find_all('td')[4].get_text(strip=True)
                time = row.find_all('td')[6].get_text(strip=True)
                formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time + "(Q2)"
                    })
            for row in table.find_all('tr')[16:]:  
                position = row.find_all('td')[1].get_text(strip=True)
                name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
                full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
                car = row.find_all('td')[4].get_text(strip=True)
                time = row.find_all('td')[5].get_text(strip=True)
                formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time + "(Q1)"
                    })
            return formatted_data
        except IndexError:
            return f"no driver data available for race {race} in the year {year}"
    else:
        return f"no data available for the year {year}"
    
def get_qualifying_result_before_2006(year, race):
    url = get_race_url(year, race).strip('race-result.html')
    url = 'https://www.formula1.com' + url + 'qualifying.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []

    if table:
        try:
            for row in table.find_all('tr')[1:]:  
                position = row.find_all('td')[1].get_text(strip=True)
                name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
                full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
                car = row.find_all('td')[4].get_text(strip=True)
                time = row.find_all('td')[5].get_text(strip=True)
                formatted_data.append({
                    'position': position,
                    'driver': full_name,
                    'car': car, 
                    'time': time 
                    })
            return formatted_data
        except IndexError:
            return f"no driver data available for race {race} in the year {year}"
    else:
        return f"no data available for the year {year}"
            

while True:
    user_input = input("? ")
    if user_input.lower() == 'exit':
        break

    parts = user_input.split(':')

    if len(parts) == 3 and parts[0].lower() == "championship":
        type_char = parts[1]
        year = parts[2]

        if type_char == '-d':
            try:
                drivers_list = get_drivers_championship(year)
                for row in drivers_list:
                    print(f"{row['position']}.{row['driver']}: {row['points']}")
            except (ValueError, TypeError):
                print("error: enter valid year")
        elif type_char == '-c':
            try:
                constructors_list = get_constructors_championship(year)
                for row in constructors_list:
                    print(f"{row['position']}.{row['team']}: {row['points']}")
            except (ValueError, TypeError):
                print("enter valid year")
        else:
            print("unknown flag: use -c or -d")
    
    elif len(parts) == 4 and parts[0].lower() == "championship":
        if parts[3].lower() == "!p":
            type_char = parts[1]
            year = parts[2]

            if type_char == '-d':
                try:
                    drivers_list = get_drivers_championship_no_points(year)
                    for row in drivers_list:
                        print(f"{row['position']}.{row['driver']}")
                except (ValueError, TypeError):
                    print("error: enter valid year")
            elif type_char == '-c':
                try:
                    constructors_list = get_constructors_championship_no_points(year)
                    for row in constructors_list:
                        print(f"{row['position']}.{row['team']}")
                except (ValueError, TypeError):
                    print("enter valid year")
            else:
                print("unknown flag: use -c or -d")
        else:
            print("unknown flag: use !p")

    elif len(parts) == 4 and parts[0].lower() == "at-pos":
        type_char = parts[1]
        year = parts[2]
        pos = parts[3]

        if type_char == '-d':
            try:
                driver = get_driver_at_position(year, pos)
                print(f"{driver['driver']}: {driver['points']}")
            except (ValueError, TypeError):
                    print("error: enter valid year")
        elif type_char == '-c':
            try:
                constructor = get_constructor_at_position(year, pos)
                print(f"{constructor['team']}: {constructor['points']}")
            except (ValueError, TypeError):
                print("enter valid year")
        else:
            print("unknown flag: use -c or -d")

    elif len(parts) == 5 and parts[0].lower() == "at-pos":
        if parts[4] == "!p":
            type_char = parts[1]
            year = parts[2]
            pos = parts[3]

            if type_char == '-d':
                try:
                    driver = get_driver_at_position(year, pos)
                    print(f"{driver['driver']}")
                except (ValueError, TypeError):
                        print("error: enter valid year")
            elif type_char == '-c':
                try:
                    constructor = get_constructor_at_position(year, pos)
                    print(f"{constructor['team']}")
                except (ValueError, TypeError):
                    print("enter valid year")
            else:
                print("unknown flag: use -c or -d")
        else:
            print("unknown flag: use !p")

    elif len(parts) == 3 and parts[0].lower() == "champion":
        type_char = parts[1]
        year = parts[2]

        if type_char == '-d':
            try:
                driver = get_driver_at_position(year, 1)
                print(f"{driver['driver']}: {driver['points']}")
            except (ValueError, TypeError):
                    print("error: enter valid year")
        elif type_char == '-c':
            try:
                constructor = get_constructor_at_position(year, 1)
                print(f"{constructor['team']}: {constructor['points']}")
            except (ValueError, TypeError):
                print("enter valid year")
        else:
            print("unknown flag: use -c or -d")

    elif len(parts) == 4 and parts[0].lower() == "champion":
        if parts[3] == "!p":
            type_char = parts[1]
            year = parts[2]

            if type_char == '-d':
                try:
                    driver = get_driver_at_position(year, 1)
                    print(f"{driver['driver']}")
                except (ValueError, TypeError):
                        print("error: enter valid year")
            elif type_char == '-c':
                try:
                    constructor = get_constructor_at_position(year, 1)
                    print(f"{constructor['team']}")
                except (ValueError, TypeError):
                    print("enter valid year")
            else:
                print("unknown flag: use -c or -d")
        else:
            print("unknown flag: use !p")  

    elif len(parts) == 2 and parts[0].lower() == "races":
        try:
            year = int(parts[1])
            races = get_races_by_year(year)
            for row in races:
                print(f"{row['location']}: {row['date']}")
        except ValueError:
            print("enter valid year")

    elif len(parts) == 3 and parts[0].lower() == "winner":
        try:
            year = parts[1]
            race = parts[2]
            
            winner = get_winner_by_race(year, race)

            print(f"{winner['driver']}: {winner['car']}")
        except ValueError:
            print("enter valid year")

    elif len(parts) == 3 and parts[0] == "pole":
        try:
            year = parts[1]
            race = parts[2]
            
            winner = get_pole_pos(year, race)

            print(f"{winner['driver']}({winner['car']}): {winner['time']}")
        except ValueError:
            print("enter valid year")

    elif len(parts) == 3 and parts[0] == "race-result":
        try:
            year = parts[1]
            race = parts[2]
            race_result = get_race_result(year, race)
            for row in race_result:
                print(f"{row['position']}. {row['driver']}({row['car']}): {row['time']}")
        except (ValueError, TypeError):
            print("error: enter valid year")

    elif len(parts) == 3 and parts[0] == "qualifying-result":
        try:
            year = int(parts[1])
            race = parts[2]
            if year >= 2006:
                race_result = get_qualifying_result_from_2006(year, race)
            else:
                race_result = get_qualifying_result_before_2006(year, race)

            for row in race_result:
                print(f"{row['position']}. {row['driver']}({row['car']}): {row['time']}")
        except (ValueError, TypeError):
            print("error: enter valid year")

    else:
        print("invalid command")

            