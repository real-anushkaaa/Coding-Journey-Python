# --------------------------------------------------
# Create function that returns student grade.
# --------------------------------------------------

def grade(marks):

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    else:
        return "C"

print(grade(85))