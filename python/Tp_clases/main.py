from models.Client import Client
from models.Account import Account
from repositories.AccountRepository import AccountRepository
from repositories.ClientRepository import ClientRepository


def main():
    client = Client("Ana", 20, "ana@ana")
    clientrepository = ClientRepository()
    account = Account(1234, 20000, client)
    accountrepository = AccountRepository()

    clientrepository.save(client)
    accountrepository.save(account)
    print("clientes")
    clientrepository.get()
    print("cuentas")
    accountrepository.get()


if __name__ == "__main__":
    main()
