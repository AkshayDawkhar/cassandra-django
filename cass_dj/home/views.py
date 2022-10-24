from django.shortcuts import render
from cassandra.cluster import Cluster
# Create your views here.
def homes(requset):
    cluster= Cluster(['0.0.0.0'],port=9042)
    session = cluster.connect("test_ks")
    rows= session.execute("SELECT * FROM test_ks.user_dtl ;")
    for row in rows:
        print(row.user_id,type(row))

    return render(requset,'home.html')
