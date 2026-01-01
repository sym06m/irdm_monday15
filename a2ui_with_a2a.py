def planner_agent():
    return "Create bakery business plan"


def ui_agent(message):
    return {
        "type": "ui.text",
        "content": f"Planner says: {message}"
    }


plan = planner_agent()
ui_update = ui_agent(plan)

print(ui_update)
