
class Propostional_Logic:
    def __init__(self):
        self.p_values = ["T", "T", "F", "F"]
        self.q_values = ["T", "F", "T", "F"]
    
    def and_(self, listp, listq):
        and_TT = {("T", "T"): "T", ("T", "F"): "F", ("F", "T"): "F", ("F", "F"): "F"}
        and_result = []
        for i in range(4):
            and_result.append(and_TT[listp[i], listq[i]])
        return and_result

    def or_(self, listp, listq):
        or_TT = {("T", "T"): "T", ("T", "F"): "T", ("F", "T"): "T", ("F", "F"): "F"}
        or_result = []
        for i in range(4):
            or_result.append(or_TT[listp[i], listq[i]])
        return or_result

    def not_(self, listp):
        not_TT = {"F": "T", "T": "F"}
        not_result = []
        for i in range(4):
            not_result.append(not_TT[listp[i]])
        return not_result

    def implication_(self, listp, listq):
        implication_TT = {("T", "T"): "T", ("T", "F"): "F", ("F", "T"): "T", ("F", "F"): "T"}
        implication_result = []
        for i in range(4):
            implication_result.append(implication_TT[listp[i], listq[i]])
        return implication_result

    def Bi_Conditional_(self, listp, listq):
        bi_conditional_TT = {("T", "T"): "T", ("T", "F"): "F", ("F", "T"): "F", ("F", "F"): "T"}
        bi_conditional_result = []
        for i in range(4):
            bi_conditional_result.append(bi_conditional_TT[listp[i], listq[i]])
        return bi_conditional_result

    def Print_Result(self, expression, result):
        print()
        for i in range(51):
            print("-",end="")
        print()
        print("|", "   P   ", "|", "   Q   ", "|", "{:^27s}".format(expression),"|")
      
        for i in range(51):
            print("-",end="")
        print()
        for i in range(4):
            print("|", "  ", self.p_values[i], "  ", "|", "  ", self.q_values[i], "  ", "|", "            ", result[i], "            ", "|")
            for i in range(51):
                print("-",end="")
            print()
        print()

    def infix_to_postfix(self, expression):
        precedence = {'~': 5, '^': 4, 'v': 3, '->': 2, '<=>': 1}
        output = []
        operators = []
        i = 0

        while i < len(expression):
            token = expression[i]
            if(token=="-"):
                token='->'
                i+=1
            if(token=="<"):
                token='<=>'
                i+=2
            if token in {'p', 'q'}:
                output.append(token)
            elif token in precedence:
                while operators and precedence.get(operators[-1], 0) >= precedence.get(token, 0):
                    output.append(operators.pop())
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()
            i += 1

        while operators:
            output.append(operators.pop())
        return output

    def Expression_Evolution(self,expression):

        postfix = self.infix_to_postfix(expression)
        
        stack = []
        
        for token in postfix:
            if token in {'p', 'q'}:
                if token == 'p':
                    stack.append(self.p_values)
                elif token == 'q':
                    stack.append(self.q_values)
            else:
                if(token!="~"):
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                else:
                    operand2 = stack.pop()
                result = None
                
                if token == '~':
                    result = self.not_(operand2)
                elif token == '^':
                    result = self.and_(operand1, operand2)
                elif token == 'v':
                    result = self.or_(operand1, operand2)
                elif token == '->':
                    result = self.implication_(operand1, operand2)
                elif token == '<=>':
                    result = self.Bi_Conditional_(operand1, operand2)
                    
                stack.append(result)
        
        return stack[0]

    def is_tautology(self,expression):
        result=self.Expression_Evolution(expression)
        
        self.Print_Result(expression, result)

        tautology=0
        contradiction=0

        for i in result:
            if i=="T":
                tautology+=1
            else:
                contradiction+=1

        if(tautology==4):
            print("The Given Expression ",expression," is Tautology\n")
        elif(contradiction==4):
            print("The Given Expression",expression," is not Tautology (Contradiction)\n")
        else:
            print("The Given Expression",expression," is not Tautology (Contingent)\n")

    def are_equivalent(self,expression1,expression2):
        result1=self.Expression_Evolution(expression1)
        result2=self.Expression_Evolution(expression2)
        self.Print_Result(expression1, result1)
        self.Print_Result(expression2, result2)

        if(result1==result2):
            print("The Two Expressions are Logically Equivalent\n")
        else:
            print("The Two Expresssions are not Logically Equivalent")


print()
while(True):
    print("Enter 1 For Tautology Check\nEnter 2 For Logically Equivalent Check\nEnter 3 For Exit\n")
    choice=int(input("Enter Your Choice : "))

    if(choice==1):
        logic = Propostional_Logic()
        expression=input("\nEnter The Expression : ")
        logic.is_tautology(expression)

    elif(choice==2):
        logic = Propostional_Logic()
        expression1=input("\nEnter The Expression1 : ")
        expression2=input("Enter The Expression2 : ")
        logic.are_equivalent(expression1,expression2)
    else:
        break


# (p^(pvq))v(q<=>p)(~p->q)




