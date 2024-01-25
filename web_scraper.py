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
    
    else:
        print("invalid command")

            