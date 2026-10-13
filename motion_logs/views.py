import os
import requests
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MotionLogSerializer

load_dotenv()

TEXTBEE_API_KEY = os.getenv("TEXTBEE_API_KEY")
TARGET_PHONE_NUMBER = os.getenv("TARGET_PHONE_NUMBER")

def send_sms_alert(location, time):
    url = "https://api.textbee.dev/api/v1/gateway/send-sms"
    headers = {
        "x-api-key": TEXTBEE_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "recipients": [TARGET_PHONE_NUMBER],
        "message": f"ALERT: Motion detected at {location} at {time}."
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to send SMS: {e}")

@api_view(['POST'])
def create_motion_log(request):
    serializer = MotionLogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        send_sms_alert(
            location=serializer.validated_data['location'],
            time=serializer.validated_data['time'].strftime("%Y-%m-%d %H:%M:%S")
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)