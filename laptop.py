import requests 
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

laptop_dict = {
    'name': [],
    'price': [],
    'shipping': [],
    'link': []
}   

url = 'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&RAM%2520Size=32%2520GB&_nkw=laptop&_sacat=0&Storage%2520Type=SSD%2520%2528Solid%2520State%2520Drive%2529&SSD%2520Capacity=1%2520TB&_ipg=4&Processor=Intel%2520Core%2520i7%252013th%2520Gen%252E&rt=nc&_oaa=1&_dcat=177&_pgn=1'

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Connection": "keep-alive",
    "DNT": "1",  # Do Not Track header
}

cookies = {
'AMP_MKTG_f93443b04c': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE',
'AMP_f93443b04c' : 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI3ZWMxMjMxYi1lNWViLTQ3ZGQtOWJiMy0wYTVhNmVjODdkNmElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzM2OTQ0MjY5NjUwJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTczNjk0ODgwMTI4NyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjklMkMlMjJwYWdlQ291bnRlciUyMiUzQTI4JTdE',
'__ssds' : '2',
'__ssuzjsr2' : 'a9be0cd8e',
'__uzma' : 'd6490395-acc7-4517-8588-c17179f74f71',
'__uzmaj2': '139191c5-4988-41e4-a520-cecc4ad95d81',
'__uzmb': '1736944268',
'__uzmbj2' : '1736944273',
'__uzmc':'275623747681',
'__uzmcj2':'350452544441',
'__uzmd':'1736944911',
'__uzmdj2':'1736944942',
'__uzme':'4227',
'__uzmf': '7f6000b935016d-5b10-4f2b-b9ab-71c007c7ee311736944268712642591-cc396927f7e9c4c237',
'__uzmfj2': '7f6000b935016d-5b10-4f2b-b9ab-71c007c7ee311736944273111669083-b72db9613bef99b825',
'__uzmlj2': 'DlYJq5GfCbdzkryq1yiu3NGs4cS5pS9WEuzb3lBmxxI=',
'ak_bmsc': '9812865C6D77E3026CE5B5BB84182169~000000000000000000000000000000~YAAQP946Fx79v1+UAQAA9S/yaRpKxbEgTmjXex0vt853vpiMm+aBwrZ+qPg3INtSvixJ2OlFatYBiUsxB86Y1IqsFdwBo3Kz7PsuDDaITLESwup4Vig5WsSF16r1e39yNTZN6IMcVls8u4loBzJ+loQahpNY7pJRB9phtDwtOcKI2qeDHFjqdBgii5S1r0nm126C83wE6zu1qmQbOVlfOzyCBX1kDr4vSMi93+m8UyMpqbohuAocrhe5oUySxOO68hAWIIuFso/fA7AfpJi0uOYbi4EqESZHdhMu1tS4ku7gX7TRaIfdT/VrdO6iK+vVyPfQTJwujUNYHG2ZQi3NXhHdKLQwNewetQny3fCHJ92MKylHJZXk3QoOWcZ1SoHQ1Nd54N+Ruf7m',
'bm_sv' : '418F64ED07B2DAF194EEDDC42BB03728~YAAQz45B1CLSt0mUAQAA1EAmahpqmaMFiQbIZWS4cLQBiHldHMTSoCEvhdlPB/ZEM7l+xE1Uv4bFDMDguDDp71bp3wCGVhUcIohSjxvyh3Cc2BHftIhTO4Yvn7MA8zUO/MkabXkR3HSsnUgXHaee0LvgEBSEPovYptQHjboCLcxAK6hAwW2MBkLDOi1c1NeuY2DTRCiWPioIepyC1l3s23cqQKvdiYfg7J46itmrGZliochdfWPHJjMB5vYTRss=~1',
'dp1':'bpbf/%236000000000000000006968eb76^bl/TR6b4a1ef6^',
'ebay':'%5Ejs%3D1%5Esbf%3D%23000000%5E',
'nonsession':'BAQAAAZRXz2gmAAaAADMABWlo63YwNjAxMADKACBrSh72NjlmMjJmNWYxOTQwYWQ5MDUxZjUzYzZjZmZmZjQ3N2UAywABZ4e+/jJHAfUaNFsjO/KJdOWwf41OnfmGgA**',
'ns1':'BAQAAAZRXz2gmAAaAANgAU2lo63ZjNjl8NjAxXjE3MzY5NDQyNzE5MDdeXjFeM3wyfDV8NHw3fDEwfDQyfDQzfDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3NRZuKjjfNQT81qJvO4wWjLuXcRRf',
's':'CgAD4ACBniPwLNjlmMjJmNWYxOTQwYWQ5MDUxZjUzYzZjZmZmZjQ3N2WPXLRG'

}

page_no = 1
while True:
    url = f'https://www.ebay.com/sch/i.html?_fsrp=1&_from=R40&RAM%2520Size=32%2520GB&_nkw=laptop&_sacat=0&Storage%2520Type=SSD%2520%2528Solid%2520State%2520Drive%2529&SSD%2520Capacity=1%2520TB&_ipg=4&Processor=Intel%2520Core%2520i7%252013th%2520Gen%252E&rt=nc&_oaa=1&_dcat=177&_pgn={page_no}'
    response = requests.get(url, headers=headers, cookies=cookies) #cookies with 
    print(response.status_code)
    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.text, 'html.parser') 

    #öncelikle bir container olusturalım
    container = soup.find('div', attrs={'id': 'srp-river-results'})
    laptops = container.find_all('div', class_='s-item__info')
    print(len(laptops))
    for laptop in laptops:

        if laptop.find('span', attrs = {'role': 'heading'}) is not None: #if the name is not none, then we can get the name
            name = laptop.find('span', attrs = {'role': 'heading'}).text
        else: 
            name = "No name found"
        laptop_dict['name'].append(name)

        if laptop.find('span', class_='s-item__price') is not None:
            price = laptop.find('span', class_='s-item__price').text
        else:
            price = "No price found"
        laptop_dict['price'].append(price)

        if laptop.find('span', class_='s-item__shipping') is not None:
            shipping = laptop.find('span', class_='s-item__shipping').text
        else:
            shipping = "No shipping found"
        laptop_dict['shipping'].append(shipping)

        if laptop.find('span', class_='s-item__location') is not None:
            link = laptop.find('a', class_= 's-item__link')['href']
        else:
            link = "No link found"
        laptop_dict['link'].append(link)

   

    next_as_button = soup.find('button', class_='pagination__next')
    if next_as_button is not None:
        break

    page_no += 1

            #If you want to capture and print the html content of the relevant page;
            # print("Writing to file...")

            # with open("ebay_pretty.html", "w", encoding="utf-8") as file:
            #     file.write(soup.prettify())
            #     print("File written successfully.")

        # Debug print to check if the code reaches here


        # container = soup.find('div', attrs={'id': 'srp-river-results'})
        # laptops = container.ul.find_all('div', class_='s-item__info') 
        # print(len(laptops))

    
df = pd.DataFrame(laptop_dict)
df.to_excel('laptops.xlsx')