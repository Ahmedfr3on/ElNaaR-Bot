import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# رقم قناة الترحيب
WELCOME_CHANNEL_ID = 1561908449485258822

@bot.event
async def on_ready():
    print(f'✅ البوت شغال بنجاح: {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="سيرفر ElNaaR 🔥"))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        embed = discord.Embed(
            title="عضو جديد انضم إلينا! 🎉",
            description=f"أهلاً بك يا {member.mention} في سيرفر **ElNaaR**!\nنتمنى لك وقتاً ممتعاً معنا. لا تنسَ قراءة القوانين.",
            color=discord.Color.gold()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"أنت العضو رقم {member.guild.member_count} 🌟")
        await channel.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content.lower().strip()

    if msg in ['السلام عليكم', 'سلام عليكم']:
        await message.reply(f'وعليكم السلام ورحمة الله وبركاته يا {message.author.mention} 🌟')
    elif msg in ['ازيك', 'إزيك', 'اخبارك', 'أخبارك']:
        await message.reply(f'أنا تمام يا {message.author.mention}، وجودك هنا بيخليني أسعد! ❤️ إنت أخبارك إيه؟')
    elif msg in ['صباح الخير', 'صباح الفل']:
        await message.reply(f'صباح النور والسرور يا {message.author.mention} ☀️')
    elif msg in ['مساء الخير', 'مساء الفل']:
        await message.reply(f'مساء الورد والياسمين يا {message.author.mention} 🌙')
    elif msg in ['مين عملك', 'مين صنعك', 'مين المطور']:
        await message.reply('أنا من صنع المطور الأسطوري **أحمد**! 🧑‍💻🔥')
    elif msg in ['الاوامر', 'اوامر', 'مساعدة', 'help']:
        embed = discord.Embed(title="📜 قائمة أوامر البوت", color=discord.Color.blue())
        embed.add_field(name="الردود التلقائية", value="السلام عليكم\nازيك\nصباح الخير\nمساء الخير\nمين المطور", inline=False)
        embed.set_footer(text="ElNaaR Bot System")
        await message.reply(embed=embed)

    await bot.process_commands(message)

# قراءة التوكن بأمان من إعدادات الاستضافة
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("❌ خطأ: التوكن غير موجود!")
