"""
4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр
- armor = 1.2 (величина брони персонажа). Теперь надо добавить новую функцию, которая будет вычислять
и возвращать полученный урон по формуле damage / armor
Следовательно, у вас должно быть 2 функции: Наносит урон.
Это улучшенная версия функции из задачи 3. Вычисляет урон по отношению к броне.

Примечание. Функция номер 2 используется внутри функции номер 1
для вычисления урона и вычитания его из здоровья персонажа.

===================================================================

nb! По отношению к исходным условиям задачи внесены следующие изменения:

 1. изменена формула расчёта брони:
    значение защиты по умолчанию = 1 (нет брони)
    значение armor = % увеличения защиты

 2. добавлено оружие (weapon), и сила оружия (weapon_power), увеличивающая урон на хх%
    как следствие, изменена формула расчёта урона (get_damage())

 3. добавлена проверка остатка жизни защищающегося; не может быть отрицательной.

 4. на труп (жизнь = 0) нельзя напасть

 тестовый сценарий в функции main()

"""


def attack_and_print_health(attacker, defender):
    print(attack(attacker, defender))
    print(get_person_health(attacker))
    print(get_person_health(defender))
    print()


def attack(attacker, defender):
    if defender['health'] <= 0:
        info = f"<!> Can`t attack: {defender['name']}`s health is over!"
    else:
        damage = get_damage(attacker, defender)
        info = f"{attacker['name']} hits {defender['name']} with {attacker['weapon']}. {damage:.2f} points damage."
        if defender['health'] > damage:
            defender['health'] -= damage
        else:
            defender['health'] = 0
            info += f" {defender['name']} is defeated!"
    return info


def get_damage(attacker, defender):
    damage = (attacker['damage'] * (1 + attacker['weapon_power'] / 100)) / (1 + defender['armor'] / 100)
    return damage


def print_start_info(*persons):
    for person in persons:
        print(get_person_info(person))
    print()


def get_person_info(person):
    info = f"{person['name']}:\
        \n\t damage = {person['damage']}\
        \n\t health = {person['health']}\
        \n\t armor = {person['armor']}\
        \n\t weapon = {person['weapon']}\
        \n\t weapon power = {person['weapon_power']}"
    return info


def get_person_health(person):
    info = f"{person['name']}`s health = {person['health']:.2f}"
    return info


def create_person(name, health=75, damage=25, armor=0, weapon='hands', weapon_power=0):
    person = {
        'name': name,
        'health': health,
        'damage': damage,
        'armor': armor,
        'weapon': weapon,
        'weapon_power': weapon_power
    }
    return person


def main():
    print('test check with armor & weapon...\n')

    player = create_person('default_Player')
    enemy = create_person('default_Enemy')
    strong_player = create_person('strong_Player', health=150, damage=25, armor=100, weapon='an axe', weapon_power=200)

    print_start_info(player, enemy, strong_player)

    attack_and_print_health(attacker=enemy, defender=player)
    attack_and_print_health(attacker=player, defender=enemy)
    attack_and_print_health(attacker=enemy, defender=player)
    attack_and_print_health(attacker=enemy, defender=player)
    attack_and_print_health(attacker=enemy, defender=player)

    attack_and_print_health(attacker=enemy, defender=strong_player)
    attack_and_print_health(attacker=enemy, defender=strong_player)
    attack_and_print_health(attacker=enemy, defender=strong_player)
    attack_and_print_health(attacker=enemy, defender=strong_player)

    attack_and_print_health(attacker=strong_player, defender=enemy)


if __name__ == '__main__':
    main()
