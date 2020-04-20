def center_print(s, width):
    ls = len(s)
    diff = width - ls

    if diff < 0:
        return s[:width]

    left = diff // 2 + diff % 2
    right = diff // 2

    return ' ' * left + s + ' ' * right 

class Player:
    def __init__(self, name, nationality, clubs, positions, quality):
        self.name = name
        self.nationality = nationality
        self.clubs = clubs
        self.positions = positions
        self.quality = quality

    def __repr__(self):
        return self.name


class Xi:
    position_width = 18    

    def __init__(self, positions, players):
        self.positions = positions
        self.players = players

    def find_position_index(self, position_name, count=1):
        matches = 0

        for i, position in enumerate(self.positions):
            if position == position_name:
                matches += 1
                if matches == count:
                    return i

        return -1

    def print_attack(self):
        lw_pos = self.find_position_index('lw')

        if lw_pos >= 0:
            rw_pos = self.find_position_index('rw')
            st_pos = self.find_position_index('st')

            return ''.join((
                center_print(self.players[lw_pos].name, self.position_width),
                ' ' * self.position_width,
                center_print(self.players[st_pos].name, self.position_width),
                ' ' * self.position_width,
                center_print(self.players[rw_pos].name, self.position_width)
            ))

        striker_a_pos = self.find_position_index('st', 1)
        striker_b_pos = self.find_position_index('st', 2)

        if striker_b_pos >= 0:
            return ''.join((                
                ' ' * self.position_width,
                center_print(self.players[striker_a_pos].name, self.position_width),
                ' ' * self.position_width,
                center_print(self.players[striker_b_pos].name, self.position_width),
                ' ' * self.position_width
            ))

        return ''.join((                
            ' ' * self.position_width,
            ' ' * self.position_width,
            center_print(self.players[striker_a_pos].name, self.position_width),
            ' ' * self.position_width,            
            ' ' * self.position_width
        ))

            
    def print_midfield(self):
        lm_pos = self.find_position_index('lm')
        rm_pos = self.find_position_index('rm')
        cm_a_pos = self.find_position_index('cm', 1)
        cm_b_pos = self.find_position_index('cm', 2)
        cm_c_pos = self.find_position_index('cm', 3)

        if lm_pos >= 0:
            if cm_c_pos >= 0:
                return ''.join((                
                    center_print(self.players[lm_pos].name, self.position_width),
                    center_print(self.players[cm_a_pos].name, self.position_width),
                    center_print(self.players[cm_b_pos].name, self.position_width),
                    center_print(self.players[cm_c_pos].name, self.position_width),
                    center_print(self.players[rm_pos].name, self.position_width)
                ))
            
            return ''.join((                
                center_print(self.players[lm_pos].name, self.position_width),
                center_print(self.players[cm_a_pos].name, self.position_width),
                ' ' * self.position_width,
                center_print(self.players[cm_b_pos].name, self.position_width),
                center_print(self.players[rm_pos].name, self.position_width)
            ))

        return ''.join((                
            ' ' * self.position_width,
            center_print(self.players[cm_a_pos].name, self.position_width),
            center_print(self.players[cm_b_pos].name, self.position_width),
            center_print(self.players[cm_c_pos].name, self.position_width),
            ' ' * self.position_width
        ))
        

    def print_defense(self):
        lb_pos = self.find_position_index('lb')
        rb_pos = self.find_position_index('rb')
        cb_a_pos = self.find_position_index('cb', 1)
        cb_b_pos = self.find_position_index('cb', 2)
        cb_c_pos = self.find_position_index('cb', 3)

        if lb_pos >= 0:
            if cb_c_pos >= 0:
                return ''.join((                
                    center_print(self.players[lb_pos].name, self.position_width),
                    center_print(self.players[cb_a_pos].name, self.position_width),
                    center_print(self.players[cb_b_pos].name, self.position_width),
                    center_print(self.players[cb_c_pos].name, self.position_width),
                    center_print(self.players[rb_pos].name, self.position_width)
                ))
            
            return ''.join((                
                center_print(self.players[lb_pos].name, self.position_width),
                center_print(self.players[cb_a_pos].name, self.position_width),
                ' ' * self.position_width,
                center_print(self.players[cb_b_pos].name, self.position_width),
                center_print(self.players[rb_pos].name, self.position_width)
            ))

        return ''.join((                
            ' ' * self.position_width,
            center_print(self.players[cb_a_pos].name, self.position_width),
            center_print(self.players[cb_b_pos].name, self.position_width),
            center_print(self.players[cb_c_pos].name, self.position_width),
            ' ' * self.position_width
        ))

    def print_gk(self):
        gk_pos = self.find_position_index('gk')

        return ''.join((                
            ' ' * self.position_width,
            ' ' * self.position_width,
            center_print(self.players[gk_pos].name, self.position_width),
            ' ' * self.position_width,
            ' ' * self.position_width
        ))
        
    def __repr__(self):
        return '\n'.join((self.print_attack(), self.print_midfield(), self.print_defense(), self.print_gk()))

