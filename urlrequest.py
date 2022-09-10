import requests
import time
import random
import optparse

parser = optparse.OptionParser()
optparse.OptionParser.format_epilog = lambda self, formatter: self.epilog
parser = optparse.OptionParser(epilog="If time is not specified, a random time interval \nbetween 5 to 30 seconds would be selected between each request.\nExample: python3 urlrequests.py --link https://bit.ly/ProfileGitHub --time 20\n")

parser.add_option("-l","--link",dest="link", help="[Reuqired] Used to specify a link for sending requests")
parser.add_option("-t","--time",dest="time", help="[Optional] Used to specify the time interval between each request")
(options,arguments) = parser.parse_args()
headers = {'Content-Type': 'text/html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }
i = 1
try: 
    if not options.link:
        print("[-] Please Specify a link to send requests to!")
    
    else:
        if options.time:
            while True:
                response = requests.get(options.link, headers=headers)
                interval = options.time
                print("\n[+] Request Sent")
                print(f"[+] Status Code: {response.status_code}")
                print(f"[+] Request Number: {i}")
                print(f"[+] Time till next request: {options.time} secs")
                i = i + 1
                time.sleep(int(interval))

        else:
            while True:
                response = requests.get(options.link, headers=headers)
                interval = random.randint(5,30)
                print("\n[+] Request Sent")
                print(f"[+] Status Code: {response.status_code}")
                print(f"[+] Request Number: {i}")
                print(f"[+] Time till next request: {interval} secs")
                i = i + 1
                time.sleep(int(interval))

except KeyboardInterrupt:
    print("[-] CTRL + C Detected...\n[-] Quiting.. ")

        