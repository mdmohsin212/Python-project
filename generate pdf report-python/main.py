import csv
from fpdf import FPDF

th = open("student.csv", "w+", newline="")
w = csv.writer(th)

header = ["Student_Id", "Name", "Roll", "Semester", "Shift", "Department", "Date of birth", "Phone_no."]
w.writerow(header)

data = []

while True:
    try:
        n = int(input("How many student records do you want to insert? "))
    except ValueError:
        continue
    else:
        break

for i in range(n):
    print("Enter Student record", i+1, "")
    student_id = input("Student ID: ")
    name = input("Name: ")
    while True:
        try:
            roll = int(input("Roll: "))
        except ValueError:
            print("Invalid Roll, Please Enter Again")
            continue
        else:
            break
    semester = input("Semester: ")
    shift = input("Shift: ")
    dept = input("Department: ")
    dob = input("Date of birth (dd/mm/yyyy): ")
    phone_no = input("Phone No: ")
    rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
    data.append(rec)
    w.writerows(data)

th.close()

print("If you want to see the PDF report, please open student.pdf file from your current directory location")
print("Student Records from stored CSV file:")

fh = open("student.csv", "r")
r = csv.reader(fh)

pdf = FPDF()
pdf.add_page()

page_width = pdf.w - 2 * pdf.l_margin
pdf.set_font('Times', 'B', 12.0)
pdf.cell(page_width, 0.0, 'Students Data Report', align='C')
pdf.ln(10)

pdf.set_font('Courier', '', 12)
col_width = page_width / 6

th = pdf.font_size

for row in r:
    pdf.cell(col_width, th, str(row[0]), border=1)
    pdf.cell(col_width, th, row[1], border=1)
    pdf.cell(col_width, th, row[2], border=1)
    pdf.cell(col_width, th, row[3], border=1)
    pdf.cell(col_width, th, row[4], border=1)
    pdf.cell(col_width, th, row[5], border=1)
    pdf.cell(col_width, th, row[6], border=1)
    pdf.cell(col_width, th, row[7], border=1)
    pdf.ln(th)

pdf.ln(10)
pdf.set_font('Times', '', 10.0)
pdf.cell(page_width, 0.0, '- end of report -', align='C')

pdf.output('student.pdf', 'F')
fh.close()
