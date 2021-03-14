import fastapi
from starlette.requests import Request

from app.api import crud
from starlette.templating import Jinja2Templates

templates = Jinja2Templates('app/templates')
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def index(request: Request):
    summaries = await crud.get_all()
    data = {'request': request, 'summaries': summaries}
    return templates.TemplateResponse('home/index.html', data)

@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url='/app/static/img/favicon.ico')