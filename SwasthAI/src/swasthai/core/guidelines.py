from ..utils.logger import get_logger

class MedicalGuidelines:
    def __init__(self):
        self.logger = get_logger("MedicalGuidelines")
        self.guidelines = {
            "anemia": "Prescribe iron supplements, monitor hemoglobin levels.",
            "pregnancy": "Regular BP and glucose monitoring, refer to specialist if high-risk."
        }
        self.logger.info("MedicalGuidelines initialized")

    def get_guidelines(self, risks):
        self.logger.debug(f"Fetching guidelines for risks: {risks}")
        guidelines = [self.guidelines.get(risk, "No specific guidelines") for risk in risks]
        self.logger.debug(f"Guidelines: {guidelines}")
        return guidelines