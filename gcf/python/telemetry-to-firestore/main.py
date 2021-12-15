import base64
import json
import logging

from google.cloud import firestore
from datetime import datetime

db = firestore.Client()

def telemetry_to_firestore(event, context):  
    """Background Cloud Function to be triggered by Pub/Sub.
    This function gets executed when telemetry data gets
    send to IoT Core and consequently a Pub/Sub message
    gets published to the selected topic.
    
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    if 'data' not in event:
        raise ValueError('No telemetry data was provided!')

    payload = base64.b64decode(event['data']).decode('utf-8')
    telemetry = json.loads(payload)
    print(f'telemetry = {telemetry}')
    attributes = event['attributes']
    device_id = attributes['deviceId']
    timestamp = datetime.strptime(context.timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
    timestamp = timestamp.timestamp()
    print(f'timestamp = {timestamp}')

    _, doc_ref = db.collection('devices/%s/measurements' % device_id).add({
        'timestamp': timestamp,
        'temperature': telemetry['temperature'],
        'humidity': telemetry['humidity']
    })
    logging.info('Message with ID: ' + doc_ref.id)
