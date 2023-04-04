from nextcord.ext import commands
from nextcord import Embed 
import random, asyncio, time
import os

bot = commands.Bot(command_prefix="!")
bot.remove_command("help")


@bot.command(name="help")
async def Help(ctx):
    embed=Embed(color=0x0080ff, title="Game Commands")
    embed.add_field(name="!help", value="Opens help embed.", inline=False)
    embed.add_field(name="!hangman", value="A game for two in which one player tries to guess the letters of a word, the other player recording failed attempts by drawing a gallows and someone hanging on it, line by line.", inline=False)
    embed.add_field(name="!blackjack", value="A card game that is monstly played in casinos. WARNING, this is a form of gambling and might not be suited for younger people. Please play at own risk", inline=False)
    embed.add_field(name="!equasion", value="Generates a random equasion for you to solve.", inline=False)
    embed.add_field(name="!rps", value="At the same time, two players display one of three symbols: a rock, paper, or scissors.", inline=False)
    embed.add_field(name="!simonsays", value="Give out the correct color (by emoji) to please simon!", inline=False)
    await ctx.send(embed=embed)


@bot.command(name="hangman")
async def SendMessage(ctx):
    lives = 9
    words = ['power', 'funny', 'apple', 'pizza', 'shirt', 'grass', 'plain','latte','paint','black','kitty','zebra','pasta','rusty','furry','sloth','fruit','candy','plato','wheel','poker']
    hidden_word = random.choice(words)
    hint = list('?????')
    heart_symbol = ':heart:'
    correct_guessed_word = False
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    def update_hint(guessed_letter, hidden_word, hint):
        index = 0
        while index < len(hidden_word):
            if guessed_letter == hidden_word[index]:
                hint[index] = guessed_letter
            index = index + 1
    

    while lives > 0:
        await ctx.send(hint)
        await ctx.send('Lives left: ' + heart_symbol * lives)
        try:
            msg = await bot.wait_for("message",timeout=60, check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond! :frowning:")
            return
        
        if msg.content == letters[0]:
            guess = 'a'
        elif msg.content == letters[1]:
            guess = 'b'
        elif msg.content == letters[2]:
            guess = 'c'
        elif msg.content == letters[3]:
            guess = 'd'
        elif msg.content == letters[4]:
            guess = 'e'
        elif msg.content == letters[5]:
            guess = 'f'
        elif msg.content == letters[6]:
            guess = 'g'
        elif msg.content == letters[7]:
            guess = 'h'
        elif msg.content == letters[8]:
            guess = 'i'
        elif msg.content == letters[9]:
            guess = 'j'
        elif msg.content == letters[10]:
            guess = 'k'
        elif msg.content == letters[11]:
            guess = 'l'
        elif msg.content == letters[12]:
            guess = 'm'
        elif msg.content == letters[13]:
            guess = 'n'
        elif msg.content == letters[14]:
            guess = 'o'
        elif msg.content == letters[15]:
            guess = 'p'
        elif msg.content == letters[16]:
            guess = 'q'
        elif msg.content == letters[17]:
            guess = 'r'
        elif msg.content == letters[18]:
            guess = 's'
        elif msg.content == letters[19]:
            guess = 't'
        elif msg.content == letters[20]:
            guess = 'u'
        elif msg.content == letters[21]:
            guess = 'v'
        elif msg.content == letters[22]:
            guess = 'w'
        elif msg.content == letters[23]:
            guess = 'x'
        elif msg.content == letters[24]:
            guess = 'y'
        elif msg.content == letters[25]:
            guess = 'z'
        elif msg.content == words[0]:
            guess = 'power'
        elif msg.content == words[1]:
            guess = 'funny'
        elif msg.content == words[2]:
            guess = 'apple'
        elif msg.content == words[3]:
            guess = 'pizza'
        elif msg.content == words[4]:
            guess = 'shirt'
        elif msg.content == words[5]:
            guess = 'grass'
        elif msg.content == words[6]:
            guess = 'plain'
        elif msg.content == words[7]:
            guess = 'latte'
        elif msg.content == words[8]:
            guess = 'paint'
        elif msg.content == words[9]:
            guess = 'black'
        elif msg.content == words[10]:
            guess = 'kitty'
        elif msg.content == words[11]:
            guess = 'zebra'
        elif msg.content == words[12]:
            guess = 'pasta'
        elif msg.content == words[13]:
            guess = 'rusty'
        elif msg.content == words[14]:
            guess = 'furry'
        elif msg.content == words[15]:
            guess = 'sloth'
        elif msg.content == words[16]:
            guess = 'fruit'
        elif msg.content == words[17]:
            guess = 'candy'
        elif msg.content == words[18]:
            guess = 'plato'
        elif msg.content == words[19]:
            guess = 'wheel'
        elif msg.content == words[20]:
            guess = 'poker'
        else:
            guess = ''


        if guess == hidden_word:
            correct_guessed_word = True
            break

        if guess in hidden_word:
            update_hint(guess, hidden_word, hint)
        else:
            await ctx.send('Wrong, You just lost a life!')
            lives = lives -1
    
    if correct_guessed_word:
        await ctx.send('Wow! You won! Your word was ' + hidden_word)
    else:
        await ctx.send('Welp... You lost. Your word was ' + hidden_word)
   


@bot.command(name="blackjack")
async def sendMessage(ctx):
    player_In = True
    dealer_In = True

    deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
            ':spades:',':clubs:',':hearts:',':diamonds:',':spades:',':clubs:',':hearts:',':diamonds:',':spades:',':clubs:',':hearts:',':diamonds:',':spades:',':clubs:',':hearts:',':diamonds:']
    player_hand = []
    dealers_hand = []

    def deal_card(turn):
        card = random.choice(deck)
        turn.append(card)
        deck.remove(card)

    def total(turn):
        total = 0
        face = [':spades:',':clubs:',':hearts:']
        for card in turn:
            if card in range(1,11):
                total += card
            elif card in face:
                total += 10
            else:
                if total > 11:
                    total += 1
                else:
                    total += 11
        return total

    def reveal_dealer_hand():
        if len(dealers_hand) == 2:
            return dealers_hand[0]
        elif len(dealers_hand) > 0:
            return dealers_hand[0], dealers_hand[1]

    for _ in range(2):
        deal_card(dealers_hand)
        deal_card(player_hand)

    while player_In or dealer_In:
        await ctx.send(f"Dealer had {reveal_dealer_hand()} and X")
        await ctx.send(f"You have {player_hand} for a total of {total(player_hand)}")
        await ctx.send("Type 1 to Stay, Type 2 to Hit")
        if player_In:
            try:
                msg = await bot.wait_for("message",timeout=60, check=lambda message: message.author == ctx.author)
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond! :frowning:")
                return
            
            if msg.content == "1":
                stay_or_hit = 1        
            elif msg.content == "2":
                stay_or_hit = 2
            else:
                stay_or_hit = ''

        
        if total(dealers_hand) > 16:
            dealer_In = False
        else:
            deal_card(dealers_hand)
        if stay_or_hit == '1':
            player_In = False
        else:
            deal_card(player_hand)
        if total(player_hand) >= 21:
            break
        elif total(dealers_hand) >= 21:
            break

    if total(player_hand) == 21:
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("Blackjack! You just won!")
    elif total(dealers_hand) == 21:
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("Blackjack! The dealer won!")
    elif total(player_hand) > 21:
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("You bust! Dealer wins!")
    elif total(dealers_hand) > 21:
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("Dealer bust! You won!")
    elif 21 - total(dealers_hand) < 21 - total(player_hand):
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("Dealer wins!")
    elif 21 - total(dealers_hand) > 21 - total(player_hand):
        await ctx.send(f"\nYou have {player_hand} for a total of 21 and the dealer has {dealers_hand} for a total of {total(dealers_hand)}")
        await ctx.send("You win!")
    
