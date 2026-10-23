"""
Smart Attendance System
------------------------
Tracks student attendance and, for each class session, the topic that
was taught. When a student has been absent, the system automatically
builds a "catch-up list" of exactly which topics they missed — based
on a real problem from teaching computer skills at an institute: when
a student missed several sessions, I had to manually figure out what
they'd missed and go over it with them separately.

This catch-up list is rule-based (matching absence dates to session
topics), not a trained model. A real AI version of this idea would go
further: using a student's quiz/assignment scores on each topic to
recommend which missed topics to prioritize reviewing first, the way
a recommendation system suggests content based on someone's history.
Building that would require per-topic performance data and recommender
system techniques I haven't learned yet — this version handles the
simpler, rule-based half of the idea: knowing exactly what was missed.
"""

from datetime import datetime

students = {
    "1001": {"name": "Aria Rostami", "gender": "Male"},
    "1002": {"name": "Parsa Mohammadi", "gender": "Male"},
    "1003": {"name": "Ava Naderi", "gender": "Female"},
    "1004": {"name": "Yasna Hosseini", "gender": "Female"},
    "1005": {"name": "Tarannom Rahimi", "gender": "Female"},
}

# Each session now has a topic, in addition to being a date.
session_topics = {
    "2026-06-30": "Introduction to Python: variables and data types",
    "2026-07-01": "Conditional statements (if/else)",
    "2026-07-03": "Loops: for and while",
    "2026-07-05": "Functions and parameters",
    "2026-07-07": "Lists and dictionaries",
    "2026-07-09": "File handling basics",
    "2026-07-11": "Introduction to Java syntax",
    "2026-07-13": "Java classes and objects",
    "2026-07-15": "Working with strings",
    "2026-07-17": "Error handling (try/except)",
    "2026-07-19": "Simple algorithms: searching and sorting",
    "2026-07-21": "Building a small console project",
    "2026-07-23": "Debugging techniques",
    "2026-07-25": "Review and practice session",
}

attendance = {
    "1001": {
        "2026-06-30": "present", "2026-07-01": "absent", "2026-07-03": "present",
        "2026-07-05": "present", "2026-07-07": "present", "2026-07-09": "present",
        "2026-07-11": "present", "2026-07-13": "present", "2026-07-15": "present",
        "2026-07-17": "present", "2026-07-19": "absent", "2026-07-21": "present",
        "2026-07-23": "present", "2026-07-25": "present",
    },
    "1002": {
        "2026-06-30": "present", "2026-07-01": "present", "2026-07-03": "present",
        "2026-07-05": "present", "2026-07-07": "absent", "2026-07-09": "present",
        "2026-07-11": "present", "2026-07-13": "absent", "2026-07-15": "present",
        "2026-07-17": "present", "2026-07-19": "present", "2026-07-21": "present",
        "2026-07-23": "absent", "2026-07-25": "present",
    },
    "1003": {
        "2026-06-30": "present", "2026-07-01": "present", "2026-07-03": "present",
        "2026-07-05": "present", "2026-07-07": "present", "2026-07-09": "present",
        "2026-07-11": "present", "2026-07-13": "present", "2026-07-15": "present",
        "2026-07-17": "present", "2026-07-19": "present", "2026-07-21": "present",
        "2026-07-23": "present", "2026-07-25": "present",
    },
    "1004": {
        "2026-06-30": "absent", "2026-07-01": "present", "2026-07-03": "present",
        "2026-07-05": "present", "2026-07-07": "present", "2026-07-09": "present",
        "2026-07-11": "present", "2026-07-13": "present", "2026-07-15": "present",
        "2026-07-17": "present", "2026-07-19": "present", "2026-07-21": "absent",
        "2026-07-23": "present", "2026-07-25": "present",
    },
    "1005": {
        "2026-06-30": "present", "2026-07-01": "present", "2026-07-03": "absent",
        "2026-07-05": "present", "2026-07-07": "present", "2026-07-09": "present",
        "2026-07-11": "present", "2026-07-13": "present", "2026-07-15": "present",
        "2026-07-17": "present", "2026-07-19": "present", "2026-07-21": "present",
        "2026-07-23": "present", "2026-07-25": "absent",
    },
}

