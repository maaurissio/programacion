import discord
from discord.ext import commands
import yt_dlp
import asyncio
import concurrent.futures
from youtubesearchpython import VideosSearch

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

class MusicQueue:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.current = None

    async def add(self, song):
        await self.queue.put(song)

    async def get(self):
        self.current = await self.queue.get()
        return self.current

    def is_empty(self):
        return self.queue.empty()

music_queue = MusicQueue()


@bot.event
async def on_ready():
    print(f'el botsito {bot.user.name} ta listo papi')

with yt_dlp.YoutubeDL({'format': 'ba/ba*', 'noplaylist': True, 'ffmpeg_location': 'C:/Program Files (x86)/ffmpeg'}) as ydl:

    @bot.command(name='join')
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            try:
                await channel.connect()
            except discord.errors.ClientException as e:
                await ctx.send("no me deja conectarme sorry :,,v")
        else:
            await ctx.send("uneme a la wea pa usar el comando po")

    @bot.command(name='leave')
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            await ctx.send("no estoy en ningun canal y quieres sacarme jaja aweonao")

    def download_song_sync(url):
        with yt_dlp.YoutubeDL({'format': 'ba/ba*', 'noplaylist': True}) as ydl:
            ydl.download([url])

    async def download_song(url):
        with concurrent.futures.ThreadPoolExecutor() as pool:
            await bot.loop.run_in_executor(pool, download_song_sync, url)

    @bot.command(name='play')
    async def play(ctx, *, search_query):
        if not ctx.voice_client:
            await join(ctx)

        if ctx.voice_client:
            async with ctx.typing():
                try:
                    videos_search = VideosSearch(search_query, limit=1)
                    result = videos_search.result()

                    if result['result']:
                        video_url = result['result'][0]['link']

                        with yt_dlp.YoutubeDL({'format': 'ba/ba*', 'noplaylist': True}) as ydl:
                            info = ydl.extract_info(video_url, download=False)

                            audio_format = next(
                                (fmt for fmt in info['formats'] if fmt.get('acodec') != 'none' and fmt.get('vcodec') == 'none'),
                                None
                            )

                            if audio_format:
                                await music_queue.add(audio_format['url'])
                                bot.loop.create_task(download_song(audio_format['url']))

                                if not ctx.voice_client.is_playing():
                                    await start_playing(ctx)

                            else:
                                await ctx.send("no se encontraron formatos de audio hrno :/")
                    else:
                        await ctx.send("no encontre tu cancion culia")

                except yt_dlp.utils.DownloadError:
                    await ctx.send("no pude descargar el video jaja cagaste")
        else:
            await ctx.send("primero uneme a un canal qlo po wn")

    @bot.command(name='skip')
    async def skip(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("ahi ta skipeando la wea")
            await check_queue(ctx, None)
        else:
            await ctx.send("no hay nada reproduciendo nanito")

    async def check_queue(ctx, error):
        if error:
            print("ajksjkd no puedo bro sorry")

        if music_queue.is_empty():
            await ctx.voice_client.disconnect()
            await ctx.send("no hay nada en la cola wn no reproducire nada")
        else:
            await start_playing(ctx)

    async def start_playing(ctx):
        print("intentando reproducir la guea")
        while not music_queue.is_empty():
            song = await music_queue.get()
            print("ahi ta sonando el temita rey")
            try:
                audio_source = discord.FFmpegPCMAudio(executable="ffmpeg", source=song)
                ctx.voice_client.play(audio_source, after=lambda error: check_queue(ctx, error))
                await ctx.send(f"ahi ta sonando el temita rey")

            except Exception as e:
                print("no se puede reproducir bro")

    async def check_queue(ctx, error):
        if error:
            print("no se puede reproducir bro")
        if music_queue.is_empty():
            await ctx.voice_client.disconnect()
            await ctx.send("no hay canciones en la cola me voy xao")
        else:
            await start_playing(ctx)


    async def start_playing(ctx):
        while not music_queue.is_empty():
            song = await music_queue.get()
            ctx.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=song), after=lambda: asyncio.run_coroutine_threadsafe(start_playing(ctx), bot.loop))
            await ctx.send("ahi ta sonando el temita rey")
            break

    @bot.command(name='pause')
    async def pause(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("ya pause la wea")
        else:
            await ctx.send("no hay canciones sonando wn")

    @bot.command(name='resume')
    async def resume(ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("ahi te la pause")
        else:
            await ctx.send("no hay canciones pausadas jajsda")

    @bot.command(name='stop')
    async def stop(ctx):
        if ctx.voice_client and (ctx.voice_client.is_playing() or ctx.voice_client.is_paused()):
            ctx.voice_client.stop()
            await ctx.send("listo ya no suena ma la wea")
        else:
            await ctx.send("no hay canciones sonando wn")
    
    bot.run('MTI0NjI5NjA4NjcxMzIwODkxMw.Gunvlp.yMYLKK_P8qQP2z5Y8Jy6guAS221_Fb2pDHOPBQ')