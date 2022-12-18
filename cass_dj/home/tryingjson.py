from cassandra.cluster import Cluster
from cassandra.query import dict_factory
import json
cluser =Cluster(['0.0.0.0'],port=9042)
session = cluser.connect()
session.row_factory= dict_factory
row = session.execute("SELECT * FROM  model.tryjson ;")
# for r in row:
#     print(dict(r))

# r=row.one()
# d=dict(r['setudt'])
# print(r['setudt'])
# print(d)
def getit():
    cluser =Cluster(['0.0.0.0'],port=9042)
    session = cluser.connect()
    session.row_factory= dict_factory
    row = session.execute("SELECT * FROM  model.pro;")
    
    return row.all()
# for r in row:
#     if not r[2]['row1']:
#         print("adesh plz provide value")
#     else:
#         print(r[2]['row1'])

# j=json.dumps(row.one())
# jl=json.loads(row.one())
# print(jl)
def addit(s):
    cluser =Cluster(['0.0.0.0'],port=9042)
    session = cluser.connect()
    session.row_factory= dict_factory
    print("-----------------------------------------------------=----------------=----------------")
    js=json.dumps(s)
    print(js,type(js))
    # print("INSERT INTO model.tryjson JSON '"+js+"'")
    ss="INSERT INTO model.pro JSON '"+js+"'"
    print(ss)
    # sp=session.prepare("INSERT INTO model.tryjson JSON ? ")
    session.execute(ss)
    row = session.execute("SELECT * FROM model.pro ;")
    # r=dict(row.all())
    print(row)
    return row.all() 