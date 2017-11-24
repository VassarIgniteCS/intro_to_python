Activities
==========

Video Game Character Class (video_game_character_class_starter.py)
------------------------------------------------------------------
Define a bunch of classes that represent different characters in a video 
game. Give them attributes like name, color, strength, health, etc, and 
give it methods like sword_attack(), heal(num), take_damage(num), etc. 
Get creative and add more methods than that!
Examples:
>> player = Warrior(“Corin”, “silver”, 0, 100)
>> player.health
    100
>> player.sword_attack()
    “Corin used sword attack, doing 0 damage!”

Bank (bank_starter.py)
----------------------
Bank (bank_starter.py)
Re-implement the bank program we made earlier, but with objects!
Make a bank class, with an accounts attribute and a balances attribute 
(both lists)
Define the appropriate constructor (the constructor can have no 
parameters beyond self, depending on how you choose to code this!)
Define other methods to add accounts to the bank, check the balance of 
an account, and make a transfer between two accounts
Examples:
>> bank = Bank()
>> bank.add_account(“corin”, 100)
>> bank.add_account(“sufyan”, 100)
>> bank.check_balance(“corin”)
    100
>> bank.make_transfer(“corin”, “sufyan”, 10)
>> bank.check_balance(“corin”)
    90
>> bank.check_balance(“sufyan”)
    110

