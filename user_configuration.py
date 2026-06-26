def add_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    for existing_key in settings:
        if existing_key.lower() == key:
            return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    key, value = pair
    key = key.lower()
    value = value.lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    return f"Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    return "\n".join(lines) + "\n"


test_settings = {'theme': 'light', 'notifications': 'enable', 'volume': 'low'}
print(view_settings(test_settings))

print(delete_setting({'theme': 'light'}, 'sound'))