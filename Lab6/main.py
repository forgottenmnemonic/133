from Name import character

player1 = character("Logar", 100, 20, "Orc")
player2 = character("Dungal", 11, 5, "Goblin")

player1.show_stats()
player1.level_up()
player2.show_stats()
#player2.set_HP(31)
player1.attack(player2)
player2.show_stats()
