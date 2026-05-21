# ----------------------------------------
# Create lambda for student grading.
# ----------------------------------------

grade = lambda marks: "A" if marks >= 90 else "B" if marks >= 75 else "C"

print(grade(85))