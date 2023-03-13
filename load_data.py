# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = ""

# Update "" with your team (e.g. T102)
__team__ = ""

#==========================================#
# Place your student_school_list function after this line


#==========================================#
# Place your student_health_list function after this line


#==========================================#
# Place your student_age_list function after this line
def student_age_list (filename: str, age: int) -> dict:
   students=[]
   with open(filename, 'r') as file:
      lines = file.readlines()
      # Extract the keys from the first row
      keys = lines[0].strip().split(',')
      # Create a list of dictionaries with each dictionary corresponding to a row in the CSV file
      result = []
      for line in lines[1:]:
         values = line.strip().split(',')
         # Convert values to the appropriate data type (e.g., int, float)
         values = [int(value) if value.isdigit() else float(value) if '.' in value else value for value in values]
         # Combine the keys and values into a dictionary
         row_dict = dict(zip(keys, values))
         result.append(row_dict)
      for row in result:
         if int(row['Age']) == age:     #if statement checking to see if the integer after the key word in equal to the imputed age value
            student = {key: value for key, value in row.items() if key != 'age'}   # finds the key and values pairs in that row except for the 'Age
            students.append(student) # adds the student to the empty list
#==========================================#
# Place your student_failures_list function after this line


#==========================================#
# Place your load_data function after this line


#==========================================#
# Place your add_average function after this line


# Do NOT include a main script in your submission
