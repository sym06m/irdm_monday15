def safe_ui(component):
    allowed = ["text", "button", "form"]
    if component["type"].split(".")[-1] not in allowed:
        return {"type": "ui.error", "message": "Invalid UI component"}
    return component


ui_component = {"type": "ui.text", "content": "Hello"}
print(safe_ui(ui_component))
