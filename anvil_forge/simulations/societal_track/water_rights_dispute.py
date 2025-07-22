class WaterRightsSimulation:
    def __init__(self, regions):
        self.regions = regions  # e.g., [{'name': 'Agri-Zone', 'demand': 100}, ...]
        self.water_supply = 250
        self.turn = 0

    def step(self, agent_actions):
        """Processes one round of negotiations."""
        print(f"Turn {self.turn}: Processing actions {agent_actions}")
        # Logic for updating state based on agent proposals goes here
        self.turn += 1
        return self.get_state()

    def get_state(self):
        """Returns the current state of the simulation."""
        return {
            "turn": self.turn,
            "water_supply": self.water_supply,
            "regions": self.regions
        }
