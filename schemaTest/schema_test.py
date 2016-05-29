#coding:utf8
'''
schema扩展格式测试
'''
import json
import os
from jsonschema import Draft4Validator

class NotFoundSchemaError(Exception):
    '''找不到'''
    pass

def get_schema_file(typ=''):
    path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(path, 'schema_files'+os.sep+typ+'.json')
    with open(file_path, 'r') as f:
        schema_str = f.read()
    return schema_str

class SchemaTest(object):
    
    def __init__(self, schema_type):
        self.schema_type = schema_type
        self.schema_obj = self._get_schema_obj()
    
    def _get_schema_obj(self):
        try:
            schema_str = get_schema_file(typ=self.schema_type)
        except:
            raise NotFoundSchemaError
        schema_obj = Draft4Validator(json.loads(schema_str))
        return schema_obj
    def valide(self, data):
        self.schema_obj.validate(data)
        return True

if __name__ == "__main__":
    schema_obj = SchemaTest('product')
    print schema_obj.valide({"url":"111"})
    pass

