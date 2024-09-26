import json
from datetime import datetime, timedelta

# Function to calculate the total hours and minutes for each day
def calculate_day_totals(data):
    for day in data["Days"]:
        total_time = timedelta()
        for interval in day["Intervals"]:
            start_time = datetime.strptime(interval["Start"], "%H:%M")
            end_time = datetime.strptime(interval["End"], "%H:%M")
            
            # Check if end time is before start time, assuming it's the next day
            if end_time < start_time:
                end_time += timedelta(days=1)  # Add a day to end time
            
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

# Loop through all the months in the journal data and calculate totals
for month_data in journal_data:
    calculate_day_totals(month_data)
    calculate_month_total(month_data)

# Write the updated JSON data back to the file
with open('./../data/storage001/folder004/file001.json', 'w') as file:
    json.dump(journal_data, file, indent=2)

# Output the result to verify the correctness
print(json.dumps(journal_data, indent=2))
