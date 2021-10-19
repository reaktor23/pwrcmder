# Count the hackers that are currently in the Hackerspace
hackers = 0

for person in hass.states.entity_ids('person'):
    state = hass.states.get(person)
    if state.name != "Reaktor23" and state.state == "home":
        hackers = hackers + 1

hass.states.set('sensor.hackers', hackers, {
    'unit_of_measurement': 'hackers',
    'friendly_name': 'Hackers in Hackerspace'
    })
