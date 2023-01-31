from opensearchpy import OpenSearch
from datetime import datetime as dt

host = [{'host': 'osearchtst.ppdp.int', 'port': 9200}]
auth = ('admin', 'admin')

client = OpenSearch(
    hosts=host,
    http_compress=True,
    http_auth=auth,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

#sid =
log_data = dt.today().strftime("%Y-%m-%d")
index = f'event_log-{log_data}'
query = {
  "query": {
    "query_string": {
      "query": "srv_key:\"sms-srv\" AND sid_key:\"1630fb5a-d167-489f-8df0-ca5971e7ec3e\""
    }
  },
  "size": 10,
  "from": 0,
  "sort": [
    {
      "method_key": {
        "unmapped_type": "keyword",
        "order": "asc"
      }
    }
  ]
}

response = client.search(
    body=query,
    index=index,
)

sms_key = response['hits']['hits'][0]['_source']['body'][31:37]
print(sms_key)
