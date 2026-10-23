# Smart Attendance System

A Python attendance tracker built while teaching computer skills at a local institute, extended with a catch-up content tracker.

## Background

I built this after running into problems with paper-based attendance records at the institute — records would go missing or get disorganized. Once the basic tracker was working, I kept running into the same follow-up problem: whenever a student missed several sessions, I had to manually remember and work out exactly what they'd missed before I could catch them up. This feature grew out of that real, recurring task.

## Features

- Add students, mark present or absent by date
- Each session can be tagged with the topic that was taught that day
- Catch-up list — for any student, automatically generates the exact list of topics they missed, by matching their absence dates against recorded session topics
- Class-wide view showing every student's missed topics at once
- Cancelled class dates are recorded and protected (no attendance marked on those days)

## How It Works

The catch-up list is simple rule-based matching — checking each absence date against the topic recorded for that session — not a trained model.

A more advanced version of this idea, which I'd like to build as I learn more, would go further: using a student's quiz or assignment scores on each topic to recommend which missed topics to prioritize reviewing first, similar to how a recommendation system suggests content based on someone's history. That would need per-topic performance data and recommender-system techniques I haven't learned yet. This version handles the simpler, rule-based half of the idea — knowing exactly what was missed — which was the first and most immediate problem I actually had to solve.

## How To Run

python attendance_system.py

## Notes

This project is a direct outcome of my time teaching at the institute, not a hypothetical exercise — the catch-up problem it solves is one I ran into personally and repeatedly.
