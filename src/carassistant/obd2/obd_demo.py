import obd

connection = obd.OBD(timeout=1.5)  # auto-connects to USB or RF port

# obd.logger.setLevel(obd.logging.DEBUG)
if connection is None:
    # TODO: log that the OBD connection couldnt be made
    exit()

cmd = obd.commands.SPEED  # select an OBD command (sensor)

response = connection.query(cmd)  # send the command, and parse the response

print(response.value)  # returns unit-bearing values thanks to Pint
print(response.value.to("mph"))  # user-friendly unit conversions
