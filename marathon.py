# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Midori Knecht}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {06/22/2022}
#
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

# $1 = 134.28¥
JAPANESE_YEN = 134.28

# 1 mi = 1609.34 meters
METERS_IN_MILE = 1609.34 
KM_IN_MILE = 1.60934

# Insert Code Below
def fitness():
  print("Tokyo marathon qualifier")
  
  name = input("Please enter your name: ")
  space = name.find(" ")
  lastName = name[space+1:]

  miles = float(input("How many miles can you run in 10 minutes? "))
  usMoney = input("How many U.S. $ do you have saved up? ")

  money = usMoney[1:]
  money = float(money)

  yen = money * JAPANESE_YEN
  pace = (miles * KM_IN_MILE) / 10

  print(f"Dear {lastName}, you have a pace of {pace:.2f} km/min.")
  print(f"Additionally you only have {yen:.2f}¥ to spend.")
    # This ignores our code so that we do not get an error Remove 'pass' when you want to start testing code.  
    
    

# This invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    fitness()
