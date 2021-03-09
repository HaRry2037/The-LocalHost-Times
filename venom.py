#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
from colorama import Fore
import random
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
yellow = Fore.YELLOW
colors = (white, green, red, cyan, yellow)
color = random.choice(colors)
banner = '''
████████╗██╗  ██╗███████╗    ██╗      ██████╗  ██████╗ █████╗ ██╗     ██╗  ██╗ ██████╗ ███████╗████████╗    ████████╗██╗███╗   ███╗███████╗███████╗
╚══██╔══╝██║  ██║██╔════╝    ██║     ██╔═══██╗██╔════╝██╔══██╗██║     ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ╚══██╔══╝██║████╗ ████║██╔════╝██╔════╝
   ██║   ███████║█████╗      ██║     ██║   ██║██║     ███████║██║     ███████║██║   ██║███████╗   ██║          ██║   ██║██╔████╔██║█████╗  ███████╗
   ██║   ██╔══██║██╔══╝      ██║     ██║   ██║██║     ██╔══██║██║     ██╔══██║██║   ██║╚════██║   ██║          ██║   ██║██║╚██╔╝██║██╔══╝  ╚════██║
   ██║   ██║  ██║███████╗    ███████╗╚██████╔╝╚██████╗██║  ██║███████╗██║  ██║╚██████╔╝███████║   ██║          ██║   ██║██║ ╚═╝ ██║███████╗███████║
   ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝          ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝        


''' 
author = 'Venom 🐍 (Gaurav Chaudhary)'
team = 'From Team Venom 🐍'
facebook = 'https://facebook.com/venomgrills'
insta = 'https://instagram.com/i.m.gauravchaudhary'
github = 'https://github.com/venomsec-Dev/'
print(color + banner + color)
print(color + '   Author: ' + color + green + author + green)
print(color + '   Team: ' + color + red + team + red)
print(color + '   Facebook: ' + color + yellow + facebook + yellow)
print(color + '   Insta: ' + color + cyan + insta + cyan)
print(color + '   Github: ' + color + white + github + white)
urls = ['https://thehackernews.com/','https://thehackernews.com/search/label/Cyber%20Attack','https://thehackernews.com/search/label/Vulnerability','https://thehackernews.com/search/label/data%20breach','https://thehackernews.com/search/label/Malware']
print('\n \n')
print(white + '   [+] ' + white + color + '---------------' + color + green + ' Menu Bar ' + green + color + '---------------' + color + white + '[+]')
menu = '''
    {[0]} Latest Cyber News
    {[1]} Latest Cyber Attacks
    {[2]} Latest Vulnerability
    {[3]} Latest Data Breach
    {[4]} Latest Malware
'''
links = []
headlines = []
print(color + menu + color)
option = int(input(red + '[ ' + red + white + '+' + white + red + ' ] ' + red + color + 'Enter an option to continue: ' + color))
def titles(x):
    response = requests.get(urls[x])
    soup = BeautifulSoup(response.content, 'html.parser')
    print(' ')
    for i in soup.findAll('a', class_="story-link"):
        link = i.get('href')
        links.append(link)
    x = 0
    print(cyan + '     [+] ' + cyan + yellow + '-------------------------' + yellow + green + ' Latest News ' + green + yellow + '------------------------' + yellow + cyan + ' [+]' + cyan)
    print('\n')
    for i in soup.findAll('h2', class_="home-title"):
        print(yellow + '     ['+ white + str(x) + white + yellow + '] ' + yellow + green + i.text + green)
        x += 1
        title = i.text
        headlines.append(title)
titles(option)
print('\n \n')
read = int(input(red + '[ ' + red + white + '+' + white + red + ' ]' + red + color + 'Enter an option to continue: ' + color))
def article(x):
    response = requests.get(links[x])
    soup = BeautifulSoup(response.content, 'html.parser')
    print(' ')
    print(white + '     [+]' + white + yellow + '-------------------------' + yellow + green + headlines[read] + green + yellow + '---------------------------' + yellow +white + '[+]')
    print(' ')
    for i in soup.findAll('p'):
        print(i.text)
article(read)
