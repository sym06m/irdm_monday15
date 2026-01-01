def layout(components):
    return {
        "type": "ui.layout",
        "components": components
    }


ui = layout([
    {"type": "text", "content": "Business Assistant"},
    {"type": "input", "name": "idea"},
    {"type": "button", "label": "Analyze"}
])

print(ui)
