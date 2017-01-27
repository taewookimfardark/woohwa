import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config :
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATION = True
    BUCKET_NAME = 'woowha_bucket'
    @classmethod
    def init_app(cls,app):
        SCHEMA_NAME = "bucket"
        if os.getenv('SERVER_SOFTWARE'):
            # google server
            if os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'):
                cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@127.0.0.1:3306/' \
                                                + SCHEMA_NAME + \
                                                '?unix_socket=/cloudsql/woowha-1370:bucket-woohwa?charset=utf8'
            print "google server log"
        else:
            # local
            print "local run"
            cls.SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@130.211.162.120:3306/' + SCHEMA_NAME

        app.config.from_object(cls)
        return app