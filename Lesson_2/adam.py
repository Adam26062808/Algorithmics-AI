questions = [
    "1. What is the average alcohol consumption for smokers and non-smokers?",
    "2. How does sleeping hours correlate with BMI?",
    "3: Total sleep hours for each smoking status group",
    "4. What is the average sleep hours among individuals with health_score over 75?",
]
import polars

file_path = "Data/synthetic_health_data.csv"
df = polars.read_csv(file_path)


# avg_health_score_by_smokers = (df.group_by("Smoking_Status")
# .agg(polars.col("Alcohol_Consumption").mean().alias("avg_Alcohol_Consumption"))
# )
# print("\n Question 1:What is the average alcohol consumption for smokers and non-smokers?")
# print(avg_health_score_by_smokers)


# correlation = df.select(
#     polars.corr("BMI","Sleep_Hours").alias("correlation")
# )
# print("\n Question 2: Correlation between BMI and Sleeping Hours:")
# print(correlation)

# Total_sleep_hours = (df.group_by("Smoking_Status")
# .agg(polars.col("Sleep_Hours").sum().alias("Total_Sleep_Hours"))
# )
# print("\n Question 1:What is the total sleep hours?")
# print(Total_sleep_hours)

avg_sleep_health_score_75 = (
    df.filter(polars.col("Health_Score") >= 75)
    .select(polars.col("Sleep_Hours").mean().alias("Average_Sleep_Hours"))
)
print(avg_sleep_health_score_75)