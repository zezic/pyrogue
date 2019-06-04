import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from engine.engine import Engine
from engine.level import Level
from engine.objects import PlayerObject, GoldObject

templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='static'), name='static')


engine = Engine()

level = Level((13, 7))
player_object = PlayerObject()
level.add_object(player_object, (4, 3))
level.add_object(GoldObject(), (2, 3))
level.add_object(GoldObject(), (6, 2))
level.add_object(GoldObject(), (10, 5))

engine.add_level(level, 0)


@app.route('/')
async def index_page(request):
    return templates.TemplateResponse('index.html.j2', {'request': request})


@app.route('/api/level')
async def level_api(request):
    rendered = [
        [obj.render() if obj else '.' for obj in row]
        for row in level.object_map
    ]
    return JSONResponse(rendered)


@app.route('/api/walk', methods=['POST'])
async def walk_api(request):
    data = await request.json()
    engine.walk(0, player_object.uuid, data.get('magnitude'))
    return JSONResponse({'status': 'success'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
