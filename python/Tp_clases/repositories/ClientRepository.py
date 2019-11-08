from models.Client import Client


class ClientRepository:
    def __init__(self):
        self._id = 1
        self._client_array = {}

    def save(self, client: Client):
        self._client_array[self._id] = client
        self._id = self._id + 1

    def get(self):
        for i in range(len(self._client_array)):
            client = self._client_array[i+1]
            print(client.to_string())

