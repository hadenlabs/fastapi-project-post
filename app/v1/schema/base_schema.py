# -*- coding: utf-8 -*-
from datetime import datetime

from pydantic import BaseModel, Field


class CommonBase(BaseModel):
    created_at: datetime = Field(default=datetime.now())
    update_at: datetime = Field(default=datetime.now())
