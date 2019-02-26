import discord
import os
import random
import numpy as np
from keep_alive import keep_alive
cookies=1
b=1
c=b
awkwards=1
headpats=1
hugs=1
client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name='Doing stuff, as usual!!'))


@client.event
async def on_message(message):
    if message.content.startswith('dan!hug'):
      await client.send_message(message.channel, '*hugs back* Thank you!')
      global hugs
      hugs += 1
      await client.send_message(message.channel, "Thanks! You've upped my total hug count to " + str(hugs) + "!")
    if message.content.startswith('dan!headpat'):
      await client.send_message(message.channel, '*smiles* Thank you!')
    if message.content.startswith('dan!cookie'):
      await client.send_message(message.channel, '*eats cookie* Thank you for the cookie!')
      global cookies
      cookies=cookies +1
      await client.send_message(message.channel, "My total cookie count is "+ str(cookies)+"!")
    if message.content.startswith('dan!flirt'):
      global awkwards
      await client.send_message(message.channel, '*blush* W-what? S-stop joking around!! People have tried to do that ' + str(awkwards) + " times.")
    if message.content.startswith('dan!erniegang'):
      await client.send_message(message.channel, 'Ernie Gang.')
    if message.content.startswith('mhw!kirin'):
      await client.send_message(message.channel, 'Kirin: Elder Dragon \n Weaknesses: Fire(Weakness Level 3), Water(Weakness Level 2), Ice(Weakness Level 2), Dragon(Weakness Level 1)\n Status Weaknesses: Sleep(Weakness Level 2), Blast(Weakness Level 2), Stun(Weakness Level 1), Poison(Weakness Level 1)\n Resistances: Thunder \n Status Resistances: Paralysis \n Elderseal Effect: Removes lightning armor effect, cancelling its defense buffs. \n Weak Points: Horn, Head \n \n Daniel\'s Solo Tip: Go with a Light Bowgun! It\'s my weapon of choice, and is perfect for soloing by allowing you to safely target the horn, using Pierce Ammo to get multiple hits, and staying far enough away to see its powerful yet choreographed attacks! Use plenty of Poison Ammo and give yourself Elemental Res Up, and use Farcasters when you need to. Don\'t be afraid to retreat. If it does regen, it\'s better than losing one of your continues! \n Daniel\'s Team Tip: While I normally recommend a strong attacker and an LBG user to distract them, due to Kirin not choosing a single target, it\'s best to have a team of 4 LBGs and Bows. Keep striking from a safe distance. It\'s good to keep some Recover Ammo on hand for everyone, as it allows healing without worrying about being slowed while you drink Potions and Mega Potions. Make sure to use Farcasters if you run out of Recover Ammo, and bring all but your highest HP party member with you. Just like Solo, use plenty of Poison Ammo and eat a meal that provides Elemental Res Up.')
    if message.content.startswith('mhw!nergigante'):
      await client.send_message(message.channel, 'Nergigante: Elder Dragon \n Weaknesses: Thunder(Weakness Level 3), Dragon(Weakness Level 2), Fire(Weakness Level 1), Ice(Weakness Level 1), Water(Weakness Level 1) \n Status Weaknesses: Poison(Weakness Level 2), Blast(Weakness Level 2), Stun(Weakness Level 2), Sleep(Weakness Level 2), Paralysis(Weakness Level 2) \n Resistances: None \n Elderseal Effect: Removes the black spike, weakening its defense. \n Weak Points: Spikes, before they turn black. Head, Forelegs. \n \n Daniel\'s Solo Tips: Initiate the battle with an Insect Glaive and strike until you sever the tail. Most of its range relies on its tail, so getting it out of the way is a great idea. Make sure to dodge a lot. My personal recommendation for Insect Glaives is to use Jumping Advancing Slash after targeting the foe with your Kinsect. You\'ll be able to mount the monster multiple times in the battle, incapacitating it. I\'ll be recommending this strategy a lot! Once you\'ve severed the tail, use a Farcaster and switch to a Light Bowgun. Barrage it with status ammo! \n Daniel\'s Team Tip: Stick with a similar plan as the Solo, but have a LBG and IG seperately. Keep another IG user with you, and have a support LBG with plenty of Recover Ammo to keep the IG users safe!')
    if message.content.startswith('mhw!teostra'):
      await client.send_message(message.channel,'Teostra: Elder Dragon \n Weaknesses: Water(Weakness Level 3), Ice(Weakness Level 3), Thunder(Weakness Level 1), Dragon(Weakness Level 1) \n Status Weaknesses: Poison(Weakness Level 2), Stun(Weakness Level 2), Sleep(Weakness Level 1), Blast(Weakness Level 1), Paralysis(Weakness Level 1) \n Resistances: Fire \n Elderseal Effect: Removes Supernova ability, drastically lowering its danger level. \n Weak Points: Face, Wings, Tail \n \n Daniel\'s Solo Tips: Initiate combat with Insect Glaive and a Sleep Kinsect. Put it to sleep, and cut off the tail while you can! It\'s a general rule of thumb that a shrunk hitbox makes a weakened monster. Then Farcaster away and switch to LBG. Fire away with Poison Ammo, and shoot Water Ammo/Ice Ammo for that Level 3 Weakness damage.\n Daniel\'s Team Tips: Start with a single IG to sever, one support LBG, 1 status LBG, and one DPS LBG. Put it to sleep/paralyze it and try to sever the tail. Then switch the IG to another support LBG. Continue protecting the DPS LBG, and attack the Teostra in openings between heals. This strategy encompasses Lunastra, too!')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