CLASS_CANCELLED_DATES = {
    "2026-07-16": "System maintenance",
    "2026-07-24": "Computer equipment upgrade",
}


# ─────────────────────────────────────────────────────────────
# CORE ATTENDANCE OPERATIONS
# ─────────────────────────────────────────────────────────────

def add_student(student_id, name, gender):
    if student_id in students:
        print(f"Student ID '{student_id}' already exists.")
        return
    students[student_id] = {"name": name, "gender": gender}
    attendance[student_id] = {}
    print(f"Student '{name}' added with ID {student_id}.")


def mark_attendance(student_id, date, status):
    if student_id not in students:
        print(f"Student ID '{student_id}' not found.")
        return
    if date in CLASS_CANCELLED_DATES:
        print(f"Class was cancelled on {date} ({CLASS_CANCELLED_DATES[date]}). No attendance recorded.")
        return
    status = status.lower()
    if status not in ["present", "absent"]:
        print("Status must be 'present' or 'absent'.")
        return
    attendance[student_id][date] = status
    print(f"Marked {students[student_id]['name']} as {status} on {date}.")


def add_session_topic(date, topic):
    """Records what topic was taught on a given session date."""
    session_topics[date] = topic
    print(f"Recorded topic for {date}: {topic}")


def get_summary(student_id):
    records = attendance[student_id]
    total = len(records)
    present = sum(1 for s in records.values() if s == "present")
    return {"name": students[student_id]["name"], "present": present, "absent": total - present, "total": total}


def print_all_summaries():
    print(f"\n{'Student':<22}{'Present':<10}{'Absent':<10}{'Total':<10}")
    print("-" * 52)
    for sid in students:
        summary = get_summary(sid)
        print(f"{summary['name']:<22}{summary['present']:<10}{summary['absent']:<10}{summary['total']:<10}")


def print_student_detail(student_id):
    name = students[student_id]["name"]
    print(f"\nAttendance detail for {name} (ID: {student_id}):")
    for date in sorted(attendance[student_id].keys()):
        status = attendance[student_id][date]
        marker = "V" if status == "present" else "X"
        print(f"  {date}: {marker} {status}")


def list_cancelled_classes():
    print("\nCancelled class sessions:")
    for date, reason in sorted(CLASS_CANCELLED_DATES.items()):
        print(f"  {date}: {reason}")


# ─────────────────────────────────────────────────────────────
# CATCH-UP CONTENT TRACKER
# ─────────────────────────────────────────────────────────────

def get_missed_topics(student_id):
    """
    Builds the list of topics a student missed, by matching their
    absent dates against the recorded session topics. This is the
    rule-based part of the idea: straightforward matching, not a
    recommendation or priority ranking.
    """
    missed = []
    for date, status in attendance[student_id].items():
        if status == "absent" and date in session_topics:
            missed.append((date, session_topics[date]))
    missed.sort()
    return missed


def print_catchup_list(student_id):
    name = students[student_id]["name"]
    missed = get_missed_topics(student_id)

    print(f"\n=== Catch-Up List: {name} ===")
    if not missed:
        print("  No missed topics. Fully caught up.")
        return

    for date, topic in missed:
        print(f"  {date}: {topic}")
    print(f"\n  Total topics to review: {len(missed)}")


def print_all_catchup_lists():
    print("\n=== Catch-Up Lists for All Students ===")
    any_missed = False
    for sid in students:
        missed = get_missed_topics(sid)
        if missed:
            any_missed = True
            name = students[sid]["name"]
            print(f"\n  {name} ({len(missed)} topic(s) missed):")
            for date, topic in missed:
                print(f"    - {date}: {topic}")
    if not any_missed:
        print("  No students have missed topics to catch up on.")


def main():
    print("=== Smart Attendance System ===")
    print("Class schedule: Saturday to Thursday, 10:00-12:00\n")

    print("Registered students:")
    for sid, info in students.items():
        print(f"  {sid}: {info['name']} ({info['gender']})")

    print_all_summaries()
    print_all_catchup_lists()

    print_student_detail("1001")
    list_cancelled_classes()

    # demonstrate adding a new session topic
    print()
    add_session_topic("2026-07-27", "Intro to version control with Git")
    print_catchup_list("1001")


if __name__ == "__main__":
    main()
