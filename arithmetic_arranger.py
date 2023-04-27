from pytest import main

def arithmetic_arranger(problems, answers=False):
    print("The problems are: ", problems)
    print("Answers needed?: ", answers)
    
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    
    location = 0
  
    for problem in problems:
        location = location + 1
        units = problem.split()
        
        # Rule 1
        if len(problems) > 4: 
            return "Error: Too many problems."
            
        # Rule 2
        if units[1] != "+" and units[1] != "-" :
            return "Error: Operator must be '+' or '-'."
            
        # Rule 4
        if len(units[0]) > 4 or len(units[2]) > 4 :
            return "Error: Numbers cannot be more than four digits."
            
        # Rule 3
        try: 
            length = len(units[0]) + len(units[2])
            
            if units[1] == "+" :
                answer = str(int(float(units[0]) + float(units[2])))
            else :
                answer = str(int(float(units[0]) - float(units[2])))

            if len(units[0]) == len(units[2]):
                first_line = first_line + " "*2 + units[0] + " "*4
                second_line = second_line + units[1] + " " + units[2] + " "*4
                third_line = third_line + "-"*(len(units[0])+2) + " "*4
                
                if len(answer) > len(units[0]) or len(answer) < 0: 
                    fourth_line = fourth_line + " " + answer + " "*4
                else: 
                    fourth_line = fourth_line + " "*2 + answer + " "*4
            
            elif len(units[0]) > len(units[2]):
                first_line = first_line + " "*2 + units[0] + " "*4
                second_line = second_line + units[1] + " "*(len(units[0])-len(units[2])+1) + units[2] + " "*4
                third_line = third_line + "-"*(len(units[0]) + 2) + " "*4
                
                if len(answer) > len(units[0]) or len(answer) < 0: 
                    fourth_line = fourth_line + " " + answer + " "*4
                else: 
                    fourth_line = fourth_line + " "*2 + answer + " "*4
            
            elif len(units[0]) < len(units[2]):
                first_line = first_line + " " * (len(units[2])-len(units[0]) + 2) + units[0] + " "*4
                second_line = second_line + units[1] + " " + units[2] + " "*4
                third_line = third_line + "-" * (len(units[2]) + 2) + " "*4
                
                if len(answer) > len(units[2]) or len(answer) < 0: 
                    fourth_line = fourth_line + " " + answer + " "*4
                else: 
                    fourth_line = fourth_line + " "*2 + answer + " "*4
            
            else:
                print("Error!")
                
        except: 
            return "Error: Numbers must only contain digits."
        
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()
    
    if answers == True: 
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else: 
        arranged_problems = first_line + "\n" + second_line + "\n" + third_line
    
    return arranged_problems