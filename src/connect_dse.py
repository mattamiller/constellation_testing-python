from dse.cluster import Cluster
from dse.auth import PlainTextAuthProvider
import sys

print(sys.version)

cloud_config = {
    'secure_connect_bundle': '/Users/matthew.miller/cassandra/secure-connect-mattsdb2.zip'
}
cluster = Cluster(cloud=cloud_config, auth_provider=PlainTextAuthProvider('mmiller', 'cassandra'))
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")