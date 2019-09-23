class Wizard():

    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print(f"Copying binaries -- {self.src} to {self.rootdir}")
            else:
                print("No operation")


if __name__ == "__main__":
    # Client code
    wizard = Wizard('python3.7.gzip', '/usr/bin/')
    # User chooses to install Python only
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()
