import json

from src.config import lambda_client


def send_alarm_slack(alarm_name: str, new_state_reason: str) -> None:
    # Comentar para evitar mandar alerta a slack
    # return
    print("Sending alarm to slack")
    data = {
        "Records": [
            {
                "EventSource": "aws:sns",
                "EventVersion": "1.0",
                "Sns": {
                    "Type": "Notification",
                    "Subject": "My Alarm Subject",
                    "Message": json.dumps(
                        {
                            "AlarmName": alarm_name,
                            "AlarmDescription": "This is a sample alarm",
                            "NewStateReason": new_state_reason,
                            "Region": "us-west-2",
                            "Trigger": {
                                "Dimensions": [
                                    {"name": "InstanceId", "value": "i-0e1dd226ff359973e"}
                                ]
                            },
                            "NewStateValue": "ALARM",
                            "OldStateValue": "OK",
                        }
                    ),
                },
            }
        ]
    }
    lambda_client.invoke(
        FunctionName="send-cloudwatch-alarms-to-slack",
        InvocationType="Event",
        Payload=json.dumps(data),
    )
