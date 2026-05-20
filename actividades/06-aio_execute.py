from aiohttp import web
import asyncio

async def execute(request):
    cmd = request.query.get('cmd')
    if not cmd:
        return web.Response(text="Missing 'cmd' parameter", status=400)
    # WARNING: in production validate/sanitize cmd or use a whitelist
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    out, err = await proc.communicate()
    text = ''
    if out:
        text += out.decode(errors='ignore')
    if err:
        text += '\nERR:\n' + err.decode(errors='ignore')
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/execute', execute)

if __name__ == '__main__':
    web.run_app(app, port=8080)
