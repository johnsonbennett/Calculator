# This is a program to do simple mathematic calculations
# Name: Bennett Johnson
# File name: BasicCalc.py

userName = input("Enter your name: ");   
print("Hello " + userName);
print();


print("This is a simple calculator program to do simple mathematical calculations")
prompt ="Y";
prompt_2 ="N";
while prompt =="Y":

    
      Result =0;
      operand_1 =int(input("Enter your first  integer number: "));   # Asking user for the numbers for the math operation
      operand_2 = int(input("Enter your second  integer number: "));

      print();
      operatChoice = input("Choose what operation to perform (+,-,*,/): ");  #Operation choice
      if(operatChoice=="+" ):
           result = operand_1 + operand_2;
           print(result);                                 # if-else statements to do different operations

      elif(operatChoice =="-"):
           result =operand_1 - operand_2;
           print( result);

      elif(operatChoice =="*"):
           result = operand_1 * operand_2;
           print(result);

      elif(operatChoice =="/"):
           result = operand_1 / operand_2;
           print(result);
    
      else:
          operateChoice = input("Choose either +,-,* or /: ");
      
      prompt_2 = input("Do you want to continue with the same calculation: ");
      while(prompt_2== "Y"):   # Another while loop for users who wants to continue with the calculation
          Result = result
          operandCon = int(input("Enter another integer to calculate: "));
          operatChoice = input("Choose + , - , * , / : ");         
          if(operatChoice=="+" ):
           result = Result + operandCon;
           print(result);

          elif(operatChoice =="-"):
               result = Result - operandCon;
               print( result);

          elif(operatChoice =="*"):
               result = Result * operandCon;
               print(result);

          elif(operatChoice =="/"):
               result = Result / operandCon;
               print(result);
    
          else:
              operateChoice = input("Choose either +,-,* or /: ");
          prompt_2 = input("Do you want to continue with the same calculation: ");
      prompt = input("Do you want to start a new calculation (Y/N): ");  # Prompt to see if user want to continue using 
      #the program
print();
print("See you later!");





