class Basic(object):
    def ___init___(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getAge(self):
        return self.age

class Performance(object):
    def ___init___(self, height, weight, stance, wins, losses, ties, wins_record, division):
        self.height = height
        self.weight = weight
        self.stance = stance
        self.wins = wins
        self.losses = losses
        self.ties = ties
        
    def getHeight(self):
        return self.height

    def getWeight(self):
        return self.weight

    def getStance(self):
        return self.stance

    def getWins(self):
        return self.wins

    def getLosses(self):
        return self.losses

    def getTies(self):
        return self.ties
    
    def setWins_Record(self, wins, losses, ties):
        return self.wins/(self.wins + self.losses + self.ties)

    def getWins_Record(self):
        return self.wins_record

    def setDivision(self, weight):
        if self.weight < 125:
            self.division = "Strawweight"
        if self.weight >= 125 and self.weight < 135:
            self.division = "Flyweight"
        if self.weight >= 135 and self.weight < 145:
            self.division = "Bantamweight"
        if self.weight >= 145 and self.weight < 155:
            self.division = "Featherweight"
        if self.weight >= 155 and self.weight < 165:
            self.division = "Lightweight"
        if self.weight >= 165 and self.weight < 170:
            self.division = "Superlightweight"
        if self.weight >= 170 and self.weight < 175:
            self.division = "Welterweight"
        if self.weight >= 175 and self.weight < 185:
            self.division = "SuperWelterweight"
        if self.weight >= 185 and self.weight < 195:
            self.division = "Middleweight"
        if self.weight >= 195 and self.weight < 205:
            self.division = "SuperMiddleweight"
        if self.weight >= 205 and self.weight < 225:
            self.division = "LightHeavyweight"
        if self.weight >= 225 and self.weight < 265:
            self.division = "Cruiserweight"
        if self.weight >= 265:
            self.division = "Heavyweight"

    def getDivision(self):
        return self.division
            
        
    
