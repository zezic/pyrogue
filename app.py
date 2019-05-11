import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='static'), name='static')


class Level():
    def __init__(self):
        self.height = 5
        self.width = 5
        self.map = [
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '@', '.', '.'],
            ['.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.']
        ]
        self.objects = {
            '@': {
                'position': {
                    'x': 2,
                    'y': 2
                }
            }
        }

    def move(self, direction):
        player = self.objects.get('@')
        position = player.get('position')
        x, y = position.get('x'), position.get('y')
        self.map[y][x] = '.'

        x_dir, y_dir = direction.get('x'), direction.get('y')
        position.update({
            'x': (x + x_dir) % self.width,
            'y': (y + y_dir) % self.height
        })
        self.map[position.get('y')][position.get('x')] = '@'


level = Level()


@app.route('/')
async def index_page(request):
    return templates.TemplateResponse('index.html.j2', {'request': request})


@app.route('/api/level')
async def level_api(request):
    return JSONResponse(level.map)


@app.route('/api/move', methods=['POST'])
async def moving_api(request):
    data = await request.json()
    level.move(data.get('direction'))
    return JSONResponse({'status': 'success'})


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
