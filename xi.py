class Player:
    def __init__(self, name, nationality, clubs, positions):
        self.name = name
        self.nationality = nationality
        self.clubs = clubs
        self.positions = positions


class Nation:
    def __init__(self, name):
        self.name = name


class Club:
    def __init__(self, name):
        self.name = name


class Position:
    def __init__(self, name):
        self.name = name


class Team:
    def __init__(self, players, positions):
        self.players = players
        self.positions = positions

    def find_xis(self):
        players_for_positions = list(map(
            lambda position: [player for player in self.players if position in player.positions],
            self.positions
            ))        

        def search(xis, n, player_names, nations, clubs):
            if n == 11:
                xis.append(player_names)
                return

            for player in players_for_positions[n]:
                if player.nationality not in nations and not player.clubs & clubs:
                    search(xis, n +1, list(player_names) + [player.name], nations | { player.nationality }, clubs | player.clubs)

        xis = search([], 0, [], set(), set())

        return xis


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
romania = Nation('Romania')
bulgaria = Nation('Bulgaria')
slovenia = Nation('Slovenia')
senegal = Nation('Senegal')
egypt = Nation('Egypt')
scotland = Nation('Scotland')
gabon = Nation('Gabon')
poland = Nation('Poland')
algeria = Nation('Algeria')
norway = Nation('Norway')

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
dc = Club('DC United')
chicago = Club('Chicago')
parma = Club('Parma')
brescia = Club('Brescia')
stuttgart = Club('Stuttgart')
padova = Club('Padova')
bologna = Club('Bologna')
fiorentina = Club('Fiorentina')
vicenca = Club('Vicenza')
sampdoria = Club('Sampdoria')
southampton = Club('Southampton')
groningen = Club('Groningen')
lille = Club('Lille')
schalke = Club('Schalke 04')
benfica = Club('Benfica')
ny = Club('New York')
monaco = Club('Monaco')
la = Club('Los Angeles Galaxy')
wolfsburg = Club('Wolfsburg')
bremen = Club('Werder Bremen')
lens = Club('Lens')
bordeaux = Club('Bordeaux')
cannes = Club('Cannes')
sporting = Club('Sporting')
fenerbahce = Club('Fenerbahce')
saint_etienne = Club('Saint Etienne')
leicester = Club('Leicester')
le_havre = Club('Le Havre')
salzburg = Club('Salzburg')
caen = Club('Caen')
valencia = Club('Valencia')
celta = Club('Celta Vigo')
eibar = Club('Eibar')

st = Position('Striker')
lw = Position('Left wing')
rw = Position('Right wing')
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
    Player('Litmanen', finland, { fulham, malmo, rostock, ajax, liverpool, barcelona }, [st, cm]),
    Player('Michael Laudrup', denmark, { ajax, real_madrid, barcelona, juventus, lazio }, [cm]),
    Player('Stoichkov', bulgaria, { dc, chicago, barcelona, parma }, [lw, st]),
    Player('Hagi', romania, { barcelona, real_madrid, brescia }, [lm, cm]),
    Player('Lahm', germany, { stuttgart, bayern }, [rb]),
    Player('Maldini', italy, { milan }, [lb, cb]),
    Player('Del Piero', italy, { juventus, padova }, [st, cm]),
    Player('Baggio', italy, { milan, inter, brescia, bologna, vicenca, fiorentina, juventus }, [cm, st]),
    Player('Gullit', netherlands, { milan, chelsea, sampdoria, psv, feyenoord }, [cm, rw]),
    Player('van Basten', netherlands, { milan, ajax }, [st]),
    Player('van Dijk', netherlands, { southampton, liverpool, celtic, groningen }, [cb]),
    Player('Buffon', italy, { juventus, parma, psg }, [gk]),
    Player('Hazard', belgium, { chelsea, lille, real_madrid }, [lw, cm, rw]),
    Player('Neuer', germany, { bayern, schalke }, [gk]),
    Player('Oblak', slovenia, { benfica, atletico_madrid }, [gk]),
    Player('Henry', france, { ny, barcelona, arsenal, juventus, monaco }, [st, lw]),
    Player('Sterling', england, { liverpool, man_c }, [lw, rw, st]),
    Player('Ronaldo', brazil, { milan, real_madrid, inter, barcelona, psv }, [st]),
    Player('Mané', senegal, { liverpool, southampton }, [lw, st, rw]),
    Player('Salah', egypt, { liverpool, chelsea, roma, fiorentina }, [lw, st, rw]),
    Player('Gerrard', england, { liverpool, la }, [cm]),
    Player('de Bruyne', belgium, { man_c, chelsea, bremen, wolfsburg }, [cm]),
    Player('Messi', argentina, { barcelona }, [st, rw]),
    Player('Alexander-Arnold', england, { liverpool }, [rb]),
    Player('Robertson', scotland, { liverpool }, [lb]),
    Player('Varane', france, { lens, real_madrid }, [cb]),
    Player('Zidane', france, { cannes, bordeaux, juventus, real_madrid }, [cm, lm]),
    Player('Cristiano Ronaldo', portugal, { man_u, sporting, real_madrid, juventus }, [lw, st, rw]),
    Player('Fabinho', brazil, { liverpool, monaco }, [cm]),
    Player('Cafu', brazil, { milan, roma }, [rb, rm]),
    Player('Roberto Carlos', brazil, { fenerbahce, real_madrid, inter }, [lb]),
    Player('Aubameyang', gabon, { saint_etienne, arsenal, dortmund, milan, monaco, lille }, [lw, st, rw]),
    Player('Lewandowski', poland, { bayern, dortmund }, [st]),
    Player('Mahrez', algeria, { leicester, man_c, le_havre }, [rw, rm, cm]),
    Player('Courtois', belgium, { chelsea, real_madrid, atletico_madrid }, [gk]),
    Player('Alisson', brazil, { liverpool, roma }, [gk]),
    Player('Haaland', norway, { salzburg, dortmund }, [st]),
    Player('Kante', france, { leicester, chelsea, caen }, [cm]),
    Player('Vieira', france, { arsenal, man_c, inter, juventus, milan, cannes }, [cm]),
    Player('Xavi', spain, { barcelona }, [cm]),
    Player('David Silva', spain, { valencia, man_c, celta, eibar }, [cm, lm]),
]

team_433 = Team(players, [gk, lb, cb, cb, rb, cm, cm, cm, lw, st, rw])

for xi in team_433.find_xis():
    for player in xi:
        print(player.name)

    print()