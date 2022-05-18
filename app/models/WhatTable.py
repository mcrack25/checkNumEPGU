import datetime
from peewee import *
from app.models.BaseModel import BaseModel

class WhatTable(BaseModel):
    snils = CharField(max_length=11, null=True)
    request_date = CharField(max_length=128, null=True)
    serviceid = CharField(max_length=128, null=True)

    file_name = CharField(max_length=256, null=False)
    num_row = IntegerField(null=False)

    created_at = DateTimeField(default=datetime.datetime.now())
    updated_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = "what_table"
        order_by = ('created_at')