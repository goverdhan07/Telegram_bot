# -*- coding: utf-8 -*-
import requests
import datetime
import random
import datetime

class BotHandler:
    def __init__(self, token):
            self.token = token
            self.api_url = "https://api.telegram.org/bot{}/".format(token)

    #url = "https://api.telegram.org/bot<token>/"

    def get_updates(self, offset=0, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_first_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[0]
        else:
            last_update = None

        return last_update




token = '1110302513:AAEbvUpTQ-uhq_y2aXvsa4LMbpROSYb9ZQs' 
mrPinkmanBot = BotHandler(token) 

quote_list1=['Failure is first step towards success', ' Dont be pushed around by the fears in your mind. Be led by the dreams in your heart.', 'Instead of worrying about what you cannot control, shift your energy to what you can create.','The past is a place of reference, not a place of residence; the past is a place of learning, not a place of living.','Maybe you can afford to wait. Maybe for you there"s a tomorrow. Maybe for you there"s one thousand tomorrows, or three thousand, or ten, so much time you can bathe in it, roll around it, let it slide like coins through you fingers. So much time you can waste it. But for some of us there"s only today. And the truth is, you never really know.','Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.','Life is about accepting the challenges along the way, choosing to keep moving forward, and savoring the journey.','You cannot control the behavior of others, but you can always choose how you respond to it.','Do not fear failure but rather fear not trying.','Never lose hope. Storms make people stronger and never last forever.','Stop comparing yourself to other people, just choose to be happy and live your own life.','Do not let the memories of your past limit the potential of your future. There are no limits to what you can achieve on your journey through life, except in your mind.','Once you realize you deserve a bright future, letting go of your dark past is the best choice you will ever make.','Stop giving other people the power to control your happiness, your mind, and your life. If you dont take control of yourself and your own life, someone else is bound to try.','If you have a strong purpose in life, you dont have to be pushed. Your passion will drive you there.','Nothing can disturb your peace of mind unless you allow it to.','Ninety-nine percent of the failures come from people who have the habit of making excuses.','Life is short. Live it. Fear is natural. Face it. Memory is powerful. Use it.','My advice is, never do tomorrow what you can do today. Procrastination is the thief of time.','Trust yourself, you know more than you think you do','Don’t stop until you’re proud.','Forget the mistake. Remember the lesson.']
#quote_list=['Failure is first step towards success']
quote=random.choice(quote_list1)
#time
currentTime = datetime.datetime.now()
currentTime.hour

def main():
    new_offset = 0
    print('hi, now launching...')

    while True:
        all_updates=mrPinkmanBot.get_updates(new_offset)

        if len(all_updates) > 0:
            for current_update in all_updates:
                print(current_update)
                first_update_id = current_update['update_id']
                if 'text' not in current_update['message']:
                    first_chat_text='New member'
                else:
                    first_chat_text = current_update['message']['text']
                first_chat_id = current_update['message']['chat']['id']
                if 'first_name' in current_update['message']:
                    first_chat_name = current_update['message']['chat']['first_name']
                elif 'new_chat_member' in current_update['message']:
                    first_chat_name = current_update['message']['new_chat_member']['username']
                elif 'from' in current_update['message']:
                    first_chat_name = current_update['message']['from']['first_name']
                else:
                    first_chat_name = "unknown"

                if first_chat_text == 'Hi' or first_chat_text == 'Hello':
                    if currentTime.hour < 12:
                        mrPinkmanBot.send_message(first_chat_id, 'Good Morning ' + first_chat_name)
                        new_offset = first_update_id + 1

                    elif 12 <= currentTime.hour < 18:
                        mrPinkmanBot.send_message(first_chat_id, 'Good Afternoon ' + first_chat_name)
                        new_offset = first_update_id + 1

                    else:
                        mrPinkmanBot.send_message(first_chat_id, 'Good Evening ' + first_chat_name)
                        new_offset = first_update_id + 1

                   
                elif first_chat_text == 'Motivate me' or first_chat_text == 'motivate me':
                    mrPinkmanBot.send_message(first_chat_id, quote + first_chat_name)
                    new_offset = first_update_id + 1

                elif first_chat_text == 'Send memes' or first_chat_text == 'send memes':
                    mrPinkmanBot.send_message(first_chat_id, 'Ah! There"s some issue ig, i will notify my boss, until then drop a message to @GoverdhanBiradar he"s a good memer btw ;)')
                    new_offset = first_update_id + 1

                elif first_chat_text == 'How are you' or first_chat_text == 'how are you':
                    mrPinkmanBot.send_message(first_chat_id, 'Iam fine wbu? ' + first_chat_name)
                    new_offset = first_update_id + 1   
                
                elif first_chat_text == 'How' or first_chat_text == 'how':
                    mrPinkmanBot.send_message(first_chat_id, 'Its simple type, "motivate me" for motivation and type "send memes" for memes and all those shit XD')
                    new_offset = first_update_id + 1

                elif first_chat_text == 'Bye' or first_chat_text == 'bye':
                    mrPinkmanBot.send_message(first_chat_id, 'Ok bye! have a nice day')
                    new_offset = first_update_id + 1

                elif first_chat_text == 'Ok bye' or first_chat_text == 'ok bye':
                    mrPinkmanBot.send_message(first_chat_id, 'Ok bye! have a nice day')
                    new_offset = first_update_id + 1



                else:
                    mrPinkmanBot.send_message(first_chat_id, 'I can motivate you and also I can send you good memes ;) ask how ' + first_chat_name)
                    new_offset = first_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()




       



