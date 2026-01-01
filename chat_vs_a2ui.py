def chat_agent():
    return "Here is the answer as text"


def a2ui_agent():
    return {
        "type": "ui.layout",
        "components": [
            {"type": "text", "content": "Here is the answer"},
            {"type": "button", "label": "Next"}
        ]
    }


print(chat_agent())
print(a2ui_agent())
