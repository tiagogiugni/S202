from pprintpp import pprint as pp
from db.database import Graph

class FootballDAO:
    def __init__(self):
        self.db = Graph(uri='bolt://3.236.155.50:7687', user='neo4j', password='galley-present-coxswains')

    def create_player(self, player):
        return self.db.execute_query('CREATE (n:Player {name:$name, age:$age, health:$health}) RETURN n', player)

    def create_team(self, team):
        return self.db.execute_query('CREATE (n:Team {name:$name, coach:$coach, wins:$wins}) RETURN n', team)

    def read_player_by_name(self, name):
        return self.db.execute_query('MATCH (n:Player {name:$name}) RETURN n', {'name': name})

    def read_team_by_name(self, name):
        return self.db.execute_query('MATCH (n:Team {name:$name}) RETURN n', {'name': name})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_health(self, player):
        return self.db.execute_query('MATCH (n:Player {name:$name}) SET n.health = $health RETURN n', player)

    def update_wins(self, team):
        return self.db.execute_query('MATCH (n:Team {name:$name}) SET n.wins = $wins RETURN n', team)

    def delete_player(self, name):
        return self.db.execute_query('MATCH (n:Player {name:$name}) DELETE n', {'name': name})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, player, team, year):
        return self.db.execute_query(
            'MATCH (n:Player {name:$player_name}), (m:Team {name:$team_name}) CREATE (n)-[r:PLAYS_FOR {year: $year}]->(m) RETURN n, r, m',
            {'player_name': player, 'team_name': team, 'year': year})

    def read_relation(self, player, team):
        return self.db.execute_query('MATCH (n:Player {name:$player_name})-[r]->(m:Team {name:$team_name}) RETURN n, r, m',
                                     {'player_name': player, 'team_name': team})

def divider():
    print('\n' + '-' * 80 + '\n')

def print_menu():
    print("\n" + "="*40)
    print("  Football Management System")
    print("="*40)
    print("1. Create a player")
    print("2. Create a team")
    print("3. Read everything")
    print("4. Update player health")
    print("5. Update team wins")
    print("6. Delete a player")
    print("7. Delete everything")
    print("8. Create player-team relation")
    print("9. Read player-team relation")
    print("0. Exit")
    print("="*40)

dao = FootballDAO()

while True:    
    print_menu()
    option = input('Select an option: ')

    if option == '1':
        name = input('  Name: ')
        age = input('  Age: ')
        health = input('  Health: ')
        player = {'name': name, 'age': age, 'health': health}
        dao.create_player(player)
        print("Player created successfully!")
        divider()

    elif option == '2':
        name = input('  Name: ')
        coach = input('  Coach: ')
        wins = input('  Wins: ')
        team = {'name': name, 'coach': coach, 'wins': wins}
        dao.create_team(team)
        print("Team created successfully!")
        divider()

    elif option == '3':
        nodes = dao.read_all_nodes()
        pp(nodes)
        divider()

    elif option == '4':
        name = input('  Name: ')
        health = input('  Health: ')
        player = {'name': name, 'health': health}
        dao.update_health(player)
        print("Player health updated successfully!")
        divider()

    elif option == '5':
        name = input('  Name: ')
        wins = input('  Wins: ')
        team = {'name': name, 'wins': wins}
        dao.update_wins(team)
        print("Team wins updated successfully!")
        divider()

    elif option == '6':
        name = input('  Name: ')
        dao.delete_player(name)
        print("Player deleted successfully!")
        divider()

    elif option == '7':
        dao.delete_all_nodes()
        print("All nodes deleted successfully!")
        divider()

    elif option == '8':
        player_name = input('  Player Name: ')
        team_name = input('  Team Name: ')
        year = input('  Year: ')
        dao.create_relation(player_name, team_name, year)
        print("Relation created successfully!")
        divider()

    elif option == '9':
        player_name = input('  Player Name: ')
        team_name = input('  Team Name: ')
        relation = dao.read_relation(player_name, team_name)
        pp(relation)
        divider()

    elif option == '0':
        print("Exiting the system...")
        break

    else:
        print("Invalid option! Please try again.")
        divider()

dao.db.close()
