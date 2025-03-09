from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

class InfluxDBClass:

    connection_data={
        "url":"http://localhost:8086",
        "bucket":"mybucket",
        "org":"myorg",
        "token":"cAg2K0eBC1oY5AuaeXz4BNLy_fMhhUFxlUdfgxHKdSeTxjaAMcOHrwrGkflz6m0cvP9Q5BxgCR3Lrohq_o80kA=="
    }

    @staticmethod
    def write_to_influxDB():
        url=InfluxDBClass.connection_data["url"]
        token=InfluxDBClass.connection_data["token"]
        org=InfluxDBClass.connection_data["org"]
        bucket=InfluxDBClass.connection_data["bucket"]

        client = InfluxDBClient(url=url, token=token, org=org)
        write_api = client.write_api(write_options=SYNCHRONOUS)
        p = Point("my_measurement").tag("location", "Prague").field("temperature", 25.3)
        write_api.write(bucket=bucket, record=p)
        client.close()
    
    @staticmethod
    def show_data():
        url=InfluxDBClass.connection_data["url"]
        token=InfluxDBClass.connection_data["token"]
        org=InfluxDBClass.connection_data["org"]
        bucket=InfluxDBClass.connection_data["bucket"]

        client = InfluxDBClient(url=url, token=token, org=org)
        query_api = client.query_api()

        tables = query_api.query('from(bucket:"'+bucket+'") |> range(start: -10m)')
        for table in tables:
            print(table)
            for row in table.records:
                print (row.values)
        client.close()