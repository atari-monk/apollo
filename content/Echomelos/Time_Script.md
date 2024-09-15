# Time script

## 10:41 - 13:45, 14:01 - 14:53 calculate hrs and min pls. (draft)

```python
from datetime import datetime

# Define the start and end times for each period
time_periods = [
    ("10:41", "13:45"),
    ("14:01", "14:53")
]

# Calculate the total time in hours and minutes
total_minutes = 0
for start, end in time_periods:
    start_time = datetime.strptime(start, "%H:%M")
    end_time = datetime.strptime(end, "%H:%M")
    delta = end_time - start_time
    total_minutes += delta.total_seconds() / 60

# Convert total minutes to hours and minutes
hours, minutes = divmod(total_minutes, 60)
hours, minutes
```

Wynik
(3.0, 56.0)
The total time is 3 hours and 56 minutes. ​
