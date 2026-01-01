class Agent:
    def handle(self, user_input):
        return {
            "type": "ui.update",
            "component": "text",
            "content": f"Agent received: {user_input}"
        }


agent = Agent()
print(agent.handle("Start analysis"))
