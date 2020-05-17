import obd
import logging

logger = logging.getLogger(__name__)
obd.logger.setLevel(obd.logging.DEBUG)


logger.info("Connecting to OBD-II")
connection = obd.OBD(timeout=1.5)  # auto-connects to USB or RF port

if connection is None:
    logger.error("OBD-II connection could not be made")
    exit()
else:
    logger.info("OBD-II connection successful")

# select an OBD command
speed_cmd = obd.commands.SPEED  # pylint: disable=no-member

# send the command, and parse the response
response = connection.query(speed_cmd)

print(response.value)
print(response.value.to("mph"))  # user-friendly unit conversions
