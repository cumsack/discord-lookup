import requests
import json
from datetime import datetime

token = "Bot " # DISCORD BOT TOKEN

user_id = input(f"User ID: ")

r=requests.get(f"https://discord.com/api/users/{user_id}", headers={"Authorization": token})

if 'Unknown User' in r.text:
  print(f"[-] Invalid ID")
  exit()
  
r=r.json()
discord_millis = int(int(user_id) * 1000 - 1420070400000)
high = bool = False
creation1 = (discord_millis << 22) + (2 ** 22 - 1 if high else 0)
DateFormat = '%d%m%H%M%S'
creation2 = str(datetime.strptime(str(creation1),DateFormat))
username = r['username'] + r['discriminator']
avatar = f"https://cdn.discordapp.com/avatars/{user_id}/{r['avatar']}"
banner_color = r['banner_color']
accent_color = r['accent_color']
banner = f"https://cdn.discordapp.com/banners/{user_id}/{r['banner']}"
flags = r['public_flags']

print(f"""\n[+] Username: {username}
[+] Avatar: {avatar}
[+] Banner: {banner}
[+] Banner Color: {banner_color}
[+] Accent: {accent_color}
[+] Flags: {flags}
[+] Creation: {creation2}
""")
