from EventHandlers.InfluxHandler import InfluxDBClass

# myObj = InfluxDBClass()
InfluxDBClass.write_to_influxDB()
print(InfluxDBClass.show_data())