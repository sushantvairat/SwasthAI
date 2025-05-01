import unittest
from swasthai.core.risk_detection import RiskDetection

class TestRiskDetection(unittest.TestCase):
    def setUp(self):
        self.risk_detector = RiskDetection()

    def test_high_risk_pregnancy(self):
        patient_data = {"bp": 150, "glucose": 150, "hemoglobin": 12, "age": 36}
        risks = self.risk_detector.detect_risk(patient_data)
        self.assertIn("High-risk pregnancy (BP)", risks)
        self.assertIn("High-risk pregnancy (Glucose)", risks)

    def test_anemia(self):
        patient_data = {"bp": 120, "glucose": 100, "hemoglobin": 10, "age": 30}
        risks = self.risk_detector.detect_risk(patient_data)
        self.assertIn("Anemia", risks)

if __name__ == "__main__":
    unittest.main() 
