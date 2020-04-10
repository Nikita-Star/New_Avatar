from telethon import TelegramClient, sync
from config import *
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from datetime import datetime
import datetime as dt
from utils import *
import pytz
import time
client = TelegramClient('банан', api_id, api_hash)

client.start()
prev_update_time = ""

while True:
    
    if time_has_changed(prev_update_time):
        prev_update_time = convert_time_to_string(dt.datetime.now(pytz.timezone('Europe/Moscow')))
        prev_update_time = prev_update_time.replace(':','_')

        client(DeletePhotosRequest(client.get_profile_photos('me')))
        file = client.upload_file(f"time_images/{prev_update_time}.jpg")
        client(UploadProfilePhotoRequest(file))
        time.sleep(15)


            

        
