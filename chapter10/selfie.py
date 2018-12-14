class Arm:
    def __init__(self, arg):  # constructor
        self.state = arg  # variable defined in the constructor so it could be used inside class functions (glob)

    def handlePrint(self):
        print(self.state)


varInsideClass = Arm("Welcome")
varInsideClass.handlePrint()

# variable = Arm("Welcome").handlePrint() // it could also worked but nah
