import json
import os
from Student import Student

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "students.json")

def save_data(students_dict):
    """Saves all student records to a JSON file."""
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        
        data_to_save = {s_id: student.to_dict() for s_id, student in students_dict.items()}
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4)
        print("✔ Data successfully saved to storage.")
    except Exception as e:
        print(f"Error: An error occurred while saving data: {e}")

def load_data():
    """Loads student records from JSON file on startup. Handles missing or corrupted files."""
    students_dict = {}
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for s_id, s_data in data.items():
                    students_dict[s_id] = Student.from_dict(s_data)
            print(f"✔ Loaded {len(students_dict)} student record(s) from storage.")
        else:
            print("ℹ No existing data file found. Starting with a fresh database.")
    except json.JSONDecodeError:
        print("⚠ Warning: Data file is corrupted or empty. Starting with a fresh database.")
    except Exception as e:
        print(f"⚠ Unexpected error while loading data: {e}")
    finally:
        return students_dict