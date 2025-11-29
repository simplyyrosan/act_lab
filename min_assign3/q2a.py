#The code below was given by the sir but it doesn't print the series, give closet number only using recursive method


def fibonacciSeries(n):
    if n==0 or n==1:
        return n
    else:
    
        return fibonacciSeries(n-2)+fibonacciSeries(n-1)

print(fibonacciSeries(10))