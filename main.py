import requests
import terminal_banner

banner_text = '     SubScan\nEnter target website like example.com'
my_banner = terminal_banner.Banner(banner_text)
target_input = input('Enter your target website:\n')

def make_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass

with open('subdomainlist.txt', 'r') as subdomain_list:
    for word in subdomain_list:
        word = word.strip()
        url ='http://' + word + '.' + target_input
        response = make_request(url)
        if response:
            print('Found subdomain -----> ' + url)