import polars

file_path = "Data/student_exam_scores.csv"
df = polars.read_csv(file_path)

# Student with maximum exam_score
maximum_exam_score = df.select(polars.col("exam_score").max()).item()
maximum_exam_score_df = df.filter(polars.col("exam_score") == maximum_exam_score)
print("Student with maximum exam score: ", maximum_exam_score_df)

# Top 7 students with lowest sleep_hours select student_id, sleep_hour, exam_score, attendance_percent
top_7_scores = df.sort("sleep_hours", descending=False).head(7)
print("\nTop 5 students with lowest sleep hours:")
print(top_7_scores.select(["student_id", "exam_score", "attendance_percent","sleep_hours"]))

# Top 5 students with highest attendance_percent

top_5_scores = df.sort("attendance_percent", descending=True).head(5)
print("\nTop 5 students with highest attendance_percent:")
print(top_5_scores.select(["student_id", "exam_score", "attendance_percent",]))
