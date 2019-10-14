from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cluster = Cluster(
    cloud={
        'secure_connect_bundle': '/Users/matthew.miller/cassandra/secure-connect-mattsdb2.zip'
    },
    auth_provider=PlainTextAuthProvider('mmiller', 'cassandra')
)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")