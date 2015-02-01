class Monsters:
    spikes = 123
    scaryness = 100

    def boo(self):
        print("Boo! Gotcha!")
        print("I have:", self.spikes, "Spikes")
        spikes = input("How many do you have? ")
        if int(spikes) < self.spikes:
            print("Ha! I have more spikes than you!")

        else:
            print("Aw man, you have more spikes than me!")

    def __init__(self, scaryness, spikes):
        self.scaryness = scaryness
        self.spikes = spikes

Type =  Monsters(1000, 678)
Type.boo()
