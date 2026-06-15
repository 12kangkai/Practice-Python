import json
import pickle
import csv
from pathlib import Path
from dataclasses import dataclass
from typing import Any

# ============= JSON Serialization =============
def json_example():
    """JSON serialization - human readable, text-based"""
    data = {
        "name": "Alice",
        "age": 30,
        "skills": ["Python", "Java", "C++"],
        "active": True
    }
    
    # Serialize to JSON string
    json_str = json.dumps(data, indent=2)
    print("JSON String:", json_str)
    
    # Write to file
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    
    # Read from file
    with open("data.json", "r") as f:
        loaded_data = json.load(f)
    print("Loaded from JSON:", loaded_data)


# ============= Pickle Serialization =============
def pickle_example():
    """Pickle serialization - Python objects, binary format"""
    data = {
        "name": "Bob",
        "scores": [95, 87, 92],
        "metadata": {"created": "2024-01-01"}
    }
    
    # Serialize to bytes
    pickled = pickle.dumps(data)
    print("Pickled bytes:", pickled)
    
    # Write to file
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)
    
    # Read from file
    with open("data.pkl", "rb") as f:
        loaded_data = pickle.load(f)
    print("Loaded from pickle:", loaded_data)


# ============= CSV Serialization =============
def csv_example():
    """CSV serialization - tabular data"""
    data = [
        {"name": "Alice", "age": 30, "city": "NYC"},
        {"name": "Bob", "age": 25, "city": "LA"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    # Write to CSV
    with open("data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(data)
    
    # Read from CSV
    with open("data.csv", "r") as f:
        reader = csv.DictReader(f)
        loaded_data = list(reader)
    print("Loaded from CSV:", loaded_data)


# ============= Custom Class Serialization =============
@dataclass
class Person:
    name: str
    age: int
    email: str
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.__dict__)
    
    @classmethod
    def from_json(cls, json_str: str) -> "Person":
        """Create from JSON string"""
        data = json.loads(json_str)
        return cls(**data)


def custom_class_example():
    """Custom class serialization"""
    person = Person("David", 28, "david@example.com")
    
    # To JSON
    json_str = person.to_json()
    print("Person as JSON:", json_str)
    
    # From JSON
    restored = Person.from_json(json_str)
    print("Restored Person:", restored)


if __name__ == "__main__":
    print("=" * 50)
    print("JSON Serialization")
    print("=" * 50)
    json_example()
    
    print("\n" + "=" * 50)
    print("Pickle Serialization")
    print("=" * 50)
    pickle_example()
    
    print("\n" + "=" * 50)
    print("CSV Serialization")
    print("=" * 50)
    csv_example()
    
    print("\n" + "=" * 50)
    print("Custom Class Serialization")
    print("=" * 50)
    custom_class_example()