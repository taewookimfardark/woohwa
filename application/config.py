import os

class Config :
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = True
    @classmethod
    def init_app(cls,app):
        SCHEMA_NAME = "woo"
        if os.getenv('SERVER_SOFTWARE'):
            # google server
            if os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
                cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@127.0.0.1:3306/' \
                                                + SCHEMA_NAME + \
                                                '?unix_socket=/cloudsql/woohwa-1370:woo?charset=utf8'
            print "google server log"
        else:
            # local
            print "local run"
            cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://taewookim:1234@173.194.242.136:3306/' + SCHEMA_NAME

        app.config.from_object(cls)
        return app