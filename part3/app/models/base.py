#!/usr/bin/python3
import uuid
from datetime import datetime, timezone
from app.persistence import Base
from sqlalchemy import Column, String, DateTime


class BaseModel(Base):
    __abstract__ = True

    id = Column(String(60),
                primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime,
                        default=datetime.now(timezone.utc))
    updated_at = Column(DateTime,
                        default=datetime.now(timezone.utc),
                        onupdate=datetime.now(timezone.utc))

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = datetime.now(timezone.utc)

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now(timezone.utc)

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp
