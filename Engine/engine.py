#!/usr/bin/env python3

import speech_recognition as sr
import datetime as dt
from gtts import gTTS
from playsound import playsound
import random as r
import pyowmimport json
import calendar
import urllib3

class Assistant:


    alarmtime = open('Configuration/data/time.txt', 'r+').read()
    # alarmtime = 18
    name = open('Configuration/data/name.txt', 'r+').read()
    # name = 'Rafayel'
    count = 0

    def get_responses(self):
        return {
            'hello': {self.speak: 'Hi'},
            'hi': {self.speak: 'Hello'},
            'how are you': {self.speak: r.choice(['Very well!', 'Good', 'Same as before', 'Can be better', 'Very bad', 'I am very good'])},
            'what is your name': {self.speak: 'My name is Tes'},
            'what is your age': {self.speak: 'I am ' + str(dt.date.today().year - 2017) + " years old."},
            'how old are you': {self.speak: 'I am ' + str(dt.date.today().year - 2017) + " years old."},
            'what is today\'s date': {
                self.speak: 'Today is ' + self.get_weekday() + ' ' + str(dt.date.today().day) + '.' + str(dt.date.today().month) + '.' + str(
                    dt.date.today().year) + '.'},
            'today': {
                self.speak: 'Today is ' + self.get_weekday() + ' ' + str(dt.date.today().day) + '.' + str(
                    dt.date.today().month) + '.' + str(
                    dt.date.today().year) + '.'},
            'bye bye': {self.speak: 'Bye-Bye!',
                        self.exit_app: 'None'},
            'where are you born': {self.speak: 'I am born in The Netherlands'},
            'fine to meet you': {self.speak: 'Nice to meet you, too'},
            'do you like YouTube': {self.speak: 'Yes, I love it!'},
            'what is the weather now': {self.speak: 'It is now ' + self.get_weatherO() + ' degrees'},
            'search': {self.speak: 'Ok, what would you like to search?'},
            'ok Google': {self.speak: 'Ha Ha Ha, Very funny!'},
            'what is the meaning of life': {self.speak: '42.'},
            'I\'m drunk': {self.speak: 'I hope you\'re not driving now!'},
            'tell me a joke': {self.speak: 'If you understand English, press 1. If you do not understand English, press 2.'},
            'job': {self.speak: 'What would you like to add to your task list?', self.add_task: 'Jobs'},
            'get jobs': {self.speak: 'Here are your tasks!', self.get_tasks: 'Jobs'},
            'delete job': {self.speak: 'What is the name of the task you want to delete?', self.delete_task: 'Jobs'},
            'goodnight': {self.speak: 'Good night!', self.good_night: 'Alarm is set for ' + str(self.alarmtime) + ' o\'clock'},
            'good night': {self.speak: 'Good night!', self.good_night: 'Alarm is set for ' + str(self.alarmtime) + ' o\'clock'},
            'thanks': {self.speak: 'I\'m always happy to help you'},
            'ok': {self.speak: 'I\'m always happy to help you'},
            'do you play Minecraft': {self.speak: 'No, it is too dificult for me'},
            'beatbox' : {self.speak: 'Boe, badaboem, boemboemboem, bada badaboem, doedoem boedoem.'}
        }

    def get_weekday(self):
        if calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 0:
            return 'Monday'
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 1:
            return 'Tuesday'
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 2:
            return "Wednesday"
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 3:
            return "Thursday"
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 4:
            return "Friday"
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 5:
            return "Saturday"
        elif calendar.weekday(dt.date.today().year, dt.date.today().month, dt.date.today().day) == 6:
            return "Sunday"


    def good_night(self, phrase):
        self.speak(phrase)
        alarm = True
        while alarm:
            time = dt.datetime.now()
            if time.hour != self.alarmtime:
                pass
            else:
                playsound('data/alarm/alarmsound.mp3')
                if self.record() == 'go':
                    alarm = False

    def speak(self, phrase):
        tts = gTTS(text=phrase, lang='en')
        tts.save('data/voice/response' + str(self.count) + '.mp3')
        playsound('data/voice/response' + str(self.count) + '.mp3')
        self.count += 1
        print(phrase + "\n")


    def look_for_answer(self, user_input, responses_list):
        for key in responses_list:
            if user_input == key:
                for action in responses_list[key]:
                    action(responses_list[key][action])
        return True

    def add_task(self, phrase = None):
        task = self.record()
        with open('data/tasks.txt', 'a+') as f:
            f.write(task + '\n')
        self.speak('Added \'' + task + '\' to your task list')

    def get_tasks(self, phrase=None):
        with open('data/tasks.txt', 'r+') as f:
            tasks = f.readlines()
            tasks = [x.strip() for x in tasks]
            for item in tasks:
                self.speak(item)

    def delete_task(self, phrase=None):
        task = self.record()
        fn = 'data/tasks.txt'
        f = open(fn)
        output = []
        for line in f:
            if task != line.strip():
                output.append(line)
        f.close()
        f = open(fn, 'w')
        f.writelines(output)
        f.close()
        self.speak('Successfully removed \'' + task + '\'from your task list')

    def record(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "....."
        except sr.RequestError as e:
            text = ""
            print("Could not request results; {0}".format(e))

        # print(text)
        return text


    def exit_app(self, Bye = None):
        quit()

    def search(self, tag):
        x = 0
        print("Searching for " + tag + "\n")
        global count
        http = urllib3.PoolManager()
        url = 'http://api.duckduckgo.com/?q=' + tag + '&format=json'
        response = http.request('GET', url)
        data = json.loads(response.data)
        self.speak('Here are some results!')
        count += 1
        for i in data["RelatedTopics"]:
            if x > 5:
                break
            try:
                resultText = data["RelatedTopics"][x]['Text']
                self.speak(resultText)
            except KeyError:
                pass
            count += 1
            x += 1


    # search('Python')
    def get_weatherO(self, phrase = None):
        http = urllib3.PoolManager()
        url = 'http://ipinfo.io/json'
        response = http.request('GET', url)
        data = json.loads(response.data)

        IP = data['ip']
        org = data['org']
        city = data['city']
        country = data['country']
        region = data['region']

        owm = pyowm.OWM('be6c5ecdf84f55df9764465d1725b7ce')
        observation = owm.weather_at_place(city + ',' + country.lower())
        w = observation.get_weather()

        return str(int(w.get_temperature('celsius')['temp']))



    def mainloop(self):
        self.speak('Hello, ' + self.name)
        while True:
            self.look_for_answer(self.record(), self.get_responses())
