###pass fail
score=float(input("write the student's exam score (out of 100):\n "))
total_classes=int(input("write the total number of classes:\n "))
attended_classes=int(input("write the number of classes attended by the student:\n "))
attendance_percentage=(attended_classes / total_classes)*100
if score>=70 and attendance_percentage >= 80:
    print("the student has passed the course.")
#elif para multiples condiciones si no es
elif score<70 and attendance_percentage<80:
    print("the student has failed both due to low exam score and low attendance.")
elif score < 70:
    print("the student has failed due to low exam score.")
else:
    print("the student has failed due to low attendance.")
print("and the attendance percentage is",attendance_percentage,"%")