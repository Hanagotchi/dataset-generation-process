from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from os import environ
from models.Log import Log, LogPhoto

from typing import Optional, Sequence
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
    def get_all_measurements(self, from_date: Optional[date] = None) -> Sequence[Measurement]:
        query = select(Measurement)
        
        if from_date:
            query = query.where(Measurement.time_stamp >= from_date)
        
        result = self.session.scalars(query).all()
        return result
    
    @withSQLExceptionsHandle()
    def get_all_photo_links(self, from_date: Optional[date] = None) -> list[tuple[int, str]]:
        query = self.session.query(Log.plant_id, LogPhoto.photo_link) \
                            .join(LogPhoto, LogPhoto.log_id == Log.id)
                            
        if from_date:
            query = query.filter(Log.created_at >= from_date)

        result = query.all()
        return result
