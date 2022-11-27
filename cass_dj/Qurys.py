from cassandra.cluster import Cluster
import random_genrator
class DatabaseError(Exception):
# The base error that functions in this module will raise when things go wrong.
    print('database Error',Exception.mro())
    
class NotFound(DatabaseError):
    print('database not found',Exception)
class InvalidDictionary(DatabaseError):
    print('Invalid dic ',Exception)
class Qury:



    cluster = None
    session = None
    creat_data = None
    i=0
    def pri():
        print(self.cluster,session)
        print(self.cluster,session)


    def makedb(self):
        global cluster
        global session
        if self.cluster == None or self.session == None :
            print("\nmaking connection to the ip ")
            self.cluster = Cluster(['0.0.0.0'],port=9042)

            print("connecting ther session")
            self.session = self.cluster.connect()

        print("\nconnected to the ip.....")
        rows=self.session.execute("SELECT * FROM system_schema.keyspaces WHERE keyspace_name='model';")
        
        if rows:
            yn=input("you have an keyspace alredy name model\ndo you wnat to make a overwrite it\n (y/n,defult=y):")
            if not yn or yn[0] == 'y':
                self.session.execute("DROP KEYSPACE model;")
                print("you choos y ..................")
                self.making_key()
        else:

            self.making_key()
        self.session.set_keyspace('model')
        

    def making_key(self):
        
        global creat_data
        global session
        global i
        print("creating the database Keyspace")
        self.session.execute("CREATE KEYSPACE model WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1 };")
        
        self.session.set_keyspace('model')
        print("creating the database Table")
        self.session.execute("CREATE TABLE usertable ( userid uuid , id int, username text ,location text,PRIMARY KEY (id) );")
        
        if self.creat_data is None:
            print("creating the data qury.............")
            self.creat_data=self.session.prepare("INSERT INTO usertable (id , userid , username , location ) VALUES ( ?,uuid(),?,?) ;")
        for t in range(12):
            self.i+=1
            self.session.execute(self.creat_data,(self.i,random_genrator.userName(),'location'))

    def add_newuser(self,newuser):
        global creat_data
        global session
        global i
        
        if self.creat_data is None:
            print("creating the data qury.............")
            self.creat_data=self.session.prepare("INSERT INTO usertable (id , userid , username , location ) VALUES ( ?,uuid(),?,?) ;")
        
        for t in range(newuser):
            self.i+=1
            self.session.execute(self.creat_data,(self.i,random_genrator.userName(),'location-V2'))

