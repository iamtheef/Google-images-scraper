import os
import uuid
import time
from pathlib import Path
import requests
from progress_bar import printProgressBar


def _download(path, url):
    _filename = str(uuid.uuid4())
    try:
        Path(os.path.join(path + _filename + '.jpg')).touch()
        f = open(os.path.join(path + _filename + '.jpg'), 'wb')
        f.write(requests.get(url).content)
        f.close()
    except:
        print('There was an error while donwloading')


def print_progress(self, l):
    items = list(range(0, 57))
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)
    for i, item in enumerate(items):
        time.sleep(0.1)
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)
