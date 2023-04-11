import json
import boto3
import datetime
from main import sample


def lambda_handler(event, context):
    cloudwatch = boto3.client("cloudwatch")
    metric_name = "FunctionSuccess"
    timestamp = datetime.datetime.utcnow()
    unit = "None"
    try:
        sample()
    except:
        metric_value = 2
    else:
        metric_value = 1
        
    response = cloudwatch.put_metric_data(
        MetricData=[
            {
                "MetricName": metric_name,
                "Value": metric_value,
                "Timestamp": timestamp,
                "Unit" : unit
                
            },
        ],
        Namespace="custom_metric",
    )
    return {"metric value": metric_value}
