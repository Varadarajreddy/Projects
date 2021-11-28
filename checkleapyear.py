year = int( input( "Enter a year to check" ) )
if year % 400 and year % 4 == 0:
    print( "its a leap year" )
elif year % 100 != 0:
    print( "its not a leap year" )
else:
    print( "Its not a leap year" )
