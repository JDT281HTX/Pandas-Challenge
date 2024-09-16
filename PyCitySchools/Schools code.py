# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("C:/Users/DonJa/Documents/Module 4 Challenge/PyCitySchools/Resources/schools_complete.csv")
student_data_to_load = Path("C:/Users/DonJa/Documents/Module 4 Challenge/PyCitySchools/Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on="school_name")
print(school_data_complete.head()) 

# Calculate the total number of unique schools
school_count = school_data_complete['school_name'].nunique()
print(f"School Count: {school_count}")

# Calculate the total number of students
student_count = school_data_complete['Student ID'].nunique()
print(f"Student Count: {student_count}") 

# Calculate the total budget
total_budget = school_data['budget'].sum()
print(f"Total Budget: {total_budget}") 

# Calculate the average (mean) math score
average_math_score = school_data_complete['math_score'].mean()
print(f"Average Math Score: {average_math_score}") 

# Calculate the average (mean) reading score
average_reading_score = school_data_complete['math_score'].mean()
print(f"Average Reading Score: {average_reading_score}") 

# Use the following to calculate the percentage of students who passed math (math scores greather than or equal to 70)
passing_math_count = school_data_complete[(school_data_complete["math_score"] >= 70)].count()["student_name"]
passing_math_percentage = passing_math_count / float(student_count) * 100
print(f"Passing Math Percentage: {passing_math_percentage}") 

# Calculate the percentage of students who passed reading (hint: look at how the math percentage was calculated)
passing_reading_count = school_data_complete[(school_data_complete["reading_score"] >= 70)].count()["student_name"]
passing_reading_percentage = passing_reading_count / float(student_count) * 100
print(f"Passing Reading Percentage: {passing_reading_percentage}")

# Use the following to calculate the percentage of students that passed math and reading
passing_math_reading_count = school_data_complete[
    (school_data_complete["math_score"] >= 70) & (school_data_complete["reading_score"] >= 70)
].count()["student_name"]
overall_passing_rate = passing_math_reading_count /  float(student_count) * 100
print(f"Overall Passing Rate: {overall_passing_rate}") 

# Create a high-level snapshot of the district's key metrics in a DataFrame
district_summary = pd.DataFrame({
    "Total Schools": [school_count],
    "Total Students": [student_count],
    "Total Budget": [total_budget],
    "Average Math Score": [average_math_score],
    "Average Reading Score": [average_reading_score]
}) 

# Formatting
district_summary["Total Students"] = district_summary["Total Students"].map("{:,}".format)
district_summary["Total Budget"] = district_summary["Total Budget"].map("${:,.2f}".format) 

# Display the DataFrame 
print(district_summary) 

# Use the code provided to select the type per school from school_data
school_types = school_data.set_index(["school_name"])["type"] 

# Calculate the total student count per school from school_data
per_school_counts = per_school_counts = school_data_complete.groupby(["school_name"])["Student ID"].count() 

# Calculate the total school budget and per capita spending per school from school_data
per_school_budget = per_school_budget = school_data.groupby(["school_name"])["budget"].sum()
per_school_capita = per_school_capita = per_school_budget / per_school_counts 

# Calculate the average test scores per school from school_data_complete
per_school_math = per_school_math = school_data_complete.groupby(["school_name"])["math_score"].mean()
per_school_reading = per_school_reading = school_data_complete.groupby(["school_name"])["reading_score"].mean() 

# Calculate the number of students per school with math scores of 70 or higher from school_data_complete
students_passing_math = students_passing_math = school_data_complete[school_data_complete["math_score"] >= 70]
school_students_passing_math = school_students_passing_math = students_passing_math.groupby(["school_name"])["Student ID"].count() 

# Calculate the number of students per school with reading scores of 70 or higher from school_data_complete
students_passing_reading = students_passing_reading = school_data_complete[school_data_complete["reading_score"] >= 70]
school_students_passing_reading = school_students_passing_reading = students_passing_reading.groupby(["school_name"])["Student ID"].count() 

# Use the provided code to calculate the number of students per school that passed both math and reading with scores of 70 or higher
students_passing_math_and_reading = school_data_complete[
    (school_data_complete["reading_score"] >= 70) & (school_data_complete["math_score"] >= 70)
]
school_students_passing_math_and_reading = students_passing_math_and_reading.groupby(["school_name"]).size() 

# Use the provided code to calculate the passing rates
per_school_passing_math = school_students_passing_math / per_school_counts * 100
per_school_passing_reading = school_students_passing_reading / per_school_counts * 100
overall_passing_rate = school_students_passing_math_and_reading / per_school_counts * 100 

# Create a DataFrame called `per_school_summary` with columns for the calculations above.
per_school_summary = pd.DataFrame({
    "School Type": school_types,  # This was created earlier
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": overall_passing_rate
})

# Formatting
per_school_summary["Total School Budget"] = per_school_summary["Total School Budget"].map("${:,.2f}".format)
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].map("${:,.2f}".format)

