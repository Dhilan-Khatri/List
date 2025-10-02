def square_filter(start, end):
    squares = [x**2 for x in range(start, end + 1)]


    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]

    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)

num1=int(input("Please Enter Starting Number: "))
num2=int(input("Please Enter Ending Number: "))
print("The square of inbetween are ")
print(square_filter(num1, num2))