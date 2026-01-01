def create_form(title, fields):
    return {
        "type": "ui.form",
        "title": title,
        "fields": fields
    }


form = create_form(
    "Bakery Setup",
    [
        {"name": "city", "type": "text"},
        {"name": "budget", "type": "number"}
    ]
)

print(form)
