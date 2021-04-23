#Name: Bennett Johnson
#File Name: calFunction

#This function describes how the calculator is used
def basicCalculator(num1,num2):
    operateChoice = input("Enter what operation to perform(+,-.*./): ");
    if(operateChoice=="+"):
        result = num1 + num2;      #This if statement adds the numbers

    elif(operateChoice=="-"):
        result = num1 - num2;      #This statements subtracts the numbers

    elif(operateChoice=="*"):
        result = num1 * num2;      #This statement multiplies the numbers

    elif(operateChoice=="/"):
        result = num1 / num2;      #This statement divides

    return result;


#The main programs stats now

def main():
    print("This is a simple calculator to do simple mathematical calculations");
    print();
    operand_1 = int(input("Enter first INTEGER number: "));    #This asks user to enter numbers for the operation. The term integer is capitalized to emphazize on
    operand_2 = int(input("Enter second INTEGER number: "));   #using integer numbers only
    prompt_2 = "Y";
    while(prompt_2 =="Y"):            #Using the while loop to do the calculation
        Result = basicCalculator(operand_1,operand_2);#Function call with operand_1 and operand_2 as its parameters
        print(Result);
        prompt = input("Do you wnat to continue with the calculation(Y/N): ");
        while(prompt =="Y"):
            newOperand = int(input("Enter another INTEGER number: "));  #Loop for users who wants to continue calculating from the result
            Result = basicCalculator(Result,newOperand);  #Function call with Result and newOperand as parameter
            print(Result);
            prompt = input("Do you want to continue: ");
        prompt_2 = input("Do you want to start a new calculation(Y/N): ");

main();   #Calling the main function
    
    
