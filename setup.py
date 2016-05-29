# coding:utf-8
try:
    from setuptools import setup
    kw = {
        'install_requires':[
            'jsonschema',
            ],
        }
except ImportError:
    from distutils.core import setup
    kw = {}

setup(
    name = 'schemaTest',
    version = '0.4',
    description = 'schema test for quixey',
    packages = ['schemaTest'],
    #py_modules = ['jsonschema'],
    author = 'dyf',
    author_email = '1821367759@qq.com',
    package_data={'schemaTest':['schema_files/*.json']},
    **kw
    )

