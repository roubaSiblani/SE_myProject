class Driver:
  
  def __init__(self,worker_Id, name, start_city):
      self.worker_Id= worker_Id
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
      self.driversMenu()
    elif choice == "3":
      print("exit system, Goodbye!")
    else:
      print("Invalid choice, please try again")
    