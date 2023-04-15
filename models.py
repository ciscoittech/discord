from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    user_message = Column(String, nullable=False)
    bot_response = Column(String, nullable=False)