@bot.command(name="equasion")
async def sendMessage(ctx):
    first_number = random.randint(0,19)
    second_number = random.randint(0,19)

    operators = ['+','-','*','/']
    random_operator = operators[random.randint(0,3)]
    equasion = first_number, random_operator, second_number

    await ctx.send(equasion)

        
    if random_operator == '+':
        awnser = first_number + second_number
    if random_operator == '-':
        awnser = first_number - second_number
    if random_operator == '*':
        awnser = first_number * second_number
    if random_operator == '/':
        awnser = first_number / second_number

    try:
        msg = await bot.wait_for("message",timeout=60, check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! :frowning:")
        return
    
    if msg.content == awnser:
        await ctx.send(f"The awnser is: {awnser}")
    else:
        await ctx.send(f"The awnser is: {awnser}")


@bot.command(name="rps")
async def rock_paper_scissors(ctx):
    win = False
    await ctx.send("Choose for either :rock: (type rock), :clipboard: (type paper) or :scissors: (type scissors)\n")
    try:
        msg = await bot.wait_for("message",timeout=60, check=lambda message: message.author == ctx.author)
    except asyncio.TimeoutError:
        await ctx.send("You took too long to respond! :frowning:")
        return
    
    if msg.content == "rock":
        user = 'r'
        await ctx.send("You chose :rock:")
    elif msg.content == "paper":
        user = 'p'
        await ctx.send("You chose :clipboard:")
    else:
        user = 's'
        await ctx.send("You chose :scissors:")
    
    computer = random.choice(['r', 'p', 's'])
    if computer == 'r':
        await ctx.send("Computer chose :rock:")
    elif computer == 'p':
        await ctx.send("Computer chose :clipboard:")
    else:
        await ctx.send("Computer chose :scissors:")

    if user == computer:
        await ctx.send('It\'s a tie')
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p') and (computer == 'r'):
            win = True
    else:
        win = False

    
    if win:
        await ctx.send('You won!')
    else:
        await ctx.send('You lost!')
        

@bot.command(name="simonsays")
async def simonsays(ctx):
    await ctx.send("Remember! The colores squares go as followed: \n"
                    ":red_square: (awnser with R) \n"
                    ":green_square: (awnser with G) \n"
                    ":blue_square: (awnser with B) \n"
                    ":orange_square: (awnser with O) \n"
                    ":yellow_square: (awnser with Y) \n"
                    ":purple_square: (awnser with P)")
    
    colors = "RGBOYP"
    simon = ""

    for score in range(0,10):
        simon += random.choice(colors)
        for color in simon:
            if color == "R":
                await ctx.send(":red_square:")
            if color == "G":
                await ctx.send(":green_square:")
            if color == "B":
                await ctx.send(":blue_square:")
            if color == "O":
                await ctx.send(":orange_square:")
            if color == "Y":
                await ctx.send(":yellow_square:")
            if color == "P":
                await ctx.send(":purple_square:")
        try:
            msg = await bot.wait_for("message",timeout=120, check=lambda message: message.author == ctx.author)
        except asyncio.TimeoutError:
            await ctx.send("You took too long to respond! :frowning:")
        if msg.content != simon:
            break
        else:
            await ctx.send(":white_check_mark:")
    
    await ctx.send(":negative_squared_cross_mark:")
    await ctx.send(f"Your final score was {score}")





@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("MTA4OTg4Mzk0NDM4MTU4MzM3MA.GKK84u.McQPS8N2VzUpbHLDsQfLWHbRUMOidjyj0cGst0")