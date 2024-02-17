#!/usr/bin/env python

__author__      = "Rev3rsX"
__copyright__   = "Copyright 2024"
import requests
import random
from random import choice, choices, randint
import string
import os 
import time
import json
import colorama

if os.name =="nt":
    os.system("cls")
else:
    os.system("clear")
    

def generate_email():
    username = ''.join(random.choices(string.ascii_letters, k=8))
    domain = random.choice(["gmail.com", "duck.com", "bing.com", "yahoo.com"])
    email = f"{username}@{domain}"
    return email

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def get_random_name():
    url = "https://2ac3872a-1ec2-4e20-adc7-f5c819bc7216-00-3hjrdx8kd9abv.kirk.replit.dev/api/name.txt"
    response = requests.get(url)
    names_list = response.text.strip().split("\n")
    return random.choice(names_list)

def getBirthday():
        day = str(randint(1, 28))
        month = str(randint(1, 12))

        if int(month) < 10: month = "0" + month
        if int(day) < 10: day = "0" + day

        birthday = "-".join([str(randint(1910, 2004)), month, day])
        return birthday


def get_access_token():
    with open("spotify_token.txt", "r") as token_file:
        return token_file.read().strip()

def add_to_library(artist_id, access_token):
    url = "https://api-partner.spotify.com/pathfinder/v1/query"
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "variables": {
            "uris": [f"spotify:artist:{artist_id}"]
        },
        "operationName": "addToLibrary",
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "656c491c3f65d9d08d259be6632f4ef1931540ebcf766488ed17f76bb9156d15"
            }
        }
    }

    response = requests.post(url, headers=headers, json=data)
    return response

def followbot():
    
    with open("spotify_token.txt", "r", encoding="utf-8") as token_file:
        access_tokens = [line.strip() for line in token_file]

    
    artist_ids = input("Spotify Artist ID'lerini virgülle ayırarak girin: ").split(",")

    for access_token in access_tokens:
        access_token = access_token.replace("['", "")  
        access_token = access_token.replace("']", "")  
        for artist_id in artist_ids:
            response = add_to_library(artist_id, access_token)
            print(f"Artist ID: \033[91m{artist_id}\033[0m, Status Code: \033[92m{response.status_code}\033[0m,Response: \033[92m{response.text}\033[0m")
            
def streamer():
    #comming soon
def generate_account():
    #comming soon
def banner():
    banners = """\033[91m
┏┓     •┏    ┏┓┏┳┓┳┓┏┓┏┓┳┳┓  ┏┳┓    ┓┏┓
┗┓┏┓┏┓╋┓╋┓┏  ┗┓ ┃ ┣┫┣ ┣┫┃┃┃   ┃ ┏┓┏┓┃┗┓
┗┛┣┛┗┛┗┗┛┗┫  ┗┛ ┻ ┛┗┗┛┛┗┛ ┗   ┻ ┗┛┗┛┗┗┛\033[0mV1 Coded By Rev3rsX
  ┛       ┛                               
#1 Followers Bot
#2 Stream Bot
#3 Account Generator
"""


    print(banners)

email = generate_email()
passw = generate_password()
name = get_random_name()

banner()

protest = input("user0@L33t -> ")

if protest == "1":

    print("[!] - Followbot Started")
    
    followbot()

