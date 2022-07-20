from builder import Builder

class Decrypt:
    def __init__(self, orc_list, p) -> None:
        self.orc_list = orc_list
        self.p = p

    def run(self):
        share_amount = int(input("How many shares would you like to build back from (how many orcs will be queried): "))
        b = Builder(self.orc_list, share_amount)
        b.request_orc_shares()

        secret = b.generate_orc_secrets(self.p)

        print(secret)
