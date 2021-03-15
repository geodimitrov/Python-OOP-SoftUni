
def play_instrument(instrument):
    return instrument.play()

# test code
class Guitar:
    def play(self):
        print("playing the guitar")

guitar = Guitar()
play_instrument(guitar)