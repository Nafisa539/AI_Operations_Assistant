def generate_email(email_type):
 
    email_type = email_type.lower()
 
    if email_type == "leave":
 
        return """
Subject: Leave Request
 
Dear Faculty,
 
I am unable to attend today's classes due to personal reasons.
Kindly grant me leave for today.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "assignment":
 
        return """
Subject: Assignment Extension Request
 
Dear Faculty,
 
I request you to kindly extend the assignment submission deadline due to unavoidable circumstances.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "technical":
 
        return """
Subject: Technical Support Request
 
Dear Support Team,
 
I am unable to access the student portal due to a technical issue.
Kindly resolve the issue at the earliest.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "attendance":
 
        return """
Subject: Attendance Correction Request
 
Dear Faculty,
 
My attendance has not been updated correctly.
Kindly verify and update my attendance.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "bonafide":
 
        return """
Subject: Bonafide Certificate Request
 
Dear Administration,
 
I request you to kindly issue my bonafide certificate for academic purposes.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "fee":
 
        return """
Subject: Fee Payment Query
 
Dear Accounts Team,
 
I have a query regarding my fee payment.
Kindly provide the required details.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "library":
 
        return """
Subject: Library Access Request
 
Dear Librarian,
 
I am facing difficulty accessing the digital library.
Kindly help me resolve the issue.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "exam":
 
        return """
Subject: Examination Query
 
Dear Examination Cell,
 
I have a query regarding the upcoming examinations.
Kindly provide the required information.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "id card":
 
        return """
Subject: Student ID Card Request
 
Dear Administration,
 
I request you to issue a duplicate student ID card as I have misplaced the original one.
 
Thank you.
 
Regards,
Student
"""
 
    elif email_type == "password":
 
        return """
Subject: Password Reset Request
 
Dear IT Support,
 
I am unable to log in to the student portal.
Kindly help me reset my password.
 
Thank you.
 
Regards,
Student
"""
 
    else:
 
        return "Email type not found."