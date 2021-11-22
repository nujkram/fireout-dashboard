from os import path
from split_settings.tools import include

if path.isfile('/home/vagrant/fireout-dashboard/envars/local-mark'):
    print('connecting to local-mark settings...')
    include('settings_collection/local-mark.py')
elif path.isfile('/app/test-server.env'):
    print('connecting to test-server settings...')
    include('settings_collection/test-server.py')
else:
    print('connecting to production settings...')
    include('settings_collection/production.py')