import json
from datetime import datetime, timedelta

# Function to calculate the total hours and minutes for each day
def calculate_day_totals(data):
    for day in data["Days"]:
        total_time = timedelta()
        for interval in day["Intervals"]:
            start_time = datetime.strptime(interval["Start"], "%H:%M")
            end_time = datetime.strptime(interval["End"], "%H:%M")
            total_time += end_time - start_time
        
        day["Total"] = {
            "Hours": total_time.days * 24 + total_time.seconds // 3600,
            "Minutes": (total_time.seconds // 60) % 60,
        }

# Function to calculate the total hours and minutes for the month
def calculate_month_total(data):
    total_time = timedelta()
    for day in data["Days"]:
        total_time += timedelta(
            hours=day["Total"]["Hours"], minutes=day["Total"]["Minutes"]
        )
    
    data["Total"] = {
        "Hours": total_time.days * 24 + total_time.seconds // 3600,
        "Minutes": (total_time.seconds // 60) % 60,
    }

# Load the JSON data from the file
with open('./../data/storage001/folder004/file001.json', 'r') as file:
    journal_data = json.load(file)

# Calculate totals
calculate_day_totals(journal_data[0])
calculate_month_total(journal_data[0])

# Write the updated JSON data back to the file
with open('./../data/storage001/folder004/file001.json', 'w') as file:
    json.dump(journal_data, file, indent=4)

# Output the result to verify the correctness
#print(json.dumps(journal_data, indent=4))
