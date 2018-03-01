from src.Direction import Direction
from src.Ride import Ride
from src.Intersection import Intersection

class Car():
    location: "Intersection"
    ride: "Ride"
    previousRides: list
    timeWhenAvailable: int

    def __init__(self):
        self.location = Intersection(0, 0)
        self.ride = None
        self.previousRides = []
        self.timeWhenAvailable = 0

    def isAvailable(self) -> bool:
        return self.ride == None

    def addRide(self, ride: "Ride", currentTime: int) -> None:
        self.ride = ride
        self.location = ride.endLocation

        distance: int = self.location.distanceTo(ride.startLocation)
        self.timeWhenAvailable = currentTime + distance + ride.time()

    def update(self, currentTime, nextRide):
        if currentTime == self.timeWhenAvailable:
            try:

                self.previousRides.append(self.ride.id)
            except:
                pass

            self.addRide(nextRide, currentTime)
            return True

        return False

        # def canFinishRide(self, ride: "Ride", timeLeft: int) -> int:
        #     distance: int = self.currentLocation.distanceTo(ride.startLocation)

        #     frames: int = (distance + ride.time()) - timeLeft

        #     return frames > 0

        # def getWeight(self, ride: "Ride", timeLeft: int) -> int:
        #     if self.canFinishRide(ride, timeLeft):
        #         return 0

        #     distanceToRide = self.currentLocation.distanceTo(ride.startLocation)

        #     return distanceToRide - ride.time()

        # def move(self):
        #     if (self.drivingQueue != []):
        #         nextInstruction = self.drivingQueue[0]
        #         if(nextInstruction == Direction.NORTH):
        #             self.moveNorth()
        #         if(nextInstruction == Direction.EAST):
        #             self.moveEast()
        #         if(nextInstruction == Direction.SOUTH):
        #             self.moveSouth()
        #         if(nextInstruction == Direction.WEST):
        #             self.moveWest()

        # def moveNorth(self):
        #     self.currentLocation.row += 1

        # def moveEast(self):
        #     self.currentLocation.column += 1

        # def moveSouth(self):
        #     self.currentLocation.row -= 1

        # def moveWest(self):
        #     self.currentLocation.column -= 1

    def getSubmissionLine(self) -> str:
        line: str = str(len(self.previousRides))

        for rideId in self.previousRides:
            line += " {:d}".format(rideId)

        return line
