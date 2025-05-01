import json
from datetime import datetime
from ..utils.logger import get_logger

class DataReporting:
    def __init__(self):
        self.logger = get_logger("DataReporting")
        self.logger.info("DataReporting initialized")

    def generate_report(self, patient_data, risks, schemes, recommendations):
        self.logger.debug(f"Generating report for patient: {patient_data['name']}")
        report = {
            "patient_name": patient_data["name"],
            "risks": risks,
            "eligible_schemes": schemes,
            "diet_recommendations": recommendations,
            "timestamp": datetime.now().isoformat()
        }
        report_str = json.dumps(report, indent=2)
        self.logger.debug(f"Report generated: {report_str}")
        return report_str 
