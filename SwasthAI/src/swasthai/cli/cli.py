import argparse
from ..core.main import SwasthAI
from ..utils.logger import get_logger

def main():
    logger = get_logger("CLI")
    parser = argparse.ArgumentParser(description="SwasthAI CLI")
    parser.add_argument("--name", required=True, help="Patient name")
    parser.add_argument("--bp", type=float, default=120, help="Blood pressure")
    parser.add_argument("--glucose", type=float, default=100, help="Glucose level")
    parser.add_argument("--hemoglobin", type=float, default=12, help="Hemoglobin level")
    parser.add_argument("--income", type=float, default=500000, help="Annual income")
    parser.add_argument("--age", type=int, default=30, help="Patient age")
    parser.add_argument("--language", default="en", help="Language code (e.g., en, hi)")
    
    args = parser.parse_args()
    
    patient_data = {
        "name": args.name,
        "bp": args.bp,
        "glucose": args.glucose,
        "hemoglobin": args.hemoglobin,
        "income": args.income,
        "age": args.age
    }
    
    logger.info(f"Starting CLI processing for patient: {args.name}")
    swasth = SwasthAI()
    report = swasth.process_patient(patient_data, language=args.language)
    print(report)

if __name__ == "__main__":
    main() 
