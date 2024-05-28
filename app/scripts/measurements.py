from datetime import datetime
from repository.repository import Repository
import pandas as pd

def export_measurements(repository: Repository, from_date: datetime):
    result = repository.get_all_measurements(from_date)
    df = pd.DataFrame(result, columns=['id', 'id_plant', 'plant_type', 'time_stamp', 'temperature', 'humidity', 'light', 'watering'])
    df.to_csv(f"exports/measurements_{str(datetime.now()).replace(':', '-').replace(' ', '_')}", index=False)