from datetime import datetime

class Student:
    """Represents a student with personal details and academic scores."""
    
    def __init__(self, student_id, full_name, class_name, gender, dob, scores=None, date_added=None):
        self.student_id = student_id
        self.full_name = full_name
        self.class_name = class_name
        self.gender = gender
        self.dob = dob
        self.scores = scores if scores is not None else {}  # Dictionary: {subject: score}
        self.date_added = date_added if date_added is not None else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total(self):
        """Calculates the sum of all recorded subject scores."""
        if not self.scores:
            return 0.0
        return sum(self.scores.values())

    def calculate_average(self):
        """Calculates the average score across recorded subjects."""
        if not self.scores:
            return 0.0
        return self.calculate_total() / len(self.scores)

    def get_grade(self):
        """Assigns a letter grade based on the average score."""
        avg = self.calculate_average()
        if not self.scores:
            return "N/A"
        if avg >= 70:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def to_dict(self):
        """Converts student object to a dictionary for JSON serialization."""
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "class_name": self.class_name,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "date_added": self.date_added
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student instance from a dictionary loaded from JSON."""
        return cls(
            student_id=data["student_id"],
            full_name=data["full_name"],
            class_name=data["class_name"],
            gender=data["gender"],
            dob=data["dob"],
            scores=data.get("scores", {}),
            date_added=data.get("date_added")
        )