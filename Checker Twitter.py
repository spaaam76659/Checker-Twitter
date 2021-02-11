import requests
r = requests.session()

count = 0
print('''
[!] Follow Me In Instagram : @680068
   _____ _               _               _______       _ _   _            
  / ____| |             | |             |__   __|     (_) | | |           
 | |    | |__   ___  ___| | _____ _ __     | |_      ___| |_| |_ ___ _ __ 
 | |    | '_ \ / _ \/ __| |/ / _ \ '__|    | \ \ /\ / / | __| __/ _ \ '__|
 | |____| | | |  __/ (__|   <  __/ |       | |\ V  V /| | |_| |_  __/ |   
  \_____|_| |_|\___|\___|_|\_\___|_|       |_| \_/\_/ |_|\__|\__\___|_|

                        Coded By | @680068
                        
''')
file = input('[~] Enter File Name :')
input("\n[!] Press Enter To Start")
berlin = file
file = open(berlin).read().splitlines()
for file in file:
    url = 'https://tweeterid.com/ajax.php'
    head = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '23',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '__utmc=116903043; __utmz=116903043.1613059243.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=a1f785df4cee6942-229f6a496cba00bf:T=1613059242:RT=1613059242:S=ALNI_MZybWJL6_nDVVzTIPVeJdO-t2R8tg; __utma=116903043.1412031861.1613059243.1613059243.1613063160.2; __utmt=1; __utmb=116903043.1.10.1613063160',
        'Host': 'tweeterid.com',
        'Origin': 'https://tweeterid.com',
        'Referer': 'https://tweeterid.com/',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A\"Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
    data = {
        'input': {file}
        }
    req = r.post(url, headers=head, data=data)
    if 'error' in req:
        count +=1
        print(f'{count}: {file} '+ ' Available')
        with open('Available @680068.txt', 'a') as x:
            x.write(file + '\n')
        
    else:
        count +=1
        print(f'{count}: {file} '+ ' Not Available')

            
