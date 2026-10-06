airports={}



while True:

     command=input("enter a command")
     if command == "quit":
       break

     elif command=="":

      code=input("what is the code")
      name=input("enter the airports name")


      airports[code]= name

     elif command== "fetch":
        print("what airport code do u want to fetch") 
        print(airports[code])