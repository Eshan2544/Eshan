Jimport os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='64bit':
    print(f'{red}[•] Facebook {white}')
    os.system('xdg-open https://web.facebook.com/careless.eshan')
    import TRT
elif bit=='32bit':
    print(f'{green}[•] subscribe krne Walo Ko Approvel Meli Ga {white}')
    os.system('xdg-open https://www.youtube.com/channel/UCPn0mhGI_GOdWlEQDdIseDA')
    
else:
    print(f'{green}[×] Sorry System Not Support{white}')
