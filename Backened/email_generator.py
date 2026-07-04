def generate_email(email_type):
 
    email_type = email_type.lower()
 
    if "assignment" in email_type:
 
        return """
Subject: Assignment Submission Reminder
 
Dear Student,
 
This is a friendly reminder to submit your assignment before the deadline.
 
Regards,
Operations Team
"""
 
    elif "exam" in email_type:
 
        return """
Subject: Exam Reminder
 
Dear Student,
 
Your examination is scheduled as per the academic timetable.
Please arrive 30 minutes before the exam.
 
Regards,
Operations Team
"""
 
    elif "fee" in email_type:
 
        return """
Subject: Fee Payment Reminder
 
Dear Student,
 
Your fee payment is pending.
Please complete the payment before the due date.
 
Regards,
Operations Team
"""
 
    elif "attendance" in email_type:
 
        return """
Subject: Attendance Warning
 
Dear Student,
 
Your attendance is below the required percentage.
Please attend the upcoming classes regularly.
 
Regards,
Operations Team
"""
 
    else:
 
        return "Email type not found."