import unittest
import sqlite3
from swasthai.core.offline_data import OfflineDataManager

class TestOfflineDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = OfflineDataManager(db_path=":memory:")

    def test_save_patient_data(self):
        patient_data = {"name": "Test", "bp": 120, "timestamp": "2025-05-01T00:00:00"}
        self.data_manager.save_patient_data(patient_data)
        cursor = self.data_manager.conn.cursor()
        cursor.execute("SELECT name FROM patients WHERE name = ?", ("Test",))
        result = cursor.fetchone()
        self.assertEqual(result[0], "Test")

if __name__ == "__main__":
    unittest.main() 
