from google.cloud import bigquery
from datetime import datetime
import base64, json, sys, os, calendar

def pubsub_to_bigquery(event, context):
   pubsub_message = base64.b64decode(event['data']).decode('utf-8')
   print(context.timestamp)
   print(event)
   timestamp = datetime.strptime(context.timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
   timestamp = datetime.strftime(timestamp, "%Y%m%d%H%M%S")
   pubsub_message=pubsub_message.replace("}", ",")
   pubsub_message=pubsub_message + "\"timestamp\":{}{}".format(timestamp, "}")
   print(pubsub_message)
   to_bigquery(os.environ['dataset'], os.environ['table'], json.loads(pubsub_message))

def to_bigquery(dataset, table, document):
   bigquery_client = bigquery.Client()
   dataset_ref = bigquery_client.dataset(dataset)
   table_ref = dataset_ref.table(table)
   table = bigquery_client.get_table(table_ref)
   errors = bigquery_client.insert_rows(table, [document])
   if errors != [] :
      print(errors, file=sys.stderr)
