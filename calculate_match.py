from datetime import datetime, timedelta

def find_free_time(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Convert input times to datetime objects
    calendar1 = [[datetime.strptime(start, '%H:%M'), datetime.strptime(end, '%H:%M')] for start, end in calendar1]
    calendar2 = [[datetime.strptime(start, '%H:%M'), datetime.strptime(end, '%H:%M')] for start, end in calendar2]
    dailyBounds1 = [datetime.strptime(time, '%H:%M') for time in dailyBounds1]
    dailyBounds2 = [datetime.strptime(time, '%H:%M') for time in dailyBounds2]
    meetingDuration = timedelta(minutes=meetingDuration)

    # Find the earliest and latest possible start times for the meeting
    earliest_start = max(dailyBounds1[0], dailyBounds2[0])
    latest_start = min(dailyBounds1[1], dailyBounds2[1])

    # Initialize the current time to the earliest possible start time
    current_time = earliest_start

    # Initialize the list of free time slots
    free_times = []

    # Iterate until the current time is past the latest possible start time
    while current_time <= latest_start:
        # Check if the current time is within a busy time slot on either calendar
        if not any(start <= current_time < end for start, end in calendar1 + calendar2):
            # Initialize the end time of the free time slot
            end_time = current_time + meetingDuration

            # Check if the end time is within the daily bounds
            if earliest_start <= end_time <= latest_start:
                free_times.append([current_time.strftime("%H:%M"), end_time.strftime("%H:%M")])
            current_time = end_time
        else:
            # If the current time is within a busy time slot, move to the end of that slot
            current_time = min(end for start, end in calendar1 + calendar2 if start <= current_time < end)

    return free_times


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailyBounds1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

print("Calendar Matching:",find_free_time(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration))


def find_optimal_block(blocks, requirements):
    optimal_index = 0
    min_max_distance = float('inf')
    for i in range(len(blocks)):
        max_distance = 0
        for req in requirements:
            distance = min([abs(j-i) for j in range(len(blocks)) if blocks[j][req] == True])
            max_distance = max(distance, max_distance)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            optimal_index = i
    return optimal_index

requirements = ['gym', 'school', 'store']

blocks = [
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": True,
    "school": False,
    "store": False,
  },
  {
    "gym": True,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": False,
  },
  {
    "gym": False,
    "school": True,
    "store": True,
  },
]
print("Apartment Hunting:",find_optimal_block(blocks,requirements))