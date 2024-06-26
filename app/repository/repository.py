from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from os import environ
from models.Log import Log, LogPhoto
from typing import Optional
from datetime import date
from models.measurement import Measurement
from utils.sql_exception_handling import withSQLExceptionsHandle

load_dotenv()

class Repository():
    db_url = environ.get("DATABASE_URL")\
        .replace("postgres://", "postgresql://", 1)

    engine = create_engine(db_url)

    def __init__(self):
        self.conn = self.engine.connect()
        self.session = Session(self.engine)

    def shutdown(self):
        self.conn.close()
        self.session.close()

    def rollback(self):
        self.session.rollback()

    @withSQLExceptionsHandle()
    def get_all_measurements(self, from_date: Optional[date] = None):
        query = self.session.query(Measurement.id,
                          Measurement.id_plant,
                          Measurement.plant_type,
                          Measurement.time_stamp,
                          Measurement.temperature,
                          Measurement.humidity,
                          Measurement.light,
                          Measurement.watering)
        
        if from_date:
            query = query.where(Measurement.time_stamp >= from_date)
        
        result = query.all()
        return result
    
    @withSQLExceptionsHandle()
    def get_all_photo_links(self, from_date: Optional[date] = None) -> list[tuple[int, str]]:
        query = self.session.query(Log.plant_id, LogPhoto.photo_link) \
                            .join(LogPhoto, LogPhoto.log_id == Log.id)
                            
        if from_date:
            query = query.filter(Log.created_at >= from_date)

        result = query.all()
        return result
    
    @withSQLExceptionsHandle()
    def get_all_log_contets(self, from_date: Optional[date] = None) -> list[tuple[int, str]]:
        query = self.session.query(Log.plant_id, Log.title, Log.content)      
         
        if from_date:
            query = query.filter(Log.created_at >= from_date)

        result = query.all()
        return result
