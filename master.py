import discord
import random
from discord.ext import commands

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print('IT-O is online!')

@bot.command()
async def funfact(ctx):
    responses = ['"Ewok" was never spoken in the original trilogy.',
                'Yoda has no determined species.',
                'Qui-Gon Jinn used a Gillette razor for his communicator.',
                'Ewoks speak Tibetan.',
                'Mandalorians started out as the Taung Species, a species indigenous to Coruscant.',
                'Lightsabers and the Death Star are both powered by Kyber crystals.',
                'Salicious B. Crumb is a Kowakian monkey-lizard.',
                'Darth Bane was so skilled with a lightsaber that he could deflect raindrops during a downpour and not get wet.',
                'Admiral Ackbar practiced martial arts every day and once destroyed a battle droid by head butting it',
                'Nien Nunb speaks fluent kikuyu, a real Kenyan language.',
                'Ewan McGregor brother was an RAF pilot, and his callsign was "Obi Two".',
                'There are almost no visible clothing fasteners (buttons/zippers/etc) in any of the Star Wars movies.',
                'The Rebel Base on Yavin was a Sith temple.',
                'The Sith Temple on Yavin was built by Naga Sadow during the Great Hyperspace War.'
                'iPhones know to capitalize Jedi, but think "Sith" is the word sigh misspelled.',
                'One of the asteroids in the asteroid chase in Empire Strikes Back is a potato.',
                'Ewan McGregor had to be muted at some points in the movie because he made the light saber noise.',
                'The type of music that is played in cantinas is called Jizz.',
                'Max Rebo is an accomploshed and well known Jizz musician.',
                'Luke original last name was Starkiller.',
                'T.I.E stands for Twin Ion Engine.',
                'Blasters shoot blaster bolts, not lasers.'
                'Blasters work by exciting a substance known as tibanna gas which then releases a supercharged plasma.',
                'Tibanna gas is harvested from places like Bespin, the planet where Cloud City is located.',
                'The little blue elephant man in Jabba Palace is named Max Rebo. The band that he plays with is also called The Max Rebo Band.',
                'Galactic Basic is the most spoken language in the galaxy, Huttese is the second most spoken.',
                'The Twilek have a language called Twileki - a language based on verbal sounds combined with lekku sign language.',
                ' Jedi Lightsabers used colors determined by force/kyber crystals to indicate their role within the Jedi Order.',
                'In the interrogation scene in KotOR, you can say the location of the Jedi temple is on Alderaan, when it is actually on Dantoonie.',
                'MOFF is a shortening of Military Official',
                'Taun tauns smell worse on the inside.',
                'Thrawn is short for Mitth raw nuruodo because humans have problems pronouncing it.',
                'The chess-like game aboard the Millennium Falcon is called Dejarik',
                'Wookiees speak Shyriiwook.',
                ]
    await ctx.send(f'{random.choice(responses)}')

bot.run('TOKEN')
