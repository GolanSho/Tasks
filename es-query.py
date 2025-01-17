from logging import error
from elastic_transport.client_utils import to_str
import elasticsearch
from elasticsearch import Elasticsearch

cluster_endpoint = "http://80.2.67.1:9200/"
es_cls_ver = (8,6,1)
py_es_ver = elasticsearch.__version__

index = 0

for ver in py_es_ver:
    if ver > es_cls_ver[index]:
        error("Version of elasticsearch python package is bigger then the ES Cluster Ver.\nPackage Ver Should be =< Cluster Ver.")
        exit(1)
    index+=1

es = Elasticsearch(cluster_endpoint)

if es.ping():
    res = es.cluster.health()
    print(f"Cluster Status: {res.body['status']}\n")
    print("Nodes Info:")
    print(es.cat.nodes(v='true'))
    print("Documents Info:")
    print(es.count())
    exit(res.meta.status)
else:
    error("No Connection to Cluster.")
    exit(1)