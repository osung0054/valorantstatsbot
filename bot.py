import discord
from discord.ext import commands

TOKEN = "NzQzMTM4NTg0MTg5NDY4Njg1.XzQTvQ.B1jPxA6CDVnAOyVg7eIvkDkjyQw"

client = discord.Client()
client = commands.Bot(command_prefix='/v')

import requests
from bs4 import BeautifulSoup

@client.event
async def on_ready():
    print(f'{client.user} online!')


@client.event
async def on_message(message):
    # 봇이 입력한 메시지라면 무시하고 넘어간다.
    if message.author == client.user:
        return

    #Help
    if message.content == '/v help':
        embed = discord.Embed(title='Valorant Stats Bot.', description='by osung0054#6765', color=0xFF2424)
        embed.add_field(name = "1. '/v ID#TAG'", value = 'Print your current season stats.', inline = False)
        embed.add_field(name = "2. '/v ID#TAG SEASON'", value = 'Print your selected season stats.\navailable seasons : \n**S1Act1**\n**S1Act2**\n**S1Act3**\n', inline = False)
        await message.channel.send(embed=embed)

    #Main
    elif '/v' in message.content:
        try:
            id = message.content.replace('/v ', '').split('#')[0]
            tag = message.content.split('#')[1]

            if 'S1Act1' in message.content:
                tag = message.content.split('#')[1].replace(' S1Act1', '').strip()
                url = 'https://dak.gg/valorant/profile/'+id+'-'+tag+'/overview/s1/act1?hl=en-US'
            elif 'S1Act2' in message.content:
                tag = message.content.split('#')[1].replace(' S1Act2', '').strip()
                url = 'https://dak.gg/valorant/profile/'+id+'-'+tag+'/overview/s1/act2?hl=en-US'
            elif 'S1Act3' in message.content:
                tag = message.content.split('#')[1].replace(' S1Act3', '').strip()
                url = 'https://dak.gg/valorant/profile/'+id+'-'+tag+'/overview/s1/act3?hl=en-US'
            else:
                url = 'https://dak.gg/valorant/profile/'+id+'-'+tag+'/overview/s1/act3?hl=en-US'

            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.content, "html.parser")
            print(id+'#'+tag)

            server = str(soup.find_all(attrs={'class':'server-badge ml-2'})).split('>')[1].split('<')[0].strip()
            update = 'Updated ' + str(soup.find_all(attrs={'class':'mt-2 mb-0'})).split('>')[1].split('<')[0].split(':')[1].strip()
            print(server, update)

            #Rank stats
            try:
                rrRank = str(soup.find_all(attrs={'class':'profile-tier__name mt-1'})).split('>')[1].split('<')[0].strip()
                rrWinloss = str(soup.find_all(attrs={'class':'profile-tier__winrate'})).split('(')[1].split(')')[0].strip()
                rrAvgscore = str(soup.find_all(attrs={'class':'text-light-gray'})[1]).split('>')[1].split('<')[0].strip()
                rrWinrate = str(soup.find_all(attrs={'class':'text-light-gray'})[3]).split('>')[1].split('<')[0].strip()
                rrAvgdmg = str(soup.find_all(attrs={'class':'text-light-gray'})[5]).split('>')[1].split('<')[0].strip()
                rrKD = str(soup.find_all(attrs={'class':'text-light-gray'})[7]).split('>')[1].split('<')[0].strip()
                rrHS = str(soup.find_all(attrs={'class':'text-light-gray'})[9]).split('>')[1].split('<')[0].strip()
                rrAvgkills = str(soup.find_all(attrs={'class':'text-light-gray'})[11]).split('>')[1].split('<')[0].strip()
                print(rrRank, rrWinloss, rrAvgscore, rrWinrate, rrAvgdmg, rrKD, rrHS, rrAvgkills)
            except:
                rrRank = '-'
                rrWinloss = '-'
                rrAvgscore = '-'
                rrWinrate = '-'
                rrAvgdmg = '-'
                rrKD = '-'
                rrHS = '-'
                rrAvgkills = '-'
                print(rrRank, rrWinloss, rrAvgscore, rrWinrate, rrAvgdmg, rrKD, rrHS, rrAvgkills)

            #Unrank stats
            try:
                urWinloss = str(soup.find_all(attrs={'class':'profile-tier__winrate'})[1]).split('(')[1].split(')')[0].strip()
                urAvgscore = str(soup.find_all(attrs={'class':'text-light-gray'})[13]).split('>')[1].split('<')[0].strip()
                urWinrate = str(soup.find_all(attrs={'class':'text-light-gray'})[15]).split('>')[1].split('<')[0].strip()
                urAvgdmg = str(soup.find_all(attrs={'class':'text-light-gray'})[17]).split('>')[1].split('<')[0].strip()
                urKD = str(soup.find_all(attrs={'class':'text-light-gray'})[19]).split('>')[1].split('<')[0].strip()
                urHS = str(soup.find_all(attrs={'class':'text-light-gray'})[21]).split('>')[1].split('<')[0].strip()
                urAvgkills = str(soup.find_all(attrs={'class':'text-light-gray'})[23]).split('>')[1].split('<')[0].strip()
                print(urWinloss, urAvgscore, urWinrate, urAvgdmg, urKD, urHS, urAvgkills)
            except:
                urWinloss = '-'
                urAvgscore = '-'
                urWinrate = '-'
                urAvgdmg = '-'
                urKD = '-'
                urHS = '-'
                urAvgkills = '-'
                print(urWinloss, urAvgscore, urWinrate, urAvgdmg, urKD, urHS, urAvgkills)

            #SpikeRush stats
            try:
                srWinloss = str(soup.find_all(attrs={'class':'profile-tier__winrate'})[2]).split('(')[1].split(')')[0].strip()
                srAvgscore = str(soup.find_all(attrs={'class':'text-light-gray'})[25]).split('>')[1].split('<')[0].strip()
                srWinrate = str(soup.find_all(attrs={'class':'text-light-gray'})[27]).split('>')[1].split('<')[0].strip()
                srAvgdmg = str(soup.find_all(attrs={'class':'text-light-gray'})[29]).split('>')[1].split('<')[0].strip()
                srKD = str(soup.find_all(attrs={'class':'text-light-gray'})[31]).split('>')[1].split('<')[0].strip()
                srHS = str(soup.find_all(attrs={'class':'text-light-gray'})[33]).split('>')[1].split('<')[0].strip()
                srAvgkills = str(soup.find_all(attrs={'class':'text-light-gray'})[35]).split('>')[1].split('<')[0].strip()
                print(srWinloss, srAvgscore, srWinrate, srAvgdmg, srKD, srHS, srAvgkills)
            except:
                srWinloss = '-'
                srAvgscore = '-'
                srWinrate = '-'
                srAvgdmg = '-'
                srKD = '-'
                srHS = '-'
                srAvgkills = '-'
                print(srWinloss, srAvgscore, srWinrate, srAvgdmg, srKD, srHS, srAvgkills)

            #DeathMatch stats
            #dmWinloss = str(soup.find_all(attrs={'class':'profile-tier__winrate'})[3]).split('(')[1].split(')')[0].strip()
            #dmAvgscore = str(soup.find_all(attrs={'class':'text-light-gray'})[37]).split('>')[1].split('<')[0].strip()
            #dmWinrate = str(soup.find_all(attrs={'class':'text-light-gray'})[39]).split('>')[1].split('<')[0].strip()
            #dmAvgdmg = str(soup.find_all(attrs={'class':'text-light-gray'})[41]).split('>')[1].split('<')[0].strip()
            #dmKD = str(soup.find_all(attrs={'class':'text-light-gray'})[43]).split('>')[1].split('<')[0].strip()
            #dmHS = str(soup.find_all(attrs={'class':'text-light-gray'})[45]).split('>')[1].split('<')[0].strip()
            #dmAvgkills = str(soup.find_all(attrs={'class':'text-light-gray'})[47]).split('>')[1].split('<')[0].strip()
            #print(dmWinloss, dmAvgscore, dmWinrate, dmAvgdmg, dmKD, dmHS, dmAvgkills)

            embed = discord.Embed(title=id+'#'+tag+"'s Valorant Stats                                                             ㅤ", description='Rank Stats', color=0xFF2424)

            #Rank Image
            if rrRank == 'Iron 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067727502540830/iron1.png')
            elif rrRank == 'Iron 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067729323393024/iron2.png')
            elif rrRank == 'Iron 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067731050397717/iron3.png')
            elif rrRank == 'Bronze 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067744812171305/bronze1.png')
            elif rrRank == 'Bronze 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067746142421002/bronze2.png')
            elif rrRank == 'Bronze 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067748104699914/bronze3.png')
            elif rrRank == 'Silver 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067758758232114/silver1.png')
            elif rrRank == 'Silver 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067760327688232/silver2.png')
            elif rrRank == 'Silver3 ':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067762079989780/silver3.png')
            elif rrRank == 'Gold 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067770564935720/gold1.png')
            elif rrRank == 'Gold 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067772318810122/gold2.png')
            elif rrRank == 'Gold 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067774437195806/gold3.png')
            elif rrRank == 'Platinum 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067783362019378/platinum1.png')
            elif rrRank == 'Platinum 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067785380003880/platinum2.png')
            elif rrRank == 'Platinum 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067786860199967/platinum3.png')
            elif rrRank == 'Diamond 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067815926595614/diamond1.png')
            elif rrRank == 'Diamond 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067817289744394/diamond2.png')
            elif rrRank == 'Diamond 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067819260674068/diamond3.png')
            elif rrRank == 'Immortal 1':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067829050703902/immortal1.png')
            elif rrRank == 'Immortal 2':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067830401663036/immortal2.png')
            elif rrRank == 'Immortal 3':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067831949099078/immortal3.png')
            elif rrRank == 'Radiant':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067837997678602/Radiant.png')
            elif rrRank == 'Unrated':
                embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/790067665930420285/790067844519821322/unranked.png')


            #Rank Embed
            embed.add_field(name = 'Rank', value = rrRank, inline = True)
            embed.add_field(name = 'W/L', value = rrWinloss, inline = True)
            embed.add_field(name = 'AvgScore', value = rrAvgscore, inline = True)
            embed.add_field(name = 'WinRate', value = rrWinrate, inline = True)
            embed.add_field(name = 'AvgDMG', value = rrAvgdmg, inline = True)
            embed.add_field(name = 'K/D', value = rrKD, inline = True)
            embed.add_field(name = 'HeadShot', value = rrHS, inline = True)
            embed.add_field(name = 'AvgKills', value = rrAvgkills, inline = True)

            #Unrated Embed
            embed.add_field(name = 'ㅤ', value = '\nUnrated Stats', inline = False)
            embed.add_field(name = 'W/L', value = urWinloss, inline = True)
            embed.add_field(name = 'AvgScore', value = urAvgscore, inline = True)
            embed.add_field(name = 'WinRate', value = urWinrate, inline = True)
            embed.add_field(name = 'AvgDMG', value = urAvgdmg, inline = True)
            embed.add_field(name = 'K/D', value = urKD, inline = True)
            embed.add_field(name = 'HeadShot', value = urHS, inline = True)
            embed.add_field(name = 'AvgKills', value = urAvgkills, inline = True)

            #Spike Rush Embed
            embed.add_field(name = 'ㅤ', value = '\nSpikeRush Stats', inline = False)
            embed.add_field(name = 'W/L', value = srWinloss, inline = True)
            embed.add_field(name = 'AvgScore', value = srAvgscore, inline = True)
            embed.add_field(name = 'WinRate', value = srWinrate, inline = True)
            embed.add_field(name = 'AvgDMG', value = srAvgdmg, inline = True)
            embed.add_field(name = 'K/D', value = srKD, inline = True)
            embed.add_field(name = 'HeadShot', value = srHS, inline = True)
            embed.add_field(name = 'AvgKills', value = srAvgkills, inline = True)

            #DeathMatch Embed
            #embed.add_field(name = 'ㅤ', value = '\nDeathMatch Stats', inline = False)
            #embed.add_field(name = 'W/L', value = dmWinloss, inline = True)
            #embed.add_field(name = 'AvgScore', value = dmAvgscore, inline = True)
            #embed.add_field(name = 'WinRate', value = dmWinrate, inline = True)
            #embed.add_field(name = 'AvgDMG', value = dmAvgdmg, inline = True)
            #embed.add_field(name = 'K/D', value = dmKD, inline = True)
            #embed.add_field(name = 'HeadShot', value = dmHS, inline = True)
            #embed.add_field(name = 'AvgKills', value = dmAvgkills, inline = True)

            embed.set_footer(text=update+'/Made by osung0054#6765')
            await message.channel.send(embed=embed)
        except:
            embed = discord.Embed(title='Failed to Track your Stats.', description='or an error occured', color=0xFF2424)
            embed.add_field(name = "1. Sign in", value = 'Go to\n**https://dak.gg/valorant**\nand sign in to track your stats.', inline = False)
            embed.add_field(name = '2. Check your account ID', value = 'There may be some typing errors.', inline = False)
            embed.add_field(name = '3. There may be some errors in this bot.', value = 'Im sorry:(', inline = False)
            await message.channel.send(embed=embed)
    
client.run(TOKEN)