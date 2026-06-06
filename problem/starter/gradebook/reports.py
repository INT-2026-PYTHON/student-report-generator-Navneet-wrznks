"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable grade report.
    """
from .stats import average_per_student
from .stats import subjects_offered
from .stats import top_scorer
from .stats import passing_students


def format_report(records):
    avg = average_per_student(records)
    subjects = sorted(subjects_offered(records))
    topper = top_scorer(records)
    passed = passing_students(records)

    report = "=== Gradebook Report ===\n"
    report += f"Total records: {len(records)}\n"
    report += "Subjects offered: " + ", ".join(subjects) + "\n\n"

    report += "Averages:\n"

    for name in sorted(avg):
        report += f"{name} : {avg[name]}\n"

    report += "\n"
    report += f"Top scorer: {topper[0]} ({topper[1]})\n"
    report += "Passing students (>= 60.0): "
    report += ", ".join(passed)

    return report
