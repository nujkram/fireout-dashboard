from os import path
from split_settings.tools import include

if path.isfile('/app/dev.env'):
    print('connecting to development settings...')
    include('settings_collection/dev.py')
elif path.isfile('/app/prod.env'):
    print('connecting to production settings...')
    include('settings_collection/production.py')