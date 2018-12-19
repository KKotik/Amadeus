# Основные библиотеки
import random
import time
import os
import re

# Модуль авторизации
vk_token = 'aaf456f32ee666421b248976d5c1e2951584f6826cbbbe490abc829ade280c670e6cde739f4bd9e41bcfc'
tg_token = '648054304:AAEhQjnMaxQ7QyAsNWMNW_yggY4YQnJYcQg'

# Модуль API вконтакте
import vk_requests

vk = vk_requests.create_api(app_id=6759791, service_token=vk_token, scope=['offline', 'messages'], interactive=True)
id = 517961285

# Датабаза на SQLite 3
import sqlite3

cwd = os.getcwd()
connection = sqlite3.connect(cwd + '/.data/data.db')
cursor = connection.cursor()

# Модуль классов

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False

# Модуль функций

def register(user):
    cursor.execute('SELECT * FROM users WHERE vk_id = ?', [user])
    if not cursor.fetchall():
        first_name = vk.users.get(user_id=user)[0]['first_name']
        last_name = vk.users.get(user_id=user)[0]['last_name']
        execute('users', "" + str(user) + ", '" + first_name + "', '" + last_name + "'")

def response(type, peer, id):
    chance = random.randint(1, 99)
    if 1  <= chance <= 50:
        cursor.execute('SELECT arg_1 FROM output WHERE data_id = ?', [id])
        data = cursor.fetchone()[0].split('$')
        send(type, peer, data[random.randint(0, len(data)-1)])
    if 51 <= chance <= 80:
        cursor.execute('SELECT arg_2 FROM output WHERE data_id = ?', [id])
        data = cursor.fetchone()[0].split('$')
        send(type, peer, data[random.randint(0, len(data)-1)])
    if 81 <= chance <= 95:
        cursor.execute('SELECT arg_3 FROM output WHERE data_id = ?', [id])
        data = cursor.fetchone()[0].split('$')
        send(type, peer, data[random.randint(0, len(data)-1)])
    if 96 <= chance <= 99:
        cursor.execute('SELECT arg_4 FROM output WHERE data_id = ?', [id])
        data = cursor.fetchone()[0].split('$')
        send(type, peer, data[random.randint(0, len(data)-1)])

def checking(word, id):
    cursor.execute('SELECT data FROM input WHERE data_id = ?', [id])
    data = cursor.fetchone()[0].split()
    if not word in data:
        return False
    else:
        return True

def execute(database, command):
    cursor.execute("INSERT INTO " + database + " VALUES (" + command + ")")
    connection.commit()

def complete(type, peer):
    if type == 'chat':
        vk.messages.markAsRead(peer_id=2000000000+int(peer))
    if type == 'user':
        vk.messages.markAsRead(peer_id=peer)

def send(type, peer, text):
    if type == 'chat':
        vk.messages.send(peer_id=2000000000+int(peer), message=text)
    if type == 'user':
        vk.messages.send(peer_id=peer, message=text)

# Модуль комманд

def command_repost(group):
    posts = vk.wall.get(owner_id=group, offset=1)
    post = str(posts['items'][0]['id'])
    cursor.execute('SELECT post_id FROM repost WHERE group_id = ?', [group])
    last = cursor.fetchone()[0]
    if not last == post:
        wall = [group, post]
        attachments = ['wall{}_{}'.format(wall[0], wall[1])]
        vk.messages.send(peer_id=2000000001, attachment=attachments)
        cursor.execute('UPDATE repost SET post_id = ? WHERE group_id = ?', [post, group])
        connection.commit()
        time.sleep(1)

