class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack
        
    def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
    __repr__=__str__


def declare_winner(fighter1, fighter2, first_attacker):

    while fighter1.health and fighter2.health > 0:

            if first_attacker == fighter1.name:
                if fighter1.health > 0:
                    fighter2.health -= fighter1.damage_per_attack
                else:
                    break

                if fighter2.health > 0:
                    fighter1.health -= fighter2.damage_per_attack
                else:
                    break

            else:
                if fighter2.health > 0:
                    fighter1.health -= fighter2.damage_per_attack
                else:
                    break

                if fighter1.health > 0:
                    fighter2.health -= fighter1.damage_per_attack
                else:
                    break



    if fighter1.health > fighter2.health:
        return fighter1.name
    else:
        return fighter2.name



print(f'{declare_winner(Fighter("Lew", 10, 2),Fighter("Harry", 5, 4), "Lew")=}')
