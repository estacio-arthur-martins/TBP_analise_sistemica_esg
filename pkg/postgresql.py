from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

class AzurePostgreSQL:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None
        self.session = None
    
    def create_engine(self):
        db_url = f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"
        self.engine = create_engine(db_url)
    
    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def execute(self, query):
        with self.session.begin() as session:
            result = session.execute(query)
        return result.fetchall()
