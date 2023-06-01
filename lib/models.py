#!/usr/bin/env python3

from sqlalchemy import (Column, String, Integer, PrimaryKeyConstraint)
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'
    __table_args__ = (
        PrimaryKeyConstraint(
            'id',
            name = "pk_id"
        ),
    )

    id = Column(Integer())
    name = Column(String())
    breed = Column(String())

