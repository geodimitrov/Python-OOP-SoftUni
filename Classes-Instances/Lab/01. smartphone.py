class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self):
        if not self.is_on:
            self.is_on = True

    def install(self, app, app_memory):
        if self.memory < app_memory:
            return f"Not enough memory to install {app}"

        if not self.is_on:
            return f"Turn on your phone to install {app}"

        self.memory -= app_memory
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"

# Test Code
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())