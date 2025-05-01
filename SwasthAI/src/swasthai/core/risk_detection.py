from ..utils.logger import get_logger

class RiskDetection:
    def __init__(self):
        self.logger = get_logger("RiskDetection")
        self.risk_thresholds = {
            "pregnancy": {"bp": 140, "glucose": 140, "age": 35},
            "anemia": {"hemoglobin": 11}
        }
        self.logger.info("RiskDetection initialized")

    def detect_risk(self, patient_data):
        self.logger.debug(f"Detecting risks for patient data: {patient_data}")
        risks = []
        if patient_data.get("bp", 0) > self.risk_thresholds["pregnancy"]["bp"]:
            risks.append("High-risk pregnancy (BP)")
        if patient_data.get("glucose", 0) > self.risk_thresholds["pregnancy"]["glucose"]:
            risks.append("High-risk pregnancy (Glucose)")
        if patient_data.get("hemoglobin", 0) < self.risk_thresholds["anemia"]["hemoglobin"]:
            risks.append("Anemia")
        return risks 
