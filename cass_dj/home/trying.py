import uuid
from cassandra.cluster import Cluster 
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import columns
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table

class DB(Model):
    __table_name__='p_name'
    __keyspace__='model'
    __connection__='cluster2'

    # pid=columns.UUID(default=uuid.uuid4)
    first_name=columns.Text(primary_key=True)
    in_stock=columns.Integer(partition_key=True)

    def getdata(self):
        return {
            'name':self.first_name,
            'pid':self.pid,
            'instock':self.in_stock
        }
def cassandratests():
    cluster = Cluster(['0.0.0.0'],port=9042)
    session = cluster.connect()
    connection.register_connection('cluster2',session=session)
    # create_keyspace_simple('model', 1, connections=['cluster2'])

if __name__ == '__main__':
    cassandratests()
    sync_table(DB)
    DB.create(first_name='akshay',in_stock=12)
    DB.save()

    db= DB.objects.all()
    print(db)
    
# cluster = Cluster(['0.0.0.0'],port=9042)
# session = cluster.connect()
# row = session.execute("SELECT pid from model.final_product_byname2 ;")
# for r in row:
#     i= r[0]
# print(type(i), i)