from mcstatus import JavaServer
import discord

# You can pass the same address you'd enter into the address field in minecraft into the 'lookup' function
# If you know the host and port, you may skip this and use JavaServer("example.org", 1234)
server = JavaServer.lookup("localhost:25565")

async def server_status(ctx, bot):
    loading_server = discord.Embed(title="Loading server...", description="Loading...", color=0xD0B8A0)
    msg = await ctx.send(embed = loading_server)
    
    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    # Don't expect the player list to always be complete, because many servers run
    # plugins that hide this information or limit the number of players returned or even
    # alter this list to contain fake players for purposes of having a custom message here.
    
    try:
        status = server.status()
    # print(f"The server has {status.players.online} player(s) online and replied in {status.latency} ms")
    except:
        status = None
    if status:
        output = f"The server has {status.players.online} player(s) online and replied in {status.latency} ms\n"
        query = server.query()
        if (status.players.online != 0):
            output += f"The server has the following players online: {', '.join(query.players.names)}"
    else:
        output = "The server is offline"
    # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
    # It is included in a 'status' call, but is also exposed separate if you do not require the additional info.
    # latency = server.ping()
    # print(f"The server replied in {latency} ms")

    # 'query' has to be enabled in a server's server.properties file!
    # It may give more information than a ping, such as a full player list or mod information.
    
    embedVar = discord.Embed(title="Minecraft Server Status", description=f"{output}", color=0xD0B8A0)
    await msg.edit(embed = embedVar)
