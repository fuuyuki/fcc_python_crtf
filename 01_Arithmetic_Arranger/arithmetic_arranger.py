from tabulate import SEPARATING_LINE, tabulate

def arithmetic_arranger(problems, display="False"):
  row1 = []
  row2 = []
  row3 = ""
  res = []
  # Check if the equation is valid
  if len(problems) > 5:
    return "Error: Too many problems."
    
  # Split the equation into a dictionary of operand
  for i in range(len(problems)):
    num_space = ""
    equation = problems[i].split(" ")
  
    if len(equation) > 3:
      return "Error: Input the correct equation format"
  
    # Check if the operands are valid
    operand1 = equation[0]
    operator = equation[1]
    operand2 = equation[2]
    
    if operator == "+" or operator == "-":
      if not operand1.isdigit() or not operand2.isdigit():
        return "Error: Numbers must only contain digits."
      
      if len(operand1) > 4 or len(operand2) > 4:
        return "Error: Numbers cannot be more than four digits."
      
      if operator == "+":
        result = int(operand1) + int(operand2)
      else: result = int(operand1) - int(operand2)
        
    else:
      return "Error: Operator must be '+' or '-'."
    
    if len(operand1) > len(operand2): num = len(operand1)+2
    else: num = len(operand2)+2
    for n in range(num): row3 += "-"
    if i != (len(problems)-1): row3 += "    "
    
    for n in range(num-len(operand2)-1): num_space += " " 
    row2.append(operator+num_space+operand2)
    if i != (len(problems)-1): row2.append("    ")

    num_space = ""
    for n in range(num-len(operand1)): num_space += " " 
    row1.append(num_space+operand1)
    if i != (len(problems)-1): row1.append("    ")
      
    num_space = ""
    for n in range(num-len(str(result))): num_space += " "
    res.append(num_space+str(result))
    if i != (len(problems)-1): res.append("    ")
  
  row1.append("\n")
  row2.append("\n")
  row3 = list(row3)
  
  arranged_problems = ""
  if display == True:
    row3.append("\n")
    arranged_problems = arranged_problems.join(row1+row2+row3+res)
  else:
    arranged_problems = arranged_problems.join(row1+row2+row3)

  return str(arranged_problems)