# -*- coding: utf-8 -*-
"""{{target.capitalize()}} model module."""
from sqlalchemy import *
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime, LargeBinary
from sqlalchemy.orm import relationship, backref

from githandler.model import DeclarativeBase, metadata, DBSession


class Payload(DeclarativeBase):
    __tablename__ = 'payloads'

    uid = Column(Integer, primary_key=True)
    data = Column(Unicode(255), nullable=False)
    user_id = Column(Integer, ForeignKey('tg_user.user_id'), index=True)
    user = relationship('User', uselist=False,
                        backref=backref('{{target.lower()}}s',
                                        cascade='all, delete-orphan'))


__all__ = ['Payload']
