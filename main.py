import requests

#1
url = 'https://python.org/'
response = requests.get(url)
print('Сторінка доступна на сервері') if response.status_code == 200 else print('Сторінка недоступна на сервері')
#2
url = 'https://en.wikipedia.org/robots.txt'
response = requests.get(url)
if response.status_code == 200:
    print(response.text)
#3
url = 'https://catalog.data.gov/api/3/action/package_search?q=*:*'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    count = data['result']['count']
    print(f'Кількість наборів даних на data.gov: {count}')
#4
url = 'https://catalog.data.gov/api/3/action/package_search?sort=metadata_created%20desc&rows=1'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    name = data['result']['results'][0]['title']
    print(name)

#5
url = "https://api.covid19api.com/summary"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Дані:", data["Date"])
    print("World")
    print("Випадки:", data["Global"]["TotalConfirmed"])
    print("Смерті:", data["Global"]["TotalDeaths"])
    print("Одужання:", data["Global"]["TotalRecovered"])

    country = "Ukraine"
    for country_data in data["Countries"]:
        if country_data["Country"] == country:
            print(f"{country}")
            print("Випадки:", country_data["TotalConfirmed"])
            print("Смерті:", country_data["TotalDeaths"])
            print("Одужання:", country_data["TotalRecovered"])
            break


