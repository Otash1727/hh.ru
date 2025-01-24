"""
from .env import of Bot tokens and other information
"""
from environs import Env

env=Env()
env.read_env()

TOKEN : str=env.str('BOT_TOKEN')
BACK_UP_CHANNEL_ID : str=env.str('BACK_UP_CHANNEL_ID')
LOG_CHANNEL_ID :str = env.str('LOG_CHANNEL_ID')

#DATABASE SETTINGS INFO
NAME : str =env.str('NAME')
USER : str =env.str('USER')
PASSWORD : str =env.str('PASSWORD')
HOST : str=env.str('HOST')
PORT : str =env.str('PORT')

#Wildberries URL
URL : str =env.str('URL') 

#Help url
HELP_URL :str=env.str('HELP_URL')

#scheduler
INTERVAL_MINUTES :str=env.str('INTERVAL_MIN')


