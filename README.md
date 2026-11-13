# Student Result Management System

A robust, modular command-line Python application designed for educational centers to manage student records, record subject scores, calculate grades, and generate performance reports with persistent JSON storage.

## Features
- **Student Management:** Add, view, search, update, and delete student records.
- **Score Management:** Record scores across 5+ subjects with built-in input validation.
- **Result Calculation:** Automatically calculates total scores, averages, and letter grades (A-F).
- **Reporting & Analysis:** View class statistics, sort students by average score or name, and export professional text reports.
- **Data Persistence:** Automatically saves and loads data using JSON (`data/students.json`).
- **Error Handling:** Robust `try/except/finally` blocks for file operations and score entry.

## Project Structure
```text
student_result_system/
├── main.py             # Entry point and interactive menu
├── student.py          # Student class and object methods
├── results.py          # Score validation utilities
├── storage.py          # JSON file handling (load/save)
├── reports.py          # Statistics, sorting, and text reports
├── data/
│   └── students.json   # Persistent JSON database
└── README.md           # Documentation