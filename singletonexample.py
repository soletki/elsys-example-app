class Config:
    _instance = None

    def __new__(cls, db_url=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db_url = db_url
        return cls._instance


if __name__ == "__main__":
    c1 = Config("localhost")
    c2 = Config("prod-db")

    print(c1.db_url)  # localhost
    print(c2.db_url)  # localhost
