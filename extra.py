import requests

def hit_sender(card,message,chat_id):
    bot_token = '5999687642:AAGwxng5g1OiFXsSwJp117FpcItSmuEPbuE'
    url = f'https://api.telegram.org/bot{5999687642:AAGwxng5g1OiFXsSwJp117FpcItSmuEPbuE}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    requests.post(url, data=data)
