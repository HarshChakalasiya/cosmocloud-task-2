import traceback
import uuid

from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool
from starlette.middleware.base import RequestResponseEndpoint
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from logger import logger
from routers.organisation_router import organisation_router
from routers.permission_router import permission_router
from routers.user_router import user_router
from util.context_vars import request_id_contextvar
from util.exceptions.application_exception import ApplicationException


tags_metadata= [
    {
        "name": "permissions",
        "description": "Please use the following value for permission type.  **READ(0), WRITE(1),ADMIIN(2)**"
    }
]
app = FastAPI(
    title="CosmosCloud Task 2 Docs",
    description="",
    version="0.1.0",
    docs_url="/cosmocloud/v1/docs",
    redoc_url="/cosmocloud/v1/redoc",
    openapi_url="/cosmocloud/v1/openapi.json",
    openapi_tags=tags_metadata
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
def closing_event():
    print("Application Shutdown")

@app.middleware("http")
async def project_middleware(request: Request, call_next: RequestResponseEndpoint):
    request_id = str(uuid.uuid4())
    request_id_contextvar.set(request_id)

    with logger.contextualize(request_id=request_id):
        request_headers = {}
        logger.info(
            f"{request.method} request to {request.url} metadata"
            f"\tHeaders: {request_headers}"
            f"\tPath Params: {request.path_params}"
        )

        try:
            response = await call_next(request)
            response.headers["X-Request-ID"] = request_id
            response_body = [chunk async for chunk in response.body_iterator]
            response.body_iterator = iterate_in_threadpool(iter(response_body))
            logger.info("Response : " + str(response_body[0].decode()))

            return response

        except Exception as ex:
            exp_trace = ('\t'.join(traceback.format_exc().splitlines()))
            logger.error(f"Exception : {exp_trace}")
            return JSONResponse(content={"result": "unable to process request"}, status_code=500,
                                headers={"request_id": request_id})

        finally:
            logger.info("Request ended")

@app.exception_handler(ApplicationException)
async def application_exception_handler(request: Request, exc: ApplicationException):
    response= {"statusCode": exc.status_code, "data": exc.args, "error": exc.message}
    return JSONResponse(
        status_code=exc.status_code,
        content=response
    )

path_prefix ="/cosmocloud/v1"
app.include_router(user_router, prefix=path_prefix)
app.include_router(organisation_router, prefix=path_prefix)
app.include_router(permission_router, prefix=path_prefix)