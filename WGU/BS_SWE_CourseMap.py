import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill

# Define the course data
courses = [
    ["C182", "Introduction to IT", 3, 7, "Yes", "Yes", "Yes", "Yes", "General Education"],
    ["C955", "Introduction to Probability and Statistics", 3, 10, "Yes", "Yes", "Yes", "Yes", "Mathematics"],
    ["C173", "Scripting and Programming - Foundations", 3, 12, "Yes", "Yes", "Yes", "Yes", "Programming"],
    ["C188", "Software Engineering", 3, 15, "No", "No", "No", "No", "Core"],
    ["C195", "Software Engineering Capstone", 4, 20, "No", "No", "No", "No", "Capstone"]
]

# Create a new workbook and select the active sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "BS Software Engineering"

# Add header row
header = ["ID", "Course Name", "Units", "Strategy (Days)", "Study.com Transfers", "Straighterline", "Sophia.org", "Certificate", "Category"]
ws.append(header)

# Apply styles to the header row
header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="4F81BD", end_color="4F81BD", fill_type="solid")
header_alignment = Alignment(horizontal="center", vertical="center")

for col in range(1, len(header) + 1):
    cell = ws.cell(row=1, column=col)
    cell.font = header_font
    cell.fill = header_fill
    cell.alignment = header_alignment

# Add course data
for course in courses:
    ws.append(course)

# Adjust column widths for better readability
column_widths = [10, 40, 8, 15, 20, 20, 20, 15, 20]
for i, width in enumerate(column_widths, start=1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(i)].width = width

# Save the workbook
wb.save("BS_Software_Engineering_Course_Tracker.xlsx")

print("Spreadsheet created successfully!")
