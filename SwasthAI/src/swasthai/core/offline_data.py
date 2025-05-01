import sqlite3
import json
from datetime import datetime
import queue
from ..utils.logger import get_logger

class OfflineDataManager:
    def __init__(self, db_path="data/swasthai_data.db"):
        self.logger = get_logger("OfflineDataManager")
        self.db_path = db_path
        self.offline_queue = queue.Queue()
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
        self.logger.info(f"OfflineDataManager initialized with DB: {db_path}")

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                data TEXT,
                timestamp TEXT,
                synced INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()
        self.logger.debug("Database tables created")

    def save_patient_data(self, patient_data):
        self.logger.debug(f"Saving patient data: {patient_data['name']}")
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO patients (name, data, timestamp, synced) VALUES (?, ?, ?, ?)",
            (patient_data["name"], json.dumps(patient_data), patient_data["timestamp"], 0)
        )
        self.conn.commit()
        self.offline_queue.put(patient_data)
        self.logger.info(f"Patient data saved for {patient_data['name']}")

    def sync_data(self):
        self.logger.info("Starting data sync")
        while not self.offline_queue.empty():
            patient_data = self.offline_queue.get()
            cursor = self.conn.cursor()
            cursor.execute(
                "UPDATE patients SET synced = 1 WHERE name = ? AND timestamp = ?",
                (patient_data["name"], patient_data["timestamp"])
            )
            self.conn.commit()
            self.logger.debug(f"Synced data for {patient_data['name']}") 
