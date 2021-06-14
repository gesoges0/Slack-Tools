from pathlib import Path
from dataclasses import dataclass

TOKNE_FILE = '../../token_file.txt'
INCOMING_WEBHOOK_FILE = '../../incoming_webhook_url.txt'


@dataclass
class Option:
    token: str = ''
    incoming_webhook_url: str = ''

    def __post_init__(self):
        with open(INCOMING_WEBHOOK_FILE) as f:
            self.incoming_webhook_url = f.read().replace('\n', '')






    # def _get(path):
    #     with open(path) as f:
    #         token:str = f.read().replace('\n','')
    #     return token
