import chardet
from pydantic import BaseModel, Field

import debugpy

debugpy.connect(("localhost", 5678))

class MyModel(BaseModel):
    val: int = 0

BaseModel.parse_obj({'val': '1'})  # breakpoint here

chardet.detect(b'foobar')  # breakpoint here

Field()