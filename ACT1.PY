class vehicle:
        def __init__(self, name, capacity):
                self.name = name
                self.capacity = capacity

        def fare(self):
                """Calculates the base fare for the vehicle."""
                return self.capacity * 100

class Bus(vehicle):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)

    def fare(self):
        """Calculates the total fare for the bus, including a 10% maintenance charge."""
        base_fare = super().fare()
        maintenance_charge = 0.10 * base_fare
        return base_fare + maintenance_charge


bus = Bus("School Bus", 50)
print(f"Total fare for the {bus.name}: ${bus.fare()}")

vehicle = vehicle("Generic Vehicle", 4)
print(f"Total fare for the {vehicle.name}: ${vehicle.fare()}")