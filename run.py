'''
run

This is the "main" method for the star-tides KB app.
'''

import os
from star_tides.create_app import create_app

_DEFAULT_PORT = 5000

if __name__ == '__main__':
    # Start the server on the port given by kNative/Cloud Run.
    port = int(os.getenv('PORT', str(_DEFAULT_PORT)))
    print(f'starting up server on port {port}')
    create_app().run(host='0.0.0.0', port=port)
