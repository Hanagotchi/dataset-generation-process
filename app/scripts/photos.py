from datetime import datetime
from time import strftime, localtime
from typing import Optional
from repository.repository import Repository
import pandas as pd

# https://firebasestorage.googleapis.com/v0/b/hanagotchi.appspot.com/o/plants%2F32%2F1713821959741?alt=media&token=c3f13738-61ad-4d5a-b38b-470b7c9fdb7e

MILISECONDS = 1000

def get_timestamp_from_photo_link(photo_link: str) -> Optional[datetime]:
    try:
        epoch = photo_link.split('?alt')[0].split('%2F')[-1]
        return strftime('%Y-%m-%d %H:%M:%S', localtime(int(epoch) / MILISECONDS))
    except Exception as e:
        return None
    

def export_log_photos(repository: Repository, from_date: datetime):
    result = repository.get_all_photo_links(from_date)   
    df = pd.DataFrame(result, columns=["plant_id", "photo_link"])
    df["created_at"] = df['photo_link'].map(get_timestamp_from_photo_link)
    df.to_csv(f"exports/photos_{str(datetime.now()).replace(':', '-').replace(' ', '_')}", index=False)
    #return list(map(lambda row: (*row, get_timestamp_from_photo_link(row[1])), result)) 
