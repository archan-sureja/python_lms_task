""" GCD """
word_num_map = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
}
num_word_map = { v : k for k,v in word_num_map.items()}
def word_to_num(word : str,current_word: str) -> str:
    """
    Converts given word in number 
    params : 
        word - str represting input word 
    return : 
        int - coresponding integer for given word 
    """
    if word=="":
        return word_num_map[current_word] if current_word in word_num_map else ""
    elif current_word in word_num_map:
       return word_num_map[current_word] + word_to_num(word,"")
    else:
        return word_to_num(word[1:],current_word+word[0])


def num_to_word(num:int) -> str:
    """
    Converts given number to word using recursion
    params : 
        num : int - input number 
    return 
        str : number as word 
    """
    if num == 0:
        return "zero"
    if num < 10:
        return num_word_map[str(num)]   
    else:
        return num_to_word(num//10) + num_word_map[str(num%10)]
def gcd(n1:str,n2:str)->str:

    """
        Calculates GCD of num1,num2 
        params : 
            num1 : number 1 
            num2 : number 2 
        return :
            int : gcd(num1,num2)
    """

    if n2 == 0:
        return n1
    else:
        return gcd(n2,n1%n2)

def main():
    """ main function """
    num1 = input("Enter first number in word : ")
    num2 = input("Enter second number in word : ")
    try:
        n1 = int(word_to_num(num1,""))
        n2 = int(word_to_num(num2,""))
    except KeyError as ex:
        raise ValueError("Invalid input word(s).")
    print(f"GCD of {num1} and {num2} is {num_to_word(gcd(n1,n2))}")

main()