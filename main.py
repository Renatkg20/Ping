import os
import requests
import time

#from twilio.rest import Client
# account_sid = 'AC019f9ff43d643f8b2761d0fa7e075167'
# auth_token = 'c564a04f643880fe45a9c0881ab55d45'
# client = Client(account_sid, auth_token)

def telegram_bot_sendtext(bot_message):
    bot_token = '127203251:AAEFp8g4Y67bB_DuzH4GEWHS3M69zO1l88g'
    bot_chatID = '535448074'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def job():
	hostname = "92.62.72.167" 
	response = os.system("ping -c 1 " + hostname)   
	if response == 0:
		print (hostname, 'Reboot successful!')
	else:
		test = telegram_bot_sendtext("No pings")
		print (hostname, 'Rebooting..!')
# message = client.messages.create(body='I will stay here)))!', from_='+12058284432', to='+996551799744')
   
# print (message.sid)
if __name__ == '__main__':
    while True:
        job()
        time.sleep(10)