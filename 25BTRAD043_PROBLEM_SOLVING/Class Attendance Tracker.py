def add_student(attendance_db, student_name):
    """Adds a new student with an empty attendance list."""
    if student_name not in attendance_db:
        attendance_db[student_name] = []
        print(f"Student '{student_name}' added.")
    else:
        print(f"Student '{student_name}' already exists.")


def mark_attendance(attendance_db, student_name, status):
    """Appends a new attendance record ('P' or 'A') for a student."""
    status = status.upper()
    if status not in ("P", "A"):
        print("Invalid status. Use 'P' for Present or 'A' for Absent.")
        return

    if student_name in attendance_db:
        attendance_db[student_name].append(status)
    else:
        print(f"Student '{student_name}' not found. Adding student first...")
        attendance_db[student_name] = [status]


def update_attendance(attendance_db, student_name, day_index, new_status):
    """Updates an existing attendance record by day index (0-based)."""
    new_status = new_status.upper()
    if student_name in attendance_db and 0 <= day_index < len(
        attendance_db[student_name]
    ):
        if new_status in ("P", "A"):
            attendance_db[student_name][day_index] = new_status
            print(
                f"Updated {student_name}'s Day {day_index + 1} attendance to"
                f" '{new_status}'."
            )
        else:
            print("Invalid status. Use 'P' or 'A'.")
    else:
        print("Invalid student name or day index.")


def calculate_percentage(records):
    """Calculates attendance percentage from a list of records."""
    if not records:
        return 0.0
    present_days = records.count("P")
    return (present_days / len(records)) * 100


def display_report(attendance_db, threshold=75.0):
    """Displays formatted attendance details and flags low attendance."""
    print("\n" + "=" * 65)
    print(
        f"{'Student Name':<15} | {'Records':<20} | {'Attendance %':<13} |"
        f" {'Status'}"
    )
    print("-" * 65)

    low_attendance_students = []

    for student, records in attendance_db.items():
        pct = calculate_percentage(records)
        status_flag = "OK" if pct >= threshold else "LOW (<75%)"
        if pct < threshold:
            low_attendance_students.append((student, pct))

        records_str = ", ".join(records) if records else "No records"
        print(
            f"{student:<15} | {records_str:<20} | {pct:>11.2f}% | {status_flag}"
        )

    print("=" * 65)

    if low_attendance_students:
        print(f"\nAlert: Students below {threshold}% attendance threshold:")
        for student, pct in low_attendance_students:
            print(f" - {student}: {pct:.2f}%")
    else:
        print(f"\nAll students meet the {threshold}% attendance threshold.")


# --- Testing Scenarios ---
if __name__ == "__main__":
    # Initial dataset: Dictionary with student names as keys and lists of statuses as values
    class_attendance = {
        "Aarav": ["P", "P", "A", "P", "P"],
        "Diya": ["P", "P", "P", "P", "P"],
        "Rohan": ["A", "A", "P", "A", "P"],
        "Meera": ["P", "A", "P", "P", "A"],
    }

    print("--- SCENARIO 1: Initial Class Attendance Report ---")
    display_report(class_attendance, threshold=75.0)

    print("\n--- SCENARIO 2: Adding a New Student & Marking New Day ---")
    add_student(class_attendance, "Kabir")
    # Marking Day 6 for everyone
    daily_updates = {
        "Aarav": "P",
        "Diya": "A",
        "Rohan": "P",
        "Meera": "P",
        "Kabir": "P",
    }
    for name, status in daily_updates.items():
        mark_attendance(class_attendance, name, status)

    display_report(class_attendance, threshold=75.0)

    print("\n--- SCENARIO 3: Updating an Incorrect Record ---")
    # Correcting Rohan's Day 2 (index 1) from 'A' to 'P'
    update_attendance(class_attendance, "Rohan", 1, "P")
    display_report(class_attendance, threshold=75.0)