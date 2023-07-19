from movies_class import *
import random as r
import os
from time import *
import sqlite3


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

from Tools.demo.mcast import sender

import json

def menu():
    x = main_page()
    
    if x == 2:
        enter()
    elif x == 1:
        menu()

    elif x == 3:
        register()

    elif x == 4:
        search()

    elif x == 5:
        news()


def main_page():
    print('==========')
    print('Uzmovi.com')
    print()
    print("1. Menu")
    print('2. Entry')
    print('3. Registration')
    print('4. Search')
    print('5. News')
    n = int(input('Enter: '))
    return n


def reader():
    with open('movies.json', 'r') as file:
        movie_data = json.load(file)
    return movie_data


def add_movies():
    title = input('Title: ')
    year = input('Year: ')
    country = input('Country: ')
    language = input('Language: ')
    time = input('Time: ')
    movie = Movie(title=title, year=year, country=country, language=language, time=time)
    movie_data = reader()
    with open('movies.json', 'w') as file:
        movie_data.append(movie.get_info())
        json.dump(movie_data, file, indent=4)
    return movie


def delete_movie():
    print("Qaysi kinoni o'chirmoqchisiz ")
    print()
    clear_movie_name = input("Nomini yozing: ")
    movie_data = reader()
    c = True
    for i in movie_data:
        if i['title'] == clear_movie_name:
            movie_data.remove(i)
            c = False
    if c:
        print('Bunday nomli kino topilmadi')
    

def search():
    print('1. Name of movie ')
    print('2. year of movies ')
    print('3. country of movies ')
    print('4. language ')
    n = int(input('Enter: '))
    print('Searching movies ...')
    sleep(1)
    with open('movies.json', 'r') as file:
        movie_data = json.load(file)
    if n == 1:
        x = input('Enter name of movie: ')
        c = True
        for i in movie_data:
            if x.upper() == i['title'].upper():
                fprint(i)
                c = False
        if c:
            print("The film wasn't found")

    if n == 2:
        x = input('Enter year of movie: ')
        c = True
        for i in movie_data:
            if x.upper() == i['year'].upper():
                fprint(i)
                c = False
        if c:
            print("The film wasn't found")
    if n == 3:
        x = input('Enter country of movie: ')
        c = True
        for i in movie_data:
            if x.upper() == i['country'].upper():
                fprint(i)
                c = False
        if c:
            print("The film wasn't found")
    if n == 4:
        x = input('Enter language of movie: ')
        c = True
        for i in movie_data:
            if x.upper() == i['language'].upper():
                fprint(i)
                c = False
        if c:
            print("The film wasn't found")


def next_movie(txt):
    os.system('cls')

    while True:
        os.system('cls')
        date = datetime.now()
        hour = str(date.hour).zfill(2)
        minutes = str(date.minute).zfill(2)
        seconds = str(date.second).zfill(2)
        print(txt)
        sleep(0.12)


def fprint(data):
    for j, k in data.items():
        print(j, ": ", k)


def news():
    print('||  News  ||')
    movie_data = reader()
    it = 0
    for i in movie_data[::-1]:
        os.system('cls')
        date = datetime.now()
        hour = str(date.hour).zfill(2)
        minutes = str(date.minute).zfill(2)
        seconds = str(date.second).zfill(2)
        fprint(i)
        sleep(3)
        print('>>>')
        sleep(1)
        it += 1
        if it == 5:
            break
    menu()


conn = sqlite3.connect('dbt.db')

conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
        name VARCHAR(50) NOT NULL,
        lastname VARCHAR(50) NOT NULL,
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
""")


def create_user(name, lastname, email, password):

    cur = conn.cursor()
    id = r.randint(1000000, 1000000)
    query = """
            insert into users (name, lastname, id, email, password)
            values (?, ?, ?, ?, ?, ?)
        """
    value = (name, lastname, id, email, password)
    cur.execute(f"""
        insert into users (name, lastname, id, email, password)
        values (name, lastname, id, email, password)
""")
    conn.commit()
# enter and register


with open("users.json", "r") as f:
    data = json.load(f)

for i in data:
    create_user(i['name'], i['surname'], i['email'], i['password'])

with open("admins.json", 'r') as f:
    admin_data = json.load(f)


def admin_page():
    print("Welcome to the admin page")
    print('1. Create a new movie')
    print('2. Delete the movie')
    print('3. Create a news')
    n = int(input("Enter: "))
    if n == 1:
        add_movies()
        print("Movies created")
    elif n == 2:
        delete_movie()
        print("Movie deleted")
    elif n == 3:
        news()
    x = input('1. admin page \n2. exit ')
    if '1' == x:
        admin_page()
    elif x == '2':
        exit()

    menu()


def exit():
    menu()


def enter():
    
    email = input('email address: ')
    password = input('password: ')
    print('0. Menu ')
    print('1. Continue ')
    x = input('Enter: ')
    c = True
    if x == '1':
        for i in admin_data:
            if password == i['password'] and email == i['email']:
                admin_page()
                c = False
        for i in data:
            if password == i['password'] and email == i['email']:
                menu()
                c = False

        if c:
            print("Error: ")
    elif x == '0':
        menu()
    
    else:
        print('Boshqa buyruq tanlandi: ')
        x = input('Enter: ')


def authenticate(email):
    sender_email = f'qarshiyevnizomiddin75@gmail.com'
    receiver_email = email
    subject = 'Account activation'
    x = r.randint(1000, 10000)
    message = f'Your activation code is: {x}'
    # SMTP server configuration for gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'qarshiyevnizomiddin75@gmail.com'
    smtp_password = 'cwonhgbttezjotmd'

    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject

    email_message.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        # server.sendmail(sender_email, receiver_email, email_message.as_string())
        server.send_message(email_message)
    return x


def register():
    dic = {}
    dic['name'] = input("Name: ")
    dic['lastname'] = input("Lastname: ")
    dic['username'] = input("Username: ")
    for i in data:
        if dic['username'] == i['username']:
            print("Bu foydalanuvchi ismi band")
            dic['username'] = input("Username: ")
    dic['email'] = input("Email: ")
    for i in data:
        if dic['email'] == i['email']:
            print("Bu email bilan ro'yxatdan o'tilgan")
            dic['email'] = input("Email: ")
    auth1 = authenticate(dic['email'])
    while activate(auth1):
        pass
    password = input("Password: ")
    while True:
        if len(password) > 7:

            break
        print("Parol 8 ta belgidan ko'p bolsin")
        password = input("Password: ")
    dic['password'] = password
    data.append(dic)
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

    return dic


def activate(auth1):
    code = int(input('code: '))
    if auth1 == code:
        print("Login successful")
        return False
    else:
        print("Login failed")
        return True


def account():
    n = int(input("Kirish uchun 0 ni kiriting \n"
                  "Ro'yxatdan o'tish uchun 1 ni kiriting "))
    if n == 0:
        enter()
    elif n == 1:
        dic1 = register()
    else:
        raise ValueError("Boshqa son kiritildi ")



# sender_email = 'qarshiyevnizomiddin75@gmail.com'
# receiver_email = 'qarshiyevnizomiddin75@gmail.com'
# subject = 'Account activation'
# message = f'Your activation code is: 1234'

# news()

menu()











