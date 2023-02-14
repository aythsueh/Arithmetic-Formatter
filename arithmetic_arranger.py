def arithmetic_arranger(problems, answers=False):

  # define all the variables in arranged_problems
  first_line = ""
  second_line = ""
  third_line = ""
  fourth_line = ""

  location = 0

  for i in problems:
    # record the current number of loop
    location = location + 1

    # define a variable answer
    answer = 0

    # split the problem into 3 units
    units_p = i.split()

    # Rule 1: The limit of problem set is five:
    if len(problems) > 5:
      return "Error: Too many problems."

    # Rule 2: only accept addition and subtraction
    if units_p[1] != "+" and units_p[1] != "-":
      return "Error: Operator must be '+' or '-'."

    # Rule 4: a max of four digits
    if len(units_p[0]) > 4 or len(units_p[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

    # Rule 3: Each number (operand) should only contain digits
    try:
      # do the calculations
      if units_p[1] == "+":
        answer = str(int(float(units_p[0]) + float(units_p[2])))
      else:
        answer = str(int(float(units_p[0]) - float(units_p[2])))

      # arrange the problems vertically according to the length of 2 numbers
      if len(units_p[0]) == len(units_p[2]):
        first_line = first_line + " " * 2 + units_p[0] + " " * 4
        second_line = second_line + units_p[1] + " " + units_p[2] + " " * 4
        third_line = third_line + "-" * (len(units_p[0]) + 2) + " " * 4

        if len(answer) > len(units_p[0]) or len(answer) < 0:
          fourth_line = fourth_line + " " + answer + " " * 4
        else:
          fourth_line = fourth_line + " " * 2 + answer + " " * 4

      elif len(units_p[0]) > len(units_p[2]):
        first_line = first_line + " " * 2 + units_p[0] + " " * 4
        second_line = second_line + units_p[1] + " " * (
          len(units_p[0]) - len(units_p[2]) + 1) + units_p[2] + " " * 4
        third_line = third_line + "-" * (len(units_p[0]) + 2) + " " * 4

        if len(answer) > len(units_p[0]) or len(answer) < 0:
          fourth_line = fourth_line + " " + answer + " " * 4
        else:
          fourth_line = fourth_line + " " * 2 + answer + " " * 4

      elif len(units_p[0]) < len(units_p[2]):
        first_line = first_line + " " * (len(units_p[2]) - len(units_p[0]) +
                                         2) + units_p[0] + " " * 4
        second_line = second_line + units_p[1] + " " + units_p[2] + " " * 4
        third_line = third_line + "-" * (len(units_p[2]) + 2) + " " * 4

        if len(answer) > len(units_p[2]) or len(answer) < 0:
          fourth_line = fourth_line + " " + answer + " " * 4
        else:
          fourth_line = fourth_line + " " * 2 + answer + " " * 4

      else:
        print("Error!")

    # Rule 3's error message
    except:
      return "Error: Numbers must only contain digits."

  first_line = first_line.rstrip()
  second_line = second_line.rstrip()
  third_line = third_line.rstrip()
  fourth_line = fourth_line.rstrip()

  # optionally take a second argument for displaying answers
  if answers == True:
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
  else:
    arranged_problems = first_line + "\n" + second_line + "\n" + third_line

  return arranged_problems
