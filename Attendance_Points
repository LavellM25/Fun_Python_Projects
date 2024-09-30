# Define variables
initial_points = 2
days_until_first_point_expires = 6  # One point expires in 6 days
days_since_last_point = 5  # Last point was received 5 days ago
points_expiry_days = 60  # Points last for 60 days before expiring
termination_threshold = 8  # Termination at 8 points
points_per_missed_shift = 1  # 1 point per missed shift
days_per_week = 7  # 7 days per week

# Calculate the total number of days until the next point expires
days_until_next_expiry = points_expiry_days - days_since_last_point

# Initialize current points and days passed
current_points = initial_points
days_passed = 0
weeks_missed = 0

# Simulate day-by-day, checking if a point expires
while current_points < termination_threshold:
    # Count a missed shift every 7 days and increase points
    if days_passed % days_per_week == 0 and days_passed > 0:
        current_points += points_per_missed_shift
        weeks_missed += 1

    # Check if a point expires
    if days_passed == days_until_first_point_expires or days_passed == days_until_next_expiry:
        current_points -= 1  # A point expires

    # Break the loop if termination threshold is reached
    if current_points >= termination_threshold:
        break

    # Increment days passed
    days_passed += 1

# Calculate the total number of weeks missed and the corresponding days
total_weeks_missed = days_passed // days_per_week
remaining_days = days_passed % days_per_week

(total_weeks_missed, remaining_days)
