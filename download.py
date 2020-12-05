import os
import uuid
from pathlib import Path
import requests



def _download(path, url):
    _filename = str(uuid.uuid4())
    try:
        Path(os.path.join(path + _filename + '.jpg')).touch()
        f = open(os.path.join(path + _filename + '.jpg'), 'wb')
        f.write(requests.get(url).content)
        f.close()
    except:
        print('There was an error while downloading')


