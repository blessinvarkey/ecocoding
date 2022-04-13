#Import python modules
#Visualisation
#Model


#Energy Usage
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()

def main():

##TO DO: 



if __name__ == "__main__":
    tracker.start()
    main()
    emi: float=tracker.stop()
    print(f"overall emmisions:{emi} kg")
    emi= emi*89875517873681764
    print(f"overall emmisions:{emi} joules")
    # energyusage.evaluate(main,pdf=True)
