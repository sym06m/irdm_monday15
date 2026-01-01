def a2ui_message(component, content):
    return {
        "type": "ui.update",
        "component": component,
        "content": content
    }


msg = a2ui_message(
    component="text",
    content="Welcome to the AI assistant"
)

print(msg)