def command_chance(type, peer, msg):
    msg[len(msg) - 1] = re.sub("[.!?]", '', msg[len(msg) - 1])
    del msg[0]
    del msg[0]
    for index in range(0, len(msg)):
        for case in switch(message[index]):
            if case('Твоего', 'твоего'):
                message[index] = 'моего'
                break
            if case('Моего', 'моего'):
                message[index] = 'твоего'
                break
            if case('Тобой', 'тобой'):
                message[index] = 'мной'
                break
            if case('Мной', 'мной'):
                message[index] = 'тобой'
                break
            if case('Тебя', 'тебя'):
                message[index] = 'меня'
                break
            if case('Меня', 'меня'):
                message[index] = 'тебя'
                break
            if case('Тебе', 'тебе'):
                message[index] = 'мне'
                break
            if case('Мне', 'мне'):
                message[index] = 'тебе'
                break
            if case('Твоя', 'твоя'):
                message[index] = 'моя'
                break
            if case('Моя', 'моя'):
                message[index] = 'твоя'
                break
            if case('Твой', 'твой'):
                message[index] = 'мой'
                break
            if case('Мой', 'мой'):
                message[index] = 'твой'
                break
            if case('Твое', 'твое'):
                message[index] = 'мое'
                break
            if case('Мое', 'мое'):
                message[index] = 'твое'
                break
            if case('Ты', 'ты'):
                message[index] = 'я'
                break
            if case('Я', 'я'):
                message[index] = 'ты'
                break
            if case('Твоего,', 'твоего,'):
                message[index] = 'моего,'
                break
            if case('Моего,', 'моего,'):
                message[index] = 'твоего,'
                break
            if case('Тобой,', 'тобой,'):
                message[index] = 'мной,'
                break
            if case('Мной,', 'мной,'):
                message[index] = 'тобой,'
                break
            if case('Тебя,', 'тебя,'):
                message[index] = 'меня,'
                break
            if case('Меня,', 'меня,'):
                message[index] = 'тебя,'
                break
            if case('Тебе,', 'тебе,'):
                message[index] = 'мне,'
                break
            if case('Мне,', 'мне,'):
                message[index] = 'тебе,'
                break
            if case('Твоя,', 'твоя,'):
                message[index] = 'моя,'
                break
            if case('Моя,', 'моя,'):
                message[index] = 'твоя,'
                break
            if case('Твой,', 'твой,'):
                message[index] = 'мой,'
                break
            if case('Мой,', 'мой,'):
                message[index] = 'твой,'
                break
            if case('Твое,', 'твое,'):
                message[index] = 'мое,'
                break
            if case('Мое,', 'мое,'):
                message[index] = 'твое,'
                break
            if case('Ты,', 'ты,'):
                message[index] = 'я,'
                break
            if case('Я,', 'я,'):
                message[index] = 'ты,'
                break
            if case():
                break
    string = ' '.join(msg)
    chance = random.randint(0, 100)
    number = random.randint(1, 4)
    cursor.execute('SELECT arg_' + str(number) + ' FROM output WHERE data_id = ?', ['101'])
    data = cursor.fetchone()
    send(type, peer, str(data[0]) + ' ' + string + ' равна ' + str(chance) + '%.')

# Счетчики

count = 0

# Главный модуль программы
while True:
    messages = vk.messages.getConversations(offset=0, count=5, unread=1)
    if messages['count'] > 0:
        msg_peer = messages['items'][0]['conversation']['peer']['local_id']
        msg_type = messages['items'][0]['conversation']['peer']['type']
        msg_user = messages['items'][0]['last_message']['from_id']
        msg_text = messages['items'][0]['last_message']['text']
        message = msg_text.split()
        if len(message) > 0 and not (msg_user == id):
            register(msg_user)
            if checking(message[0], '001'):
                if len(message) > 1:
                    if checking(message[1], '101'):
                        if len(message) == 2:
                            send(msg_type, msg_peer, 'Похоже что-то пошло не так, для выполнения твоего запроса у меня недостаточно аргументов!'
                                                     '\n\nФормат запроса: Курису, вероятность <событие>.')
                        else:
                            command_chance(msg_type, msg_peer, message)
                    if len(message) > 2:
                        print('none')
                else:
                    response(msg_type, msg_peer, '001')
            if checking(message[0], '002'):
                response(msg_type, msg_peer, '002')
        if count == 30:
            command_repost('-167609719')
            command_repost('-79997904')
            command_repost('-9273458')
            count = 0
        count += 1
        complete(msg_type, msg_peer)
    time.sleep(1)