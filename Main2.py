class Patient:
    #Represents a patient's vital signs used to calculate the Medi Score.

    def __init__(self, oxygen_status, consciousness, respiration_rate, spo2, temperature):
        self.oxygen_status = oxygen_status  # 0 for air, 2 for oxygen
        self.consciousness = consciousness  # 0 for alert, non-zero for CVPU
        self.respiration_rate = respiration_rate  # Breaths per minute
        self.spo2 = spo2  # Oxygen saturation percentage
        self.temperature = round(temperature, 1)  # Rounded to 1 decimal place

def calculate_medi_score(patient):
    total_score = patient.oxygen_status  # Oxygen adds 2 points if patient is on oxygen

    # Consciousness: If the patient isn't fully alert, add 3 points
    total_score += 3 if patient.consciousness != 0 else 0

    # Add scores from respiration, SpO2, and temperature categories
    total_score += get_respiration_score(patient.respiration_rate)
    total_score += get_spo2_score(patient.spo2, patient.oxygen_status == 2)
    total_score += get_temperature_score(patient.temperature)

    return total_score

def get_respiration_score(rate):
    #Scores respiration rate based on ranges predefined
    if rate <= 8:
        return 3  # Critically low
    elif 9 <= rate <= 11:
        return 1  # Slightly low
    elif 12 <= rate <= 20:
        return 0  # Normal range
    elif 21 <= rate <= 24:
        return 2  # Slightly high
    elif rate >= 25:
        return 3  # Critically high
    return 0  # Default case (should never happen)

def get_spo2_score(value, on_oxygen):
    #Scores oxygen saturation levels based on whether the patient is on oxygen.
    if value <= 83:
        return 3  # Very low SpO2
    elif 84 <= value <= 85:
        return 2
    elif 86 <= value <= 87:
        return 1
    elif 88 <= value <= 92 or (value >= 93 and not on_oxygen):
        return 0  # Normal for someone breathing air
    elif on_oxygen and 93 <= value <= 94:
        return 1
    elif on_oxygen and 95 <= value <= 96:
        return 2
    elif on_oxygen and value >= 97:
        return 3  # Unusually high for someone on oxygen
    return 0  # Default case (should never happen)

def get_temperature_score(temp):
    #Scores body temperature based on risk levels.
    if temp <= 35.0:
        return 3  # Hypothermia risk
    elif 35.1 <= temp <= 36.0:
        return 1  # Slightly low
    elif 36.1 <= temp <= 38.0:
        return 0  # Normal range
    elif 38.1 <= temp <= 39.0:
        return 1  # Slightly high
    elif temp >= 39.1:
        return 2  # High fever
    return 0  # Default case (should never happen)

def test_examples():
    #Runs test cases for sample patients.
    patient1 = Patient(oxygen_status=0, consciousness=0, respiration_rate=15, spo2=95, temperature=37.1)
    patient2 = Patient(oxygen_status=2, consciousness=0, respiration_rate=17, spo2=95, temperature=37.1)
    patient3 = Patient(oxygen_status=2, consciousness=1, respiration_rate=23, spo2=88, temperature=38.5)

    print(f"Patient 1 Medi Score: {calculate_medi_score(patient1)}")
    print(f"Patient 2 Medi Score: {calculate_medi_score(patient2)}")
    print(f"Patient 3 Medi Score: {calculate_medi_score(patient3)}")
# Run the test cases
test_examples()
