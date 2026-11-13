from Student import Student
from results import validate_score
from storage import load_data, save_data
from reports import generate_text_report, sort_students, calculate_class_stats

def display_menu():
    print("\n" + "=" * 45)
    print("      STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add New Student")
    print("2. View All Registered Students")
    print("3. Search Student (by ID or Name)")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Record/Update Scores (5+ Subjects)")
    print("7. Display Individual Report Card")
    print("8. View Class Statistics & Sorted List")
    print("9. Generate & Save Text Report")
    print("10. Save and Exit")
    print("=" * 45)

def main():
    students = load_data()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-10): ").strip()
        
        if choice == "1":
            print("\n--- Add New Student ---")
            s_id = input("Enter Student ID (e.g., STU001): ").strip()
            if not s_id:
                print("Error: Student ID cannot be empty.")
                continue
            if s_id in students:
                print("Error: A student with this ID already exists.")
                continue
            
            name = input("Enter Full Name: ").strip()
            class_name = input("Enter Class/Form (e.g., SS2): ").strip()
            gender = input("Enter Gender (M/F/Other): ").strip()
            dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()
            
            new_student = Student(s_id, name, class_name, gender, dob)
            students[s_id] = new_student
            save_data(students)
            print(f"✔ Student {name} added successfully!")

        elif choice == "2":
            print("\n--- All Registered Students ---")
            if not students:
                print("No student records found.")
            else:
                print(f"{'ID':<10} | {'Name':<20} | {'Class':<10} | {'Gender':<8} | {'DOB':<12}")
                print("-" * 68)
                for s in students.values():
                    print(f"{s.student_id:<10} | {s.full_name:<20} | {s.class_name:<10} | {s.gender:<8} | {s.dob:<12}")

        elif choice == "3":
            print("\n--- Search Student ---")
            query = input("Enter Student ID or Full Name to search: ").strip().lower()
            found = [s for s in students.values() if query in s.student_id.lower() or query in s.full_name.lower()]
            
            if not found:
                print("No matching student found.")
            else:
                print(f"\nFound {len(found)} result(s):")
                for s in found:
                    print(f"ID: {s.student_id} | Name: {s.full_name} | Class: {s.class_name} | DOB: {s.dob}")
                    print(f"Scores: {s.scores if s.scores else 'No scores recorded yet'}")
                    print("-" * 40)

        elif choice == "4":
            print("\n--- Update Student Information ---")
            s_id = input("Enter Student ID to update: ").strip()
            if s_id not in students:
                print("Error: Student ID not found.")
                continue
            
            s = students[s_id]
            print(f"Updating details for {s.full_name}. Press Enter to keep existing value.")
            
            new_name = input(f"New Full Name [{s.full_name}]: ").strip()
            if new_name: s.full_name = new_name
            
            new_class = input(f"New Class [{s.class_name}]: ").strip()
            if new_class: s.class_name = new_class
            
            new_gender = input(f"New Gender [{s.gender}]: ").strip()
            if new_gender: s.gender = new_gender
            
            new_dob = input(f"New Date of Birth [{s.dob}]: ").strip()
            if new_dob: s.dob = new_dob
            
            save_data(students)
            print("✔ Student information updated successfully!")

        elif choice == "5":
            print("\n--- Delete Student Record ---")
            s_id = input("Enter Student ID to delete: ").strip()
            if s_id not in students:
                print("Error: Student ID not found.")
                continue
            
            confirm = input(f"Are you sure you want to delete {students[s_id].full_name}? (y/n): ").strip().lower()
            if confirm == 'y':
                del students[s_id]
                save_data(students)
                print("✔ Student record deleted successfully.")
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            print("\n--- Record/Update Scores for Subjects ---")
            s_id = input("Enter Student ID: ").strip()
            if s_id not in students:
                print("Error: Student ID not found.")
                continue
            
            s = students[s_id]
            print(f"Recording scores for {s.full_name}.")
            
            subjects = ["Mathematics", "English Language", "Basic Science", "Social Studies", "Computer Science"]
            custom = input("Use standard 5 subjects (Math, English, Science, Social Studies, Computer)? (y/n): ").strip().lower()
            if custom != 'y':
                subjects = []
                print("Enter 5 subject names:")
                for i in range(5):
                    sub = input(f"Subject {i+1} name: ").strip()
                    while not sub:
                        sub = input(f"Subject name cannot be empty. Subject {i+1} name: ").strip()
                    subjects.append(sub)
            
            temp_scores = {}
            for sub in subjects:
                while True:
                    val = input(f"Enter score for {sub} (0-100): ").strip()
                    score = validate_score(val)
                    if score is not None:
                        temp_scores[sub] = score
                        break
            
            s.scores = temp_scores
            save_data(students)
            print("✔ Scores recorded and saved successfully!")

        elif choice == "7":
            print("\n--- Individual Student Report Card ---")
            s_id = input("Enter Student ID: ").strip()
            if s_id not in students:
                print("Error: Student ID not found.")
                continue
            
            s = students[s_id]
            print("\n" + "=" * 50)
            print(f"            ACADEMIC REPORT CARD")
            print("=" * 50)
            print(f"Student ID   : {s.student_id}")
            print(f"Full Name    : {s.full_name}")
            print(f"Class/Form   : {s.class_name}")
            print(f"Gender       : {s.gender}")
            print(f"Date of Birth: {s.dob}")
            print(f"Record Date  : {s.date_added}")
            print("-" * 50)
            if not s.scores:
                print("No scores recorded yet.")
            else:
                print(f"{'Subject':<22} | {'Score':<6}")
                print("-" * 31)
                for sub, score in s.scores.items():
                    print(f"{sub:<22} | {score:<6.1f}")
                print("-" * 31)
                print(f"Total Score  : {s.calculate_total():.1f}")
                print(f"Average Score: {s.calculate_average():.2f}%")
                print(f"Final Grade  : {s.get_grade()}")
            print("=" * 50)

        elif choice == "8":
            print("\n--- Class Statistics & Sorted Rankings ---")
            if not students:
                print("No student records available.")
                continue
            
            stats = calculate_class_stats(students)
            print("\n--- Class Statistics ---")
            print(f"Total Students : {len(students)}")
            if stats:
                print(f"Highest Average: {stats['highest']:.2f}%")
                print(f"Lowest Average : {stats['lowest']:.2f}%")
                print(f"Class Average  : {stats['class_average']:.2f}%")
            
            sort_choice = input("\nSort by (1) Average Score (Highest to Lowest) or (2) Student Name? Enter 1 or 2: ").strip()
            if sort_choice == "2":
                sorted_list = sort_students(students, by="name", reverse=False)
                print("\n--- Students Sorted by Name ---")
            else:
                sorted_list = sort_students(students, by="average", reverse=True)
                print("\n--- Students Sorted by Average Score ---")
                
            print(f"{'ID':<10} | {'Full Name':<20} | {'Class':<10} | {'Total':<8} | {'Average':<8} | {'Grade':<5}")
            print("-" * 68)
            for s in sorted_list:
                print(f"{s.student_id:<10} | {s.full_name:<20} | {s.class_name:<10} | {s.calculate_total():<8.1f} | {s.calculate_average():<8.1f} | {s.get_grade():<5}")

        elif choice == "9":
            print("\n--- Generate & Save Text Report ---")
            if not students:
                print("No student records available to report.")
                continue
            filename = input("Enter output filename [class_performance_report.txt]: ").strip()
            if not filename:
                filename = "class_performance_report.txt"
            
            report_text = generate_text_report(students, filename)
            print("\nPreview of Generated Report:")
            print(report_text[:400] + "\n... [Full text saved to file] ...")

        elif choice == "10":
            print("\nSaving data and exiting... Goodbye!")
            save_data(students)
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

if __name__ == "__main__":
    main()