class Team:
    def __init__(self, formation, players, positions):
        self.formation = formation
        self.players = players
        self.positions = positions
        self.xis = []
        self.xi_name_sets = set()
        self.best_at_5 = 0

    def generate_xis(self):
        players_for_positions = list(map(
            lambda position: [player for player in self.players if position in player.positions],
            self.positions
            ))        

        def search(n, players, nations, clubs):
            if n == 11:
                player_names = tuple(sorted([player.name for player in players]))
                if player_names not in self.xi_name_sets:
                    self.xi_name_sets.add(player_names)
                    self.xis.append(Xi(self.positions, list(players)))
                return

            if n == 5:
                score = sum(player.quality for player in players)
                
                if score > self.best_at_5:
                    self.best_at_5 = score

                if score + 4 < self.best_at_5:
                    return

            for player in players_for_positions[n]:
                if player.nationality not in nations and not player.clubs & clubs:
                    search( n +1, list(players) + [player], nations | { player.nationality }, clubs | player.clubs)

        search(0, [], set(), set())


def parse_positions(positionstring):
    return positionstring[1:-1].split(',')
    

def parse_clubs(clubstring):
    clubs = set()

    for s in clubstring[1:-1].split(','):
        clubs.add(s.replace('_', ' '))

    return clubs


def get_players():
    players = []

    with open('players.txt', encoding='utf-8') as f:
        for line in f.readlines():
            name, nation, clubs, positions, quality = line.split()
            clubset = parse_clubs(clubs)
            positionlist = parse_positions(positions)
            players.append(Player(name.replace('_', ' '), nation.replace('_', ' '), clubset, positionlist, int(quality)))

    return players

if __name__ == '__main__':
    players = get_players()

    teams = [
        Team('4-3-3', players, ['gk', 'lb', 'cb', 'cb', 'rb', 'cm', 'cm', 'cm', 'lw', 'st', 'rw']),
        Team('4-4-2', players, ['gk', 'lb', 'cb', 'cb', 'rb', 'lm', 'cm', 'cm', 'rm', 'st', 'st']),
        Team('3-4-3', players, ['gk', 'cb', 'cb', 'cb', 'lm', 'cm', 'cm', 'rm', 'lw', 'st', 'rw']),
        Team('3-5-2', players, ['gk', 'cb', 'cb', 'cb', 'lm', 'cm', 'cm', 'cm', 'rm', 'st', 'st']),
        Team('4-5-1', players, ['gk', 'lb', 'cb', 'cb', 'rb', 'lm', 'cm', 'cm', 'cm', 'rm', 'st']),
    ]

    for team in teams:
        print()
        print()
        team.generate_xis()
        team.xis.sort(key = lambda xi: sum(player.quality for player in xi.players))

        print('Top 3 for', team.formation)
        print()
        for xi in team.xis[-1:-4:-1]:
            print('Team strength:', sum(player.quality for player in xi.players))
            print()
            print(xi)
            print()