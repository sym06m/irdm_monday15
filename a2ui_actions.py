def action_button(label, action_id):
    return {
        "type": "ui.button",
        "label": label,
        "action": action_id
    }


button = action_button(
    label="Generate Plan",
    action_id="generate_business_plan"
)

print(button)
