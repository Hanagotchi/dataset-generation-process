from datetime import datetime
from time import strftime, localtime
from typing import Optional
from repository.repository import Repository
import pandas as pd

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
    df.to_csv(f"exports/log_photos_{str(datetime.now()).replace(':', '-').replace(' ', '_')}", index=False)
    
def export_log_content(repository: Repository, from_date: datetime):
    result = repository.get_all_log_contets(from_date)   
    df = pd.DataFrame(result, columns=["plant_id", "title", "content"])
    df.to_csv(f"exports/log_content_{str(datetime.now()).replace(':', '-').replace(' ', '_')}", index=False)
