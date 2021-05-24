from setuptools import setup 

setup(
    name='emailosint',

    version='1.0.0',
    description='Email OSINT',
    url='https://github.com/krishpranav',
    
    author = 'krishpranav',
    author_email='',
    license='GPLv3',

    install_requires = ['colorama','requests','urllib3'],
    console =['emailosint.py'],
)
