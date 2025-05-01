 
from .risk_detection import RiskDetection
from .multilingual_support import MultilingualSupport
from .offline_data import OfflineDataManager
from .scheme_eligibility import SchemeEligibility
from .recommendations import RecommendationEngine
from .guidelines import MedicalGuidelines
from .reporting import DataReporting
from ..utils.logger import get_logger
from ..utils.config import load_config
import threading

class SwasthAI:
    def __init__(self, config_path="config/config.json"):
        self.logger = get_logger("SwasthAI")
        self.config = load_config(config_path)
        self.risk_detector = RiskDetection()
        self.multilingual = MultilingualSupport()
        self.data_manager = OfflineDataManager(db_path=self.config.get("db_path", "data/swasthai_data.db"))
        self.scheme_mapper = SchemeEligibility()
        self.recommender = RecommendationEngine()
        self.guidelines = MedicalGuidelines()
        self.reporter = DataReporting()
        self.logger.info("SwasthAI initialized")

    def process_patient(self, patient_data, language="en"):
        self.logger.info(f"Processing patient: {patient_data['name']}")
        self.multilingual.set_language(language)
        
        risks = self.risk_detector.detect_risk(patient_data)
        schemes = self.scheme_mapper.map_schemes(patient_data, risks)
        recommendations = self.recommender.get_diet_recommendation(risks)
        doctor_guidelines = self.guidelines.get_guidelines(risks)
        
        patient_data["timestamp"] = patient_data.get("timestamp", datetime.now().isoformat())
        self.data_manager.save_patient_data(patient_data)
        
        report = self.reporter.generate_report(patient_data, risks, schemes, recommendations)
        
        self.multilingual.text_to_voice(f"Risks detected: {', '.join(risks)}. Eligible schemes: {', '.join(schemes)}")
        
        self.logger.info("Patient processing complete")
        return report

if __name__ == "__main__":
    from datetime import datetime
    swasth = SwasthAI()
    patient_data = {
        "name": "Anita",
        "bp": 145,
        "glucose": 150,
        "hemoglobin": 10,
        "income": 400000,
        "age": 36
    }
    report = swasth.process_patient(patient_data, language="en")
    print(report)
    
    sync_thread = threading.Thread(target=swasth.data_manager.sync_data)
    sync_thread.start()