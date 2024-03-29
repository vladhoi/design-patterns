class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck,
                                          cls).__new__(cls, *args, **kwargs)

        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def add_server(self):
        self._servers.append('Server1')
        self._servers.append('Server2')
        self._servers.append('Server3')
        self._servers.append('Server4')

    def change_server(self):
        self._servers.pop()
        self._servers.append('Server5')


hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.add_server()
print("Schedule health check for servers (1)..")
for i in range(4):
    print(f"Checking {hc1._servers[i]}")

hc2.add_server()
print("Schedule health check for servers (2)..")
for i in range(4):
    print(f"Checking {hc2._servers[i]}")
