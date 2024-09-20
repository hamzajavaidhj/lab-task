# modelbasedreflexagent..

class Model_Based_Reflex_Agent:
    def __init__(self, desiredtemperature):
        self.desiredtemperature = desiredtemperature
        self.previousaction = None

    def perceive(self, currenttemperature):
        return currenttemperature

    def act(self, currenttemperature):
        if currenttemperature < self.desiredtemperature:
            action = "Turn on heater"
        elif currenttemperature >= self.desiredtemperature and self.previousaction != "Turn off heater":
            action = "Turn off heater"
        else:
            action = "No action needed"
        
        self.previousaction = action
        return action
rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}

desiredtemperature = 22
agent = Model_Based_Reflex_Agent(desiredtemperature)
for room, temperature in rooms.items():
    action = agent.act(temperature)
    print(f"{room}: Current temperature = {temperature}°C. {action}.")

