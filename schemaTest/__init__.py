#coding:utf8
'''
#Example
>>> from schemaTest import SchemaTest
>>> import schemaTest
>>> schema_obj = SchemaTest('product')

>>> data = {"url":"111"}  #need valide data
>>> print schema_obj.valide(data)

>>> print schemaTest.all_schemas
['album', 'recording', ...]
'''
import os
from .schema_test import SchemaTest

path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(os.path.join(path, 'schema_files'))
all_schemas = [filename.split('.')[0] for filename in files]

__all__ = [SchemaTest, all_schemas]
