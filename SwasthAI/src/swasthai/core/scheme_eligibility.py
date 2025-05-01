from ..utils.logger import get_logger

class SchemeEligibility:
    def __init__(self):
        self.logger = get_logger("SchemeEligibility")
        self.schemes = {
            "PMJAY": {"income": 500000, "conditions": ["pregnancy", "anemia"]},
            "StateHealth": {"income": 300000, "conditions": ["anemia"]}
        }
        self.logger.info("SchemeEligibility initialized")

    def map_schemes(self, patient_data, risks):
        self.logger.debug(f"Mapping schemes for patient: {patient_data.get('name')}")
        eligible_schemes = []
        for scheme, criteria in self.schemes.items():
            if patient_data.get("income", float("inf")) <= criteria["income"]:
                if any(cond in risks for cond in criteria["conditions"]):
                    eligible_schemes.append(scheme)
        self.logger.debug(f"Eligible schemes: {eligible_schemes}")
        return eligible_schemes 
