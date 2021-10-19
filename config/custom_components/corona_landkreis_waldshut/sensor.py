import asyncio
import logging
from datetime import timedelta as td

from homeassistant.components.sensor import ENTITY_ID_FORMAT
from homeassistant.helpers.entity import Entity, async_generate_entity_id
from homeassistant.helpers.typing import HomeAssistantType

from . import DOMAIN
from .const import SENSORS

LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = td(seconds=60)


@asyncio.coroutine
def async_setup_platform(hass, config, async_add_devices, discovery_info=None):

    api = hass.data[DOMAIN]

    devices = []
    for sensor, icon in SENSORS.items():
        devices.append(CoronaWTSensor(hass, sensor, icon, api))
    devices.append(CoronaWTSensor(hass, 'map', 'mdi:map', api))
    async_add_devices(devices)
    LOGGER.debug("Platform setup done")


class CoronaWTSensor(Entity):
    def __init__(self, hass: HomeAssistantType, sensor, icon, api):
        self._sensor = sensor
        self._state = None
        self._icon = icon
        self._api = api

        self.entity_id = async_generate_entity_id(
            ENTITY_ID_FORMAT, f"corona_wt_{sensor}", hass=hass
        )

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._sensor

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {DOMAIN: "Data provided by Landkreis Waldshut"}

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return self._icon

    async def async_update(self):
        LOGGER.debug("Update entity %s started", self._sensor)
        self._state = await self._api.get_data(self._sensor)
        LOGGER.debug("Update entity %s finished", self._sensor)
