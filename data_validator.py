class DataValidator:
    @staticmethod
    def validate(data):
        errors = []
        if not (-20 <= data['temperature'] <= 36):
            errors.append("Temperature out of valid range.")
        if not (900 <= data['pressure'] <= 1100):
            errors.append("Pressure out of valid range.")
        if not (0 <= data['humidity'] <= 90):
            errors.append("Humidity out of valid range.")
        return errors
