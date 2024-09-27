# LAB 03




class SimpleReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature 

    def perceive(self, current_temperature):
        return current_temperature

    def act(self, current_temperature):
        if current_temperature < self.desired_temperature:
            action = "Turn on heater"
        else:
            action = "Turn off heater"
        return action

# Simulating different rooms with different current temperatures
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

# Desired temperature for all rooms
desired_temperature = 22
agent = SimpleReflexAgent(desired_temperature)

# Run the agent for each room
for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")




class ModelBasedReflexAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.heater_status = {}

    def perceive(self, room, current_temperature):
        return current_temperature

    def act(self, room, current_temperature):
        if room not in self.heater_status:
            self.heater_status[room] = "off"
        
        if current_temperature < self.desired_temperature and self.heater_status[room] == "off":
            action = "Turn on heater"
            self.heater_status[room] = "on"
        elif current_temperature >= self.desired_temperature and self.heater_status[room] == "on":
            action = "Turn off heater"
            self.heater_status[room] = "off"
        else:
            action = "Do nothing"  
        
        return action

# Simulating different rooms with different current temperatures
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

# Desired temperature for all rooms
desired_temperature = 22
agent = ModelBasedReflexAgent(desired_temperature)

# Run the agent for each room
for room, temperature in rooms.items():
    action = agent.act(room, temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")
