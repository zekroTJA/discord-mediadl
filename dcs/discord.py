import requests


class Discord:

    def __init__(self, token):
        self.USER_AGENT = 'DiscordMessageScript v0.1'
        self.API_URL = "https://discordapp.com/api"
        self.token = token

    def _req(self, method, url, body=None):
        headers = {
            'Authorization': 'Bot {}'.format(self.token)
        }

        res = requests.request(
            method=method,
            url='{}/{}'.format(self.API_URL, url),
            headers=headers,
            params=body)

        if res.status_code >= 400:
            raise Exception('Request failed: {}\n{}'.format(res.status_code, res.json()))

        return res

    def get_channel_messages(self, channel_id, limit=100, before=None, after=None):
        params = {
            'limit': limit,
            'before': before,
            'after': after,
        }
        res = self._req('GET', '/channels/{}/messages'.format(channel_id), params)
        return res.json()

    def get_all_channel_messages(self, channel_id):
        all_messages = []
        last_msg_id = None

        while True:
            res = self.get_channel_messages(channel_id, limit=100, before=last_msg_id)
            if len(res) == 0:
                break
            last_msg_id = res[-1]['id']
            all_messages.extend(res)
            print('Requested {} messages...'.format(len(all_messages)))

        return all_messages
