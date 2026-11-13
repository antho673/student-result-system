def calculate_class_stats(students_dict):
    """Calculates class highest, lowest, and average scores."""
    if not students_dict:
        return None
    
    averages = [s.calculate_average() for s in students_dict.values() if s.scores]
    if not averages:
        return {"highest": 0.0, "lowest": 0.0, "class_average": 0.0}
    
    return {
        "highest": max(averages),
        "lowest": min(averages),
        "class_average": sum(averages) / len(averages)
    }

def sort_students(students_dict, by="average", reverse=True):
    """Sorts students by average score or name."""
    students_list = list(students_dict.values())
    if by == "average":
        students_list.sort(key=lambda x: x.calculate_average(), reverse=reverse)
    elif by == "name":
        students_list.sort(key=lambda x: x.full_name, reverse=not reverse)
    return students_list

def generate_text_report(students_dict, filename="class_performance_report.txt"):
    """Generates a text-based report and saves it to a file."""
    stats = calculate_class_stats(students_dict)
    sorted_studs = sort_students(students_dict, by="average", reverse=True)
    
    report_lines = []
    report_lines.append("=" * 65)
    report_lines.append("            STUDENT RESULT MANAGEMENT SYSTEM - REPORT")
    report_lines.append("=" * 65)
    report_lines.append(f"Total Registered Students: {len(students_dict)}")
    
    if stats:
        report_lines.append(f"Class Highest Average    : {stats['highest']:.2f}%")
        report_lines.append(f"Class Lowest Average     : {stats['lowest']:.2f}%")
        report_lines.append(f"Overall Class Average    : {stats['class_average']:.2f}%")
    report_lines.append("-" * 65)
    report_lines.append(f"{'ID':<10} | {'Full Name':<20} | {'Class':<10} | {'Total':<8} | {'Average':<8} | {'Grade':<5}")
    report_lines.append("-" * 65)
    
    for s in sorted_studs:
        total = s.calculate_total()
        avg = s.calculate_average()
        grade = s.get_grade()
        report_lines.append(f"{s.student_id:<10} | {s.full_name:<20} | {s.class_name:<10} | {total:<8.1f} | {avg:<8.1f} | {grade:<5}")
    
    report_lines.append("=" * 65)
    report_content = "\n".join(report_lines)
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_content)
        print(f"✔ Report successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving report file: {e}")
        
    return report_content