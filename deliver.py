class Driver:
  
  def __init__(self,driver_Id, name, start_city):
      self.driver_Id= driver_Id
      self.name= name
      self.start_city= start_city

class WeDeliver:
  # constructor
  def __init__(self,drivers,cities):
    self.drivers=[]
    self.cities= ["Akkar", "Saida", "Jbeil"]
    self.deliveries={}
    self.driver_id_counter = 1

  #  The main menue of the system  
  def mainMenue(self):
    choice =None
    while choice != "3":
      print("Hello! Please enter:")
      print("1.To go to the drivers’ menu")
      print("2.To go to the cities’ menu")
      print("3.To exit the system")

    choice=input("Select an option:")

    if choice == "1":
      self.driversMenu()
    elif choice == "2":
      self.citiesMenu()
    elif choice == "3":
      print("exit system, Goodbye!")
    else:
      print("Invalid choice, please try again")
    
   #The driversMenu:
  def driversMenu():
    while True:
      print("Enter:")
      print("1.To view all the drivers")
      print("2.To add a driver")
      print("3.To go back to main menu")

      choix=input()

      if choix == "1":
        self.view_all_drivers()
      elif choix == "2":
        self.add_driver()
      elif choix == "3":
          break
      else:
          print("Invalid choice, please try again.")
  
  def view_all_drivers(self):
        print("\nList of all drivers:")
        if not self.drivers:
            print("No drivers in the system.")
        for driver in self.drivers:
            print(driver)