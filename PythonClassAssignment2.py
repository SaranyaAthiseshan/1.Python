class assignment2:
    def SubfieldsInAI():
        SubfieldsInAI=("Sub-fields in AI Are:", "Machine Learning", "Neural Networks", "Vision", "Speech Processing", "Natural Language Processing")
        for a in SubfieldsInAI:
            print(a)
    
    def OddEven():
        OddEven=int(input("Enter the number: "))
        if((OddEven%2)==1):
            print(OddEven, " is Odd Number")
        else:
            print(OddEven," is Even Number")
    
    def ElegiblityForMarriage():
        Gender=input("Your Gender: ")
        Age=int(input("Your Age: "))
        if(Gender=='Male'):
            if(Age>=21):
                print("Elegible")
            else:
                print("Not Elegible")
        elif(Gender=='Female'):
            if(Age>=18):
                print("Elegible")
            else:
                print("Not Elegible")
        else:
            print("Nothing found")
    
    def FindPercent():
        Subject1=int(input("Subject1= "))
        Subject2=int(input("Subject2= "))  
        Subject3=int(input("Subject3= "))
        Subject4=int(input("Subject4= "))
        Subject5=int(input("Subject5= "))
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:" ,Total)
        Percentage=float(Total/5)
        print("Percentage: ",Percentage)
    
    def triangle():
        H=int(input("Height: "))
        B=int(input("Breadth: "))
        Area=(H*B)/2
        print("Area of Triangle: ",Area)
        H1=int(input("Height1: "))
        H2=int(input("Height2: "))
        B2=int(input("Breadth: "))
        Perimeter=H1+H2+B2
        print("Perimeter of Triangle: ",Perimeter)