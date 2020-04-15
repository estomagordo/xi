class Player:
    def __init__(self, name, nationality, clubs, positions):
        this.name = name
        this.nationality = nationality
        this.clubs = clubs
        this.positions = positions


class Nation:
    def __init__(self, name):
        this.name = name


class Club:
    def __init__(self, name):
        this.name = name


class Position:
    def __init__(self, name):
        this.name = name


sweden = Nation('Sweden')
denmark = Nation('Denmark')
finland = Nation('Finland')
england = Nation('England')
netherlands = Nation('Netherlands')
belgium = Nation('Belgium')
france = Nation('France')
germany = Nation('Germany')
portugal = Nation('Portugal')
spain = Nation('Spain')
italy = Nation('Italy')
brazil = Nation('Brazil')
argentina = Nation('Argentina')
serbia = Nation('Serbia')
croatia = Nation('Croatia')
czechia = Nation('Czechia')

malmo = Club('Malmö')
liverpool = Club('Liverpool')
man_u = Club('Man U')
man_c = Club('Man C')
chelsea = Club('Chelsea')
tottenham = Club('Tottenham')
arsenal = Club('Arsenal')
celtic = Club('Celtic')
rangers = Club('Rangers')
west_ham = Club('West Ham')
barcelona = Club('Barcelona')
real_madrid = Club('Real Madrid')
atletico_madrid = Club('Atletico Madrid')
juventus = Club('Juventus')
milan = Club('Milan')
inter = Club('Inter')
lazio = Club('Lazio')
roma = Club('Roma')
bayern = Club('Bayern')
leverkusen = Club('Leverkusen')
monchengladbach = Club('Mönchengladbach')
dortmund = Club('Dortmund')
psg = Club('PSG')
lyon = Club('Lyon')
ajax = Club('Ajax')
psv = Club('PSV')
feyenoord = Club('Feyenoord')
blackburn = Club('Blackburn')
willem = Club('Willem II')
fulham = Club('Fulham')
rostock = Club('Hansa Rostock')

st = Position('Striker')
lm = Position('Left midfield')
cm = Position('Center midfield')
rm = Position('Right midfield')
lb = Position('Left back')
cb = Position('Center back')
rb = Position('Right back')
gk = Position('Goalkeeper')

players = [
    Player('Ibhrahimovic', sweden, { malmo, ajax, juventus, inter, barcelona, milan, psg }, [st]),
    Player('Ljungberg', sweden, { arsenal, celtic, west_ham }, [lm, cm, rm]),
    Player('Andersson', sweden, { malmo, monchengladbach, blackburn, bayern, barcelona }, [cb]),
    Player('Schmeichel', denmark, { man_u }, [gk]),
    Player('Hyypiä', finland, { willem, liverpool, leverkusen }, [cb]),
    Player('Litmanen', finland, { fulham, malmo, rostock, ajax, liverpool, barcelona }, [st, cm])
]