# Display the DataFrame
pd.set_option('display.max_columns', None) 
pd.set_option('display.width', None)
print (per_school_summary) 

# Sort the schools by `% Overall Passing` in descending order and display the top 5 rows.
top_schools =top_schools = per_school_summary.sort_values(by="% Overall Passing", ascending=False)
print(top_schools.head(5)) 

# Sort the schools by `% Overall Passing` in ascending order and display the top 5 rows.
bottom_schools = bottom_schools = per_school_summary.sort_values(by="% Overall Passing", ascending=True)
print(bottom_schools.head(5)) 

# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")] 

# Group by `school_name` and take the mean of the `math_score` column for each.
ninth_grade_math_scores = ninth_graders.groupby("school_name")["math_score"].mean()
tenth_grader_math_scores = tenth_graders.groupby("school_name")["math_score"].mean() 
eleventh_grader_math_scores = eleventh_graders.groupby("school_name")["math_score"].mean() 
twelfth_grader_math_scores = twelfth_graders.groupby("school_name")["math_score"].mean()

# Combine each of the scores above into single DataFrame called `math_scores_by_grade`
math_scores_by_grade = math_scores_by_grade = pd.DataFrame({
    "9th Grade": ninth_grade_math_scores,
    "10th Grade": tenth_grader_math_scores,
    "11th Grade": eleventh_grader_math_scores,
    "12th Grade": twelfth_grader_math_scores
})

# Minor data wrangling
math_scores_by_grade.index.name = None

# Display the DataFrame
print(math_scores_by_grade) 

# Use the code provided to separate the data by grade
ninth_graders = school_data_complete[(school_data_complete["grade"] == "9th")]
tenth_graders = school_data_complete[(school_data_complete["grade"] == "10th")]
eleventh_graders = school_data_complete[(school_data_complete["grade"] == "11th")]
twelfth_graders = school_data_complete[(school_data_complete["grade"] == "12th")]

# Group by `school_name` and take the mean of the the `reading_score` column for each.
ninth_grade_reading_scores = ninth_graders.groupby("school_name")["reading_score"].mean()
tenth_grader_reading_scores = tenth_graders.groupby("school_name")["reading_score"].mean() 
eleventh_grader_reading_scores = eleventh_graders.groupby("school_name")["reading_score"].mean() 
twelfth_grader_reading_scores = twelfth_graders.groupby("school_name")["reading_score"].mean() 

# Combine each of the scores above into single DataFrame called `reading_scores_by_grade`
reading_scores_by_grade = math_scores_by_grade = pd.DataFrame({
    "9th Grade": ninth_grade_reading_scores,
    "10th Grade": tenth_grader_reading_scores,
    "11th Grade": eleventh_grader_reading_scores,
    "12th Grade": twelfth_grader_reading_scores
}) 

# Minor data wrangling
reading_scores_by_grade.index.name = None 

# Display the DataFrame
print(reading_scores_by_grade) 

# Establish the bins
spending_bins = [0, 585, 630, 645, 680]
labels = ["<$585", "$585-630", "$630-645", "$645-680"] 

