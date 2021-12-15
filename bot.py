import discord
from discord.ext import commands
import random
from datetime import datetime
import sched, time

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents, help_command=None)

roasty = ('Jsi malá ubrečená píča, debile', 'Proč ztrácíš můj čas, plebe?', 'Nestojíš ani za roast.','Ty jsi tak těžký že ani pružinky z Lipra tě nezvednou (Generální partneři roastu jsou: Liper.)','Slabý kus')
forcePasty = ('Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. **Ironic.** He could save others from death, but not himself.' , 'The dark side of the Force is a pathway to many abilities some consider to be unnatural.', 'You wanna buy some deathsticks?')

championsNames = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","Aurelion Sol","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia","Cho'gath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan IV","Jax","Jayce","Jhin","Jinx","Kai'sa","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","Kha'zix","Kindred","Kled","Kog'maw","LeBlanc","Lee Sin","Leona","Lillia","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne","Nunu and Willump","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","Rek'sai","Rell","Renekton","Rengar","Riven","Rumble","Ryze","Samira","Sejuani","Senna","Seraphine","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Sylas","Syndra","Tahm Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Vel'koz","Vi","Viego","Viktor","Vladimir","Volibear","Warwick","Wukong","Xayah","Xerath","Xin Zhao","Yasuo","Yone","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]
championCosts = ["4800","3150","3150","1350","450","3150","450","6300","450","6300","4800","6300","3150","4800","4800","4800","6300","4800","1350","3150","4800","4800","450","4800","6300","4800","1350","3150","1350","4800","4800","3150","3150","450","4800","3150","4800","4800","3150","6300","4800","6300","1350","4800","1350","4800","6300","4800","6300","4800","3150","3150","3150","3150","450","6300","4800","4800","6300","6300","4800","3150","4800","4800","6300","4800","4800","4800","3150","1350","4800","4800","450","3150","1350","1350","4800","1350","4800","6300","3150","4800","450","3150","4800","6300","3150","450","6300","6300","4800","6300","1350","6300","6300","4800","4800","4800","4800","450","6300","4800","6300","6300","6300","3150","3150","3150","450","1350","450","4800","3150","450","4800","6300","4800","6300","6300","4800","1350","1350","4800","1350","3150","1350","1350","3150","1350","3150","4800","4800","1350","4800","4800","6300","4800","3150","3150","450","4800","6300","4800","1350","4800","6300","4800","6300","4800","4800","4800","1350","6300","4800"]


@client.event
async def on_ready():
    print('Bot is ready baby oh yes!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Eternal suffering and chronic depressoin .help"))
#@client.event
#async def on_member_join(member):
#    print(f"Gods of the afterlife, spare my arse, to which curse do I owe {member}'s presence?.")

#@client.event
#async def on_member_remove(member):
#    print(f"{member} odešel, good riddance.")   

@client.command()
async def roast(ctx, user: discord.Member):
    if user == '':
        i = random.randint(0, 4)
        roast = roasty[i]
        await ctx.send(roast)
    else:
        i = random.randint(0, 4)
        roast = roasty[i]
        await ctx.send(roast + user.mention)

@client.command()
async def insult(ctx, user:discord.Member, *, message=None):
    i = random.randint(0, 4)
    roast = roasty[i]
    message = roast;
    embed = discord.Embed(title=message);
    await user.send(embed=embed)

@client.command()
async def force(ctx):
    i = random.randint(0, 2)
    pasta = forcePasty[i]
    await ctx.send(pasta)

@client.command()
async def vasek(ctx, user: discord.Member):
    if user == '':
        await ctx.send('Ostříhej se :)')
    else:
        await ctx.send('Ostříhej se :)' + user.mention)

@client.command()
async def help(ctx):
    await ctx.send('```list všech příkazů \n .roast jméno(volitelné) | Dostaneš náhodný roast.    \n .vasek jmeno(volitelné) | Já fakt nevim proč jsem to přidal. \n .playlist | Pošle link na award winning playlist. \n .force | Pošle náhodnou Star Wars pastu. \n .pp jméno(volitelné) | Zjisti jak obdařen jsi ty, nebo někdo jiný. \n .doinb | DoinB copypasta z 2019 \n https://twitter.com/selfmade_LoL/status/1288949960298450944?s=20 \n .cas | Zobrazí čas u rudých sviní. \n .champ jmenoChampa | Napíše ti kolik stojí champ \n .had | Odhalí hada \n .amogus | Bacha na impostory *vtipné* \n .poggers | Fizi poggers```')

@client.command()
async def playlist(ctx):
    await ctx.send('https://youtu.be/9GUQUgmt1zg')

@client.command()
async def pp(ctx, user: discord.Member):
    i = random.randint(10, 250)
    i = i/10
    if i < 5:
        komentar = 'Tvoje pp dosahuje chabých rozměrů - '
    elif i < 10:
        komentar = 'Zklamání, něco jako Star Wars 8/9 - '
    elif i < 15:
        komentar = 'Mohlo by to být i horší - '
    elif i < 20:
        komentar = 'Gratuluji, ppgode - '
    elif i <= 25:
        komentar = 'Měl bys nosit jen dlouhé kalhoty - '
    komentar += str(i) + ' cm'
    if user == '':
        await ctx.send(komentar)
    else:
        await ctx.send(komentar + user.mention)
@client.command()
async def doinb(ctx):
    await ctx.send('DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN DOINB RYZE HACK？英雄联盟 400 CS 24 MIN')

@client.command()
async def cas(ctx):
    now = datetime.now()
    hours = now.hour + 7
    if(int(hours) >= 24):
        offset = hours - 24
        hours = 0
        hours += offset
    minutes = (now.minute)
    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)
    if minutes < 10:
        minutes = '0' + str(minutes)
    else:
        minutes = str(minutes)
    current_time =  hours + ':' + minutes 
    cas = 'Na Náměstí Nebeského klidu je nyní ' + current_time
    await ctx.send(cas)

@client.command()
async def champ(ctx, arg):
    if arg == '':
        await ctx.send('Zkus to znovu (.champ jmenoChampa)')
    else:
        arg = arg.lower()
        arg = arg.capitalize()
        print(arg)
        if arg in championsNames:
            if  arg in ["Kai'sa","Kog'maw", "Rek'sai", "Kha'zix", "Vel'koz", "Gho'gath"]:
                if arg == "Kai'sa":
                    arg = "Kai'Sa"
                elif arg == "Kog'maw":
                    arg = "Kog'Maw"
                elif arg == "Cho'gath":
                    arg = "Cho'Gath"
                elif arg == "Kha'Zix":
                    arg = "Vel'Koz"
                else:
                    arg ="Rek'Sai"
            await ctx.send('Champion ' + arg + ' stojí ' + str(championCosts[championsNames.index(arg)]) + ' BE')
        else:
            await ctx.send('Buď je dev debil a má špatně databási champů, nebo neumíš psát, vyber si.')

@client.command(pass_context = True)
async def amogus(ctx):
    await ctx.send('LMAO TY JSI IMPOSTOR :joy:' + ctx.message.author.mention)

@client.command()
async def had(ctx):
    sam = '<@401475658800300062>'
    await ctx.send(sam)

@client.command()
async def poggers(ctx):
    await ctx.send('https://youtu.be/TRsDgmNzo2w')

@client.command()
async def wtf(ctx):
    await ctx.send('https://imgur.com/gallery/JwrTxSl')


client.run('TOKEN');
