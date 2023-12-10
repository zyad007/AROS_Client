from package.service.singletonMeta import SingletonMeta

BASE_URL = 'http://localhost:3000'

class UserServices(metaclass= SingletonMeta):
    def login(self, username, password):

        # POST Request to the server

        if(username == 'admin' and password == 'admin'):
            return True
        else:
            return False