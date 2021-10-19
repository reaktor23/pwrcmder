
SENSORS = {
    "total": "mdi:emoticon-neutral-outline",
    "active": "mdi:emoticon-sad-outline",
    "recovered": "mdi:emoticon-happy-outline",
    "deaths": "mdi:emoticon-cry-outline",
    "incidence": "mdi:numeric-7-box",
}

PATTERNS = {
    "total": {"p": r"Positiv getestete Personen: (\d+)", "t": "int"},
    "active": {"p": r"Derzeit aktive Infektionen: (\d+)", "t": "int"},
    "recovered": {"p": r"Genesene Personen: (\d+)", "t": "int"},
    "deaths": {"p": r"Verstorbene Personen: (\d+)", "t": "int"},
    "incidence": {"p": r"7-Tage-Inzidenz: ([\d,]+)", "t": "float"}
}

MAP = r"<a.*><img class=\"image-embed-item\" src=\"([^\"]*)"
