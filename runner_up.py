#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
#You are given N scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    ar = map(int, input().split())                         #Takes input, splits it at whitespaces and maps the string input with int function to convert string array to integer    
    ar_set = set(ar)                                       #Converts the integer array to set to remove duplicates
    ar_list = list(ar_set)                                 #Converts set to list to make the iterable ordered and indexed
    ar_list.sort(reverse = True)                           #Sorts the list in descending order
    print(ar_list[1])                                      #Prints second element of the list which will be the 2nd largest element i.e the runner up

