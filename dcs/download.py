import requests
import os
from os import path
import random
import string


class Download:

    def __init__(self, loc='./out'):
        self.loc = loc
        if not path.isdir(loc) and not path.isfile(loc):
            os.makedirs(loc)

    def _download(self, url, filename=None):
        if url is None or len(url) == 0:
            return

        res = requests.get(url, stream=True)
        if res.status_code != 200:
            print('[ERR ] faield downloading image {} - Response code was {}'.format(url, res.status_code))
            return

        mimetype = res.headers.get('content-type')
        if mimetype is None or 'text/html' in mimetype:
            return

        if filename is None:
            filename = url.split('/')[-1].split('?')[0].split('&')[0].split(':')[0].split('#')[0]

        if len(filename) == 0:
            letters = string.ascii_lowercase
            filename = ''.join(random.choice(letters) for i in range(16))

        if len(filename.split('.')) < 2:
            mimetype = res.headers.get('content-type')
            if len(mimetype) > 0 and len(mimetype.split('/')) > 1:
                filename += '.{}'.format(mimetype.split('/')[-1])

        try:
            with open('{}/{}'.format(self.loc, filename), 'wb') as f:
                for chunk in res:
                    f.write(chunk)
            print('[INFO] image {} saved as {}'.format(url, filename))
        except Exception as e:
            print('[ERR ] faield saving image: {}'.format(e))

    def download_image_from_message(self, msg, name=None):
        if msg is None:
            return

        attachments = msg.get('attachments')
        embeds = msg.get('embeds')

        if attachments is None and embeds is None:
            return

        if len(attachments) == 0 and len(embeds) == 0:
            return

        i = 0

        def __get_file_name(ind):
            return '{}-{}'.format(msg.get('id'), ind)

        for a in attachments:
            self._download(a.get('url'), filename=__get_file_name(i))

        for e in embeds:
            self._download(e.get('url'), filename=__get_file_name(i))