# Create a copy of the school summary for later aggregations
school_spending_df = per_school_summary.copy() 
per_school_summary["Per Student Budget"] = per_school_summary["Per Student Budget"].replace('[\$,]', '', regex=True).astype(float)

# Use `pd.cut` on the per_school_capita Series from earlier to categorize per student spending based on the bins.
school_spending_df["Spending Ranges (Per Student)"] = pd.cut(per_school_summary["Per Student Budget"], 
                                                             bins=spending_bins, 
                                                             labels=labels)

# Convert Spending Ranges (Per Student) to a string
school_spending_df["Spending Ranges (Per Student)"] = school_spending_df["Spending Ranges (Per Student)"].astype(str)
print(school_spending_df) 

#  Calculate averages for the desired columns.
spending_math_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Math Score"].mean()
spending_reading_scores = school_spending_df.groupby(["Spending Ranges (Per Student)"])["Average Reading Score"].mean()
spending_passing_math = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Math"].mean()
spending_passing_reading = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Passing Reading"].mean()
overall_passing_spending = school_spending_df.groupby(["Spending Ranges (Per Student)"])["% Overall Passing"].mean() 

# Assemble into DataFrame
spending_summary = pd.DataFrame({
    "Average Math Score": spending_math_scores,
    "Average Reading Score": spending_reading_scores,
    "% Passing Math": spending_passing_math,
    "% Passing Reading": spending_passing_reading,
    "% Overall Passing": overall_passing_spending
})

# Display results
print(spending_summary) 

# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
labels = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"] 

# Create a copy of the school summary for later aggregations
school_size_df = per_school_summary.copy() 

# Use `pd.cut` on the per_school_counts Series from earlier to categorize school size based on the bins.
school_size_df["School Size"] = pd.cut(per_school_counts, bins=size_bins, labels=labels)

# Convert School Size to a string
school_size_df["School Size"] = school_size_df["School Size"].astype(str)
print(school_size_df) 

# Calculate averages for the desired columns.
size_math_scores = school_size_df.groupby(["School Size"])["Average Math Score"].mean()
size_reading_scores = school_size_df.groupby(["School Size"])["Average Reading Score"].mean()
size_passing_math = school_size_df.groupby(["School Size"])["% Passing Math"].mean()
size_passing_reading = school_size_df.groupby(["School Size"])["% Passing Reading"].mean()
size_overall_passing = school_size_df.groupby(["School Size"])["% Overall Passing"].mean() 

# Create a DataFrame called `size_summary` that breaks down school performance based on school size (small, medium, or large).
# Use the scores above to create a new DataFrame called `size_summary`
size_summary = size_summary = pd.DataFrame({
    "Average Math Score": size_math_scores,
    "Average Reading Score": size_reading_scores,
    "% Passing Math": size_passing_math,
    "% Passing Reading": size_passing_reading,
    "% Overall Passing": size_overall_passing
})

# Display results
print(size_summary) 

# Group the per_school_summary DataFrame by "School Type" and average the results.
average_math_score_by_type = per_school_summary.groupby(["School Type"])["Average Math Score"].mean()
average_reading_score_by_type = per_school_summary.groupby(["School Type"])["Average Reading Score"].mean()
average_percent_passing_math_by_type = per_school_summary.groupby(["School Type"])["% Passing Math"].mean()
average_percent_passing_reading_by_type = per_school_summary.groupby(["School Type"])["% Passing Reading"].mean()
average_percent_overall_passing_by_type = per_school_summary.groupby(["School Type"])["% Overall Passing"].mean() 

# Assemble the new data by type into a DataFrame called `type_summary`
type_summary = pd.DataFrame({
    "Average Math Score": average_math_score_by_type,
    "Average Reading Score": average_reading_score_by_type,
    "% Passing Math": average_percent_passing_math_by_type,
    "% Passing Reading": average_percent_passing_reading_by_type,
    "% Overall Passing": average_percent_overall_passing_by_type
})

# Display results
print(type_summary)