import  os
class Config:
    SECRET_KEY=os.urandom(32)
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:111@localhost:5432/flask"


project_config = {
    'dev': DevelopmentConfig,
    "prd": ProductionConfig
}