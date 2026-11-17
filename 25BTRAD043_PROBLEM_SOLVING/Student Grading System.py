def get_mark(subject):
	"""Read and validate a mark from 0 to 100."""
	while True:
		try:
			mark = float(input(f"Enter marks for {subject} (0-100): "))
			if 0 <= mark <= 100:
				return mark
			print("Marks must be between 0 and 100.")
		except ValueError:
			print("Please enter a valid number.")


def get_grade(percentage):
	if percentage >= 90:
		return "A+"
	if percentage >= 80:
		return "A"
	if percentage >= 70:
		return "B"
	if percentage >= 60:
		return "C"
	if percentage >= 50:
		return "D"
	return "F"


def main():
	print("Student Grading Automation")
	subjects = [subject.strip() for subject in input(
		"Enter subjects separated by commas: "
	).split(",") if subject.strip()]

	if not subjects:
		print("At least one subject is required.")
		return

	students = []
	try:
		count = int(input("Enter number of students: "))
		if count <= 0:
			raise ValueError
	except ValueError:
		print("Enter a positive whole number of students.")
		return

	for number in range(1, count + 1):
		name = input(f"\nEnter name of student {number}: ").strip() or f"Student {number}"
		marks = [get_mark(subject) for subject in subjects]
		total = sum(marks)
		percentage = total / len(subjects)
		students.append((name, total, percentage, get_grade(percentage)))

	print("\nGrading Report")
	print("-" * 60)
	print(f"{'Name':<25}{'Total':>10}{'Percent':>12}{'Grade':>10}")
	print("-" * 60)
	for name, total, percentage, grade in students:
		print(f"{name:<25}{total:>10.2f}{percentage:>11.2f}%{grade:>10}")
	print("-" * 60)


if __name__ == "__main__":
	main()
