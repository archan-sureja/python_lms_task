def check_balance_parentheses(brackets:str)->bool:
    '''
    Checks if the given string of parentheses is balanced or not
    params:
        brackets : string - a string of parentheses
    return:
        bool - True if balanced, else False
    '''

    s = []
    help_map = {")":"(" , "}":"{" , "]":"["}
    for ch in brackets:
        if len(s)==0:
            if ch=="(" or ch=="{" or ch=="[": s.append(ch)
            else: return False
        else:
            if ch in help_map and s[-1]==help_map[ch]:
                s.pop()
            elif ch in ('(',"{","["):
                s.append(ch)
            else:
                return False 
    return len(s)==0

def generate_parentheses(n : int) -> list[str]:
    '''
        Generatea all combinations for n pairs of parentheses
        params:
            n:int - number of pairs of parentheses
        return: 
            list of strings - all combinations of parentheses
    '''
    def backtrack(s="",left=0,right=0):
        if len(s)==2*n:
            res.append(s)
            return
        if left<n:
            backtrack(s+"(",left+1,right)
        if right<left:
            backtrack(s+")",left,right+1)
    res = []
    backtrack()
    return res

def main():
    ''' main function '''
    n = int(input("Enter number of pairs of parentheses : "))
    print(list(filter(check_balance_parentheses,generate_parentheses(n))))

main()