import ctypes

class Array(object):
    
    def __init__(self, size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        assert 0 <= index < len(self), "Array subscript out of range"
        return self._elements[index]

        
    def __setitem__(self, index, value):
        assert 0 <= index < len(self), "Array subscript out of range"
        self._elements[index] = value

        
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

class Queue(object):
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0

    def isEmpty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
        self._qhead = self._qhead.next
        self._count -= 1
        return node.item

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

class Passenger :
# Creates a passenger object.
 def __init__( self, idNum, arrivalTime ):
  self._idNum = idNum
  self._arrivalTime = arrivalTime

# Gets the passenger's id number.
 def idNum( self ) :
  return self._idNum

# Gets the passenger's arrival time.
 def timeArrived( self ) :
  return self._arrivalTime

class TicketAgent(object):
    def __init__(self, idNum):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    
    def idNum(self):
        return self._idNum

    
    def isFree(self):
        return self._passenger is None

    
    def isFinished(self, curTime):
        return self._passenger is not None and self._stopTime == curTime

    
    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    
    def stopService(self):
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger

from random import random

class TicketCounterSimulation :
 
 # Create a simulation object.
    def __init__( self, numAgents, numMinutes, betweenTime, serviceTime ):
            # Parameters supplied by the user.
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes

            # Simulation components.
        self._passengerQ =Queue()
        self._theAgents = Array(numAgents)
        for i in range( numAgents ) :
            self._theAgents[i] = TicketAgent(i+1)

            # Computed during the simulation.
        self._totalWaitTime = 0
        self._numPassengers = 0

 # Run the simulation using the parameters supplied earlier.
    def run(self):
        for curTime in range(1, self._numMinutes + 1):
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def printResults(self):
        numServed = self._numPassengers - len(self._passengerQ) 
        avgWait = float(self._totalWaitTime) / numServed
        print("")

        print ("Number of passengers served = %d" % numServed)
        print (("Number of passengers remaining in line = %d") % len(self._passengerQ))
        print (("The average wait time was %4.2f minutes.\n") % avgWait)

    def _handleArrival(self, curTime):
        odds = random()
        
        if odds <= self._arriveProb:
             self._numPassengers += 1
             #self._numPassengers
             passenger = Passenger(self._numPassengers, curTime)
             self._passengerQ.enqueue(passenger) 
             print(("Time %4d    Passenger %d arrived.") % (curTime, passenger.idNum()))
             

    def _handleBeginService(self, curTime):
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.dequeue()
                self._totalWaitTime = (curTime - passenger.timeArrived())
                print(("Time %4d    Agent %d started serving passenger %d") % (curTime, self._theAgents[i].idNum(), passenger.idNum()))


   
    def _handleEndService(self, curTime):
        for i in range(len(self._theAgents)):
            if self._theAgents[i].isFinished(curTime):
                passenger = self._theAgents[i].stopService()
                print (("Time %d    Agent %d stopped serving passenger %d") % (curTime, self._theAgents[i].idNum(), passenger.idNum()))

if __name__ == "__main__":
     num_minutes=int(input("\nNumber of minutes to simulate:"))
     num_agents=int(input("Number of ticket agents:"))
     service_time=int(input("Average service time per passenger:"))
     between_time=int(input("Average time between passenger arrival:"))

     TCSimulation = TicketCounterSimulation(num_agents, num_minutes, between_time, service_time)
     TCSimulation.run()
     TCSimulation.printResults()
