class AlertSystem:
    def __init__(self):
        self.thresholds = {
            'temperature': 35  
        }

    def check_alerts(self, current_temp, condition):
        if current_temp > self.thresholds['temperature']:
            print(f"Alert! High temperature detected: {current_temp}°C in {condition}.")
