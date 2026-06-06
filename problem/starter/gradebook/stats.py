"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    results = {}
    for record in records:
        name = record["name"]
        score = record["score"]

        if name not in results:
            results[name] = {"total": 0, "count": 0}

        results[name]["total"] += score
        results[name]["count"] += 1
    averages = {}
    for name, data in results.items():
        averages[name] = data["total"] / data["count"]
    return averages

def subjects_offered(records: list[dict]) -> set[str]:
    subjects = set()
    for record in records:
        subjects.add(record["subject"])
    return subjects


def top_scorer(records: list[dict]) -> tuple[str, float]:
    avearges = average_per_student(records)
    highest_name = None
    highest_avg = -1
    for name, avg in avearges.items():
        if avg > highest_avg:
            highest_name = name
            highest_avg = avg
    return highest_name, highest_avg


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    averages = average_per_student(records)

    names = []

    for name, avg in averages.items():
        if avg >= threshold:
            names.append(name)
    return sorted(names)
