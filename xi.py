class Player:
    def __init__(self, name, nationality, clubs, positions, quality):
        self.name = name
        self.nationality = nationality
        self.clubs = clubs
        self.positions = positions
        self.quality = quality

    def __repr__(self):
        return self.name


class Nation:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Club:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Position:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Team:
    def __init__(self, players, positions):
        self.players = players
        self.positions = positions

    def find_xis(self):
        players_for_positions = list(map(
            lambda position: [player for player in self.players if position in player.positions],
            self.positions
            ))

        xis = []

        def search(n, players, nations, clubs):
            if n == 11:
                xis.append(players)
                return

            for player in players_for_positions[n]:
                if player.nationality not in nations and not player.clubs & clubs:
                    search( n +1, list(players) + [player], nations | { player.nationality }, clubs | player.clubs)

        search(0, [], set(), set())

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
cote_d_ivoire = Nation("Cote d'ivoire")
south_korea = Nation('South Korea')
uruguay = Nation('Uruguay')
colombia = Nation('Colombia')
cameroon = Nation("Cameroon")
australia = Nation('Australia')
ireland = Nation('Ireland')
wales = Nation('Wales')
austria = Nation('Austria')
turkey = Nation('Turkey')
chile = Nation('Chile')

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
newcastle = Club('Newcastle')
rennais = Club('Rennais')
olympiacos = Club('Olympiacos')
hamburg = Club('Hamburg')
bari = Club('Bari')
munich_1860 = Club('1860 Munich')
sevilla = Club('Sevilla')
boca = Club('Boca Juniors')
colorado = Club('Colorado')
tampa = Club('Tampa Bay')
miami = Club('Miami')
valladolid = Club('Valladolid')
montpellier = Club('Montpellier')
mallorca = Club('Mallorca')
everton = Club('Everton')
leeds = Club('Leeds')
nottingham = Club('Nottingham Forest')
hoffenheim = Club('Hoffenheim')
freiburg = Club('Freiburg')
river = Club('River Plate')
napoli = Club('Napoli')

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
    Player('Ibhrahimovic', sweden, { malmo, ajax, juventus, inter, barcelona, milan, psg }, [st], 9),
    Player('Ljungberg', sweden, { arsenal, celtic, west_ham }, [lm, cm, rm], 6),
    Player('Andersson', sweden, { malmo, monchengladbach, blackburn, bayern, barcelona }, [cb], 6),
    Player('Schmeichel', denmark, { man_u }, [gk], 9),
    Player('Hyypiä', finland, { willem, liverpool, leverkusen }, [cb], 7),
    Player('Litmanen', finland, { fulham, malmo, rostock, ajax, liverpool, barcelona }, [st, cm], 5),
    Player('Michael Laudrup', denmark, { ajax, real_madrid, barcelona, juventus, lazio }, [cm], 8),
    Player('Stoichkov', bulgaria, { dc, chicago, barcelona, parma }, [lw, st], 8),
    Player('Hagi', romania, { barcelona, real_madrid, brescia }, [lm, cm], 8),
    Player('Lahm', germany, { stuttgart, bayern }, [rb], 8),
    Player('Maldini', italy, { milan }, [lb, cb], 9),
    Player('Del Piero', italy, { juventus, padova }, [st, cm], 7),
    Player('Baggio', italy, { milan, inter, brescia, bologna, vicenca, fiorentina, juventus }, [cm, st], 8),
    Player('Gullit', netherlands, { milan, chelsea, sampdoria, psv, feyenoord }, [cm, rw], 8),
    Player('van Basten', netherlands, { milan, ajax }, [st], 9),
    Player('van Dijk', netherlands, { southampton, liverpool, celtic, groningen }, [cb], 9),
    Player('Buffon', italy, { juventus, parma, psg }, [gk], 9),
    Player('Hazard', belgium, { chelsea, lille, real_madrid }, [lw, cm, rw], 8),
    Player('Neuer', germany, { bayern, schalke }, [gk], 9),
    Player('Oblak', slovenia, { benfica, atletico_madrid }, [gk], 8),
    Player('Henry', france, { ny, barcelona, arsenal, juventus, monaco }, [st, lw], 9),
    Player('Sterling', england, { liverpool, man_c }, [lw, rw, st], 8),
    Player('Ronaldo', brazil, { milan, real_madrid, inter, barcelona, psv }, [st], 9),
    Player('Mané', senegal, { liverpool, southampton }, [lw, st, rw], 8),
    Player('Salah', egypt, { liverpool, chelsea, roma, fiorentina }, [lw, st, rw], 8),
    Player('Gerrard', england, { liverpool, la }, [cm], 9),
    Player('de Bruyne', belgium, { man_c, chelsea, bremen, wolfsburg }, [cm], 9),
    Player('Messi', argentina, { barcelona }, [st, rw], 10),
    Player('Alexander-Arnold', england, { liverpool }, [rb], 8),
    Player('Robertson', scotland, { liverpool }, [lb], 7),
    Player('Varane', france, { lens, real_madrid }, [cb], 8),
    Player('Zidane', france, { cannes, bordeaux, juventus, real_madrid }, [cm, lm], 10),
    Player('Cristiano Ronaldo', portugal, { man_u, sporting, real_madrid, juventus }, [lw, st, rw], 10),
    Player('Fabinho', brazil, { liverpool, monaco }, [cm], 7),
    Player('Cafu', brazil, { milan, roma }, [rb, rm], 9),
    Player('Roberto Carlos', brazil, { fenerbahce, real_madrid, inter }, [lb], 9),
    Player('Aubameyang', gabon, { saint_etienne, arsenal, dortmund, milan, monaco, lille }, [lw, st, rw], 7),
    Player('Lewandowski', poland, { bayern, dortmund }, [st], 8),
    Player('Mahrez', algeria, { leicester, man_c, le_havre }, [rw, rm, cm], 7),
    Player('Courtois', belgium, { chelsea, real_madrid, atletico_madrid }, [gk], 8),
    Player('Alisson', brazil, { liverpool, roma }, [gk], 8),
    Player('Haaland', norway, { salzburg, dortmund }, [st], 7),
    Player('Kanté', france, { leicester, chelsea, caen }, [cm], 8),
    Player('Vieira', france, { arsenal, man_c, inter, juventus, milan, cannes }, [cm], 8),
    Player('Xavi', spain, { barcelona }, [cm], 9),
    Player('David Silva', spain, { valencia, man_c, celta, eibar }, [cm, lm], 8),
    Player('Shearer', england, { newcastle, southampton, blackburn }, [st], 8),
    Player('Cech', czechia, { chelsea, arsenal, rennais }, [gk], 8),
    Player('Yaya', cote_d_ivoire, { man_c, barcelona, monaco, olympiacos }, [cm], 7),
    Player('Son', south_korea, { tottenham, leverkusen, hamburg }, [lw, rw, st], 6),
    Player('Boban', croatia, { milan, celta, bari }, [cm, lm], 7),
    Player('Suker', croatia, { munich_1860, west_ham, arsenal, real_madrid, sevilla }, [st], 7),
    Player('Vidic', serbia, { inter, man_u }, [cb], 8),
    Player('De Rossi', italy, { roma, boca }, [cm], 7),
    Player('Suarez', uruguay, { liverpool, barcelona, ajax, groningen }, [st], 8),
    Player('Valderrama', colombia, { colorado, tampa, miami, montpellier, valladolid }, [cm], 7),
    Player("Eto'o", cameroon, { sampdoria, everton, chelsea, inter, barcelona, real_madrid, mallorca }, [st, rw], 7),
    Player('Kewell', australia, { liverpool, leeds }, [cm, lw], 6),
    Player('Juninho Pernambucano', brazil, { ny, lyon }, [cm, rw], 6),
    Player('Mihajlovic', serbia, { lazio, inter, roma, sampdoria }, [cb], 7),
    Player('Keane', ireland, { man_u, celtic, nottingham }, [cm], 8),
    Player('Bale', wales, { tottenham, real_madrid, southampton }, [lw, st, rw], 7),
    Player('Alaba', austria, { hoffenheim, bayern }, [cm, cb, lb], 6),
    Player('Söyüncü', turkey, { leicester, freiburg }, [cb], 5),
    Player('Salas', chile, { juventus, lazio, river }, [st], 7),
    Player('Maradona', argentina, { napoli, boca, sevilla, barcelona }, [cm], 10)
]

team_433 = Team(players, [gk, lb, cb, cb, rb, cm, cm, cm, lw, st, rw])

xis = team_433.find_xis()
xis.sort(key = lambda xi: sum(player.quality for player in xi))

print('Top 3')
print()
for xi in xis[-3:]:
    print(sum(player.quality for player in xi))
    
    for player in xi:
        print(player)

    print()

print('Bottom 3')
print()
for xi in xis[:3]:
    print(sum(player.quality for player in xi))
    
    for player in xi:
        print(player)
    
    print()