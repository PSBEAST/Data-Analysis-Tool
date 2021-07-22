import mysql.connector
from datetime import datetime
import hashlib, binascii, os

class Query():
    mydb = None
    mycursor = None

    def hash_password(self, password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def check_user(self, username):
        stmt = 'select exists(select * from login where username = \'{}\')'.format(username)
        self.mycursor.execute(stmt)
        ans  = self.mycursor.fetchall()
        return True if ans[0][0] == 1 else False

    def connect(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "prithvi",
            password = "",
            database = "db_chat"
        )
        self.mycursor = self.mydb.cursor(buffered= True)
    
    def disconnect(self):
        self.mydb.commit()
        self.mycursor.close()
        self.mydb.close()
    
    def display(self ,row_headers, data):
        data = [list(ele) for ele in data]
        c =[]
        for d in data:
            for i in range(0, len(d)):
                if type(d[i])  == datetime:
                    # print('im here\n' , d[i])
                    d[i] = d[i].strftime("%m-%d-%Y %H:%M:%S")
                    # print(d[i])
                elif type(d[i]) in [int, float]:
                    d[i] = str(d[i])
                elif type(d[i]) != str and d[i] is not None:
                    if i not in c:
                        c.append(i)
        for r in data:
            for i in c:
                r[i] = r[i].decode('utf-8')
        data  = [['None' if item is  None else item for item in r] for r in data]
        row_format = '{:20}' * len(row_headers)
        print(row_format.format(*row_headers))
        for row in data:
            print(row_format.format(*row))
    
    def sign_up(self, username , password, ques, ans):
        stmt = 'insert into login (username , password , '
        if ques == 1:
            stmt += 'mother_name ) values ( %s, %s, %s)'
        elif ques == 2:
            stmt += "pet_name ) values ( %s, %s, %s)"
        elif ques == 3:
            stmt += 'school_name ) values ( %s, %s, %s)'
        else:
            stmt += 'passcode ) values ( %s, %s, %s)'
        try:
            password = self.hash_password(password)
            self.mycursor.execute(stmt , (username, password, ans))
        except mysql.connector.Error as error:
            if error.errno == 1062:
                print('Username Already exists !!')
            elif error.errno == 1366:
                print('Invalid data type entry !!!')
            else :
                print('Something went wrong')
        except mysql.connector.ProgrammingError as error:
            print(error)

    def login_user(self, username, password):
        stmt = 'select password from login where username = \'{}\''.format(username)
        self.mycursor.execute(stmt)
        pwd = self.mycursor.fetchall()
        salt = pwd[0][0][:64]
        passd = pwd[0][0][64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')                                  
        if pwd:
            if pwdhash == passd :
                self.update_user(username, 'last_login', datetime.now())
                return True
            else:
                return False
        else:
            return False

    def show_records(self, table):
        stmt  = 'select * from {}'.format(table)
        self.mycursor.execute(stmt)
        self.display([x[0] for x in self.mycursor.description], self.mycursor.fetchall())

    def get_user(self, field, value, queIndex):
        stmt = ''
        if queIndex == 1: stmt = 'select mother_name from login where username = \'{}\''.format(value)
        elif queIndex == 2: stmt = 'select pet_name from login where username = \'{}\''.format(value)
        elif queIndex == 3: stmt = 'select school_name from login where username = \'{}\''.format(value)
        elif queIndex == 4: stmt = 'select passcode from login where username = \'{}\''.format(value)
        self.mycursor.execute(stmt)
        data = self.mycursor.fetchall()
        return data[0][0]

    def update_user(self, username , field , value):
        if field == 'password':
            hexhash = self.hash_password(value)
            stmt = 'update login set password = \'{}\' where username = \'{}\''.format(hexhash, username)
        elif field == 'passcode':
            stmt = 'update login set passcode = {} where username = \'{}\''.format(value, username)
        else:
            stmt = 'update login set {0} = \'{1}\' where username = \'{2}\''.format(field, value, username)
        self.mycursor.execute(stmt)
        self.show_records('login')


if __name__ == "__main__" :
    q = Query()
    q.connect()
    q.update_user("umang", 'password', "123")
    q.disconnect()
    q.connect()
    print(q.login_user('umang','456'))