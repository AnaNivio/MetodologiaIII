from datetime import datetime
from .Client import Client


class Account:
    def __init__(self, number: int, total: float, client: Client):
        self._number = number
        self._total = total
        self._date_time_client = datetime.now()
        self._client = client

    def to_string(self):
        return "Number: " + str(self._number) + "\n Total: " + str(self._total) + "\n Date Time Client: " + str(self._date_time_client) + "\n Client:\n " + str(self._client.to_string())
