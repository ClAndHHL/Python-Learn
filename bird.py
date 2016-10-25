class Bird :
    def __init__(self):
        self.hungry = True;
    def eat(self):
        if self.hungry:
            print "Bird eat .."
        else:
            print "Bird eat  No thanks"

class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self);
        self.sound = "Squawk"
    def sing(self):
        print self.sound;


