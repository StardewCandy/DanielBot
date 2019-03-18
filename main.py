import discord
import os
import random
import numpy as np
from keep_alive import keep_alive
cookies=1
b=1
c=b
awkwards=1
awkwards100=1
awkwards1000=1
headpats=1
hugs=1
cookies100=1
cookies1000=1
hugs100=1
hugs1000=1
client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name='Doing stuff, as usual!!'))

@client.event
async def on_message(message):
    if 'fortnite' in message.content:
        await client.send_message(message.channel, 'Don\'t. It\'s a fine game, but it\'s way overrated.')
@client.event
async def on_message(message):
    if message.content.startswith('dan!grookey'):
        await client.send_message(message.channel, 'Grookey is super cute, and it\'s shows the more "mellow" side of happiness compared to the energy exhibited by Scorbunny, and it looks really nice! I\'d pick it, but for now I\'m on Team Sobble until we see final evolutions.')
    if message.content.startswith('dan!scorbunny'):
        await client.send_message(message.channel, 'Scorbunny is really cute and I love its energetic personality and how upbeat and happy it always looks!')
    if message.content.startswith('dan!sobble'):
        await client.send_message(message.channel, 'It\'s *soooo* cute and *sooo* charming and I love it and I want one and it\'s so precious and adorable and it looks so happy to be here!')
    if message.content.startswith('dan!gen8'):
        await client.send_message(message.channel,'Sobble is *sooooo* cute! It\'s my favorite. It\'s like my spirit animal. Also, no one has commented on the new starters being Big Chungus and Harambe.')
    if message.content.startswith('dan!hug'):await client.send_message(message.channel, '*hugs back* Thank you!')
        global hugs
        global hugs100
        global hugs1000
        hugs += 1
        hugs100+=1
        hugs1000+=1
        await client.send_message(message.channel, "Thanks! You've upped my total hug count to " + str(hugs) + "!")
        if hugs100==100:
            await client.send_message(message.channel, "W-woah! 100 hugs! I'm so happy! *hugs back*")
            hugs100-=100
        if hugs1000==1000:
            await client.send_message(message.channel, "A t-thousand hugs? Really? Woah! T-thank you so much!")
            hugs1000-=1000
        if message.content.startswith('dan!headpat'):
            await client.send_message(message.channel, '*smiles* Thank you!')
        if message.content.startswith('dan!cookie'):
            await client.send_message(message.channel, '*eats cookie* Thank you for the cookie!')
            global cookies
            global cookies100
            global cookies1000
            cookies100=cookies100+1
            cookies=cookies +1
            cookies1000+=1
            await client.send_message(message.channel, "My total cookie count is "+ str(cookies)+"!")
            if cookies100==100:
                await client.send_message(message.channel, "W-woah! A hundred cookies?! That's at least a whole cookie jar worth of cookies!")
                cookies100-=100
            if cookies1000==1000:
                await client.send_message(message.channel, "W-wait, really? That makes... 1000 whole cookies?! T-that's a lot of cookies! That's enough to fill... 200 cookie jars!")
                cookies1000-=1000
            if message.content.startswith('dan!flirt'):
                global awkwards
                global awkwards100
                awkwards += 1
                await client.send_message(message.channel, '*blush* W-what? S-stop joking around!! People have tried to do that ' + str(awkwards) + " times.")
                awkwards100 +=1
                if awkwards100 == 100:
                    await client.send_message(message.channel, '*blushes profusely* Honestly, I-I\'m starting to think you guys are serious... You\'ve tried that 100 times now...')
                    awkwards100 -= 100
                if awkwards1000 == 1000:
                    await client.send_message(message.channel, "*blushes intensely* W-wait, r-really? Y-you've tried this 1000 times... *blushes more* A-are you r-really sure you want to?")
                if message.content.startswith('dan!erniegang'):
                    await client.send_message(message.channel, 'Ernie Gang.')
                if message.content.startswith('mhw!kirin'):
                    await client.send_message(message.channel, 'Kirin: Elder Dragon \n Weaknesses: Fire(Weakness Level 3), Water(Weakness Level 2), Ice(Weakness Level 2), Dragon(Weakness Level 1)\n Status Weaknesses: Sleep(Weakness Level 2), Blast(Weakness Level 2), Stun(Weakness Level 1), Poison(Weakness Level 1)\n Resistances: Thunder \n Status Resistances: Paralysis \n Elderseal Effect: Removes lightning armor effect, cancelling its defense buffs. \n Weak Points: Horn, Head \n \n Daniel\'s Solo Tip: Go with a Light Bowgun! It\'s my weapon of choice, and is perfect for soloing by allowing you to safely target the horn, using Pierce Ammo to get multiple hits, and staying far enough away to see its powerful yet choreographed attacks! Use plenty of Poison Ammo and give yourself Elemental Res Up, and use Farcasters when you need to. Don\'t be afraid to retreat. If it does regen, it\'s better than losing one of your continues! \n Daniel\'s Team Tip: While I normally recommend a strong attacker and an LBG user to distract them, due to Kirin not choosing a single target, it\'s best to have a team of 4 LBGs and Bows. Keep striking from a safe distance. It\'s good to keep some Recover Ammo on hand for everyone, as it allows healing without worrying about being slowed while you drink Potions and Mega Potions. Make sure to use Farcasters if you run out of Recover Ammo, and bring all but your highest HP party member with you. Just like Solo, use plenty of Poison Ammo and eat a meal that provides Elemental Res Up.')
                if message.content.startswith('mhw!nergigante'):
                    await client.send_message(message.channel, 'Nergigante: Elder Dragon \n Weaknesses: Thunder(Weakness Level 3), Dragon(Weakness Level 2), Fire(Weakness Level 1), Ice(Weakness Level 1), Water(Weakness Level 1) \n Status Weaknesses: Poison(Weakness Level 2), Blast(Weakness Level 2), Stun(Weakness Level 2), Sleep(Weakness Level 2), Paralysis(Weakness Level 2) \n Resistances: None \n Elderseal Effect: Removes the black spike, weakening its defense. \n Weak Points: Spikes, before they turn black. Head, Forelegs. \n \n Daniel\'s Solo Tips: Initiate the battle with an Insect Glaive and strike until you sever the tail. Most of its range relies on its tail, so getting it out of the way is a great idea. Make sure to dodge a lot. My personal recommendation for Insect Glaives is to use Jumping Advancing Slash after targeting the foe with your Kinsect. You\'ll be able to mount the monster multiple times in the battle, incapacitating it. I\'ll be recommending this strategy a lot! Once you\'ve severed the tail, use a Farcaster and switch to a Light Bowgun. Barrage it with status ammo! \n Daniel\'s Team Tip: Stick with a similar plan as the Solo, but have a LBG and IG seperately. Keep another IG user with you, and have a support LBG with plenty of Recover Ammo to keep the IG users safe!')
                if message.content.startswith('mhw!teostra'):
                    await client.send_message(message.channel,'Teostra: Elder Dragon \n Weaknesses: Water(Weakness Level 3), Ice(Weakness Level 3), Thunder(Weakness Level 1), Dragon(Weakness Level 1) \n Status Weaknesses: Poison(Weakness Level 2), Stun(Weakness Level 2), Sleep(Weakness Level 1), Blast(Weakness Level 1), Paralysis(Weakness Level 1) \n Resistances: Fire \n Elderseal Effect: Removes Supernova ability, drastically lowering its danger level. \n Weak Points: Face, Wings, Tail \n \n Daniel\'s Solo Tips: Initiate combat with Insect Glaive and a Sleep Kinsect. Put it to sleep, and cut off the tail while you can! It\'s a general rule of thumb that a shrunk hitbox makes a weakened monster. Then Farcaster away and switch to LBG. Fire away with Poison Ammo, and shoot Water Ammo/Ice Ammo for that Level 3 Weakness damage.\n Daniel\'s Team Tips: Start with a single IG to sever, one support LBG, 1 status LBG, and one DPS LBG. Put it to sleep/paralyze it and try to sever the tail. Then switch the IG to another support LBG. Continue protecting the DPS LBG, and attack the Teostra in openings between heals. This strategy encompasses Lunastra, too!')
                if message.content.startswith('mhw!xenojiiva'):
                    await client.send_message(message.channel,'Xeno\'Jiiva: Elder Dragon \n Weaknesses: All Elements(Weakness Level 2) \n Status Weaknesses: Poison(Weakness Level 3), Paraylsis(Weakness Level 1), Blast(Weakness Level 2), Stun(Weakness Level 1) \n Resistances: Sleep \n Elderseal Effect: Reduces duration of Rage Mode. \n Weak Points: Head, Foreclaws, Tail \n \n Daniel\'s Solo Tips: Go for the time-tested LBG and a new piece of your arsenal, the Fireproof Mantle. Xeno\'Jiiva heats up the ground by using its beam attack, so you\'ll need the mantle to avoid Burning. Stalactites above can be knocked down. Make sure to stay on the elevated platforms to avoid its melee attacks until it breaks the platform. Use as much Dragon Ammo as possible to inflict Elderseal and keep its Rage Mode from hurting you too much. \n Daniel\'s Team Tips: Start with one two DPS LBGs, one Support LBG, and on DPS IG. Support LBG keeps the group safe with Healing Ammo and Dragon Ammo, as the IG goes to attack the tail with a Poison Kinsect. The DPS LBGs start by attacking the foreclaws, then move on to the head. Use plenty of Pierce Ammo, as it\'s one of the best Ammo types. Eventually you\'ll whittle its health down enough to win, as you keep yourself alive with Ghillie/Temporal Mantles and Potions.')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(hidden)
