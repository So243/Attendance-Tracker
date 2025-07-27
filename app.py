def mark_attendance():
    # Create an empty dictionary to store attendance status
    attendance = {}

    print("Welcome to the Attendance Tracker!")

    while True:
        attendee_name = input(
            "Enter the name of attendee (or 'exit' to finish): ")
        if attendee_name.lower() == 'exit':
            break
        attendance[attendee_name] = True  # Mark as present

    # Display attendance status
    print("\nAttendance Status:")
    for attendee, present in attendance.items():
        status = "Present" if present else "Absent"
        print(f"{attendee}: {status}")


if __name__ == "__main__":
    mark_attendance()
