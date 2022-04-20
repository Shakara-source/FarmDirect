from fastapi import Request
from fastapi.responses import JSONResponse
from Infrastructure.Config.token import verify_token


async def AuthShopper(request: Request, call_next):
    """Middleware for authenticating farmers on required routes"""
    token = str(
        request.cookies.get("jwtToken")
    )

    try:
        shopper_id = verify_token(token)
        if shopper_id:
            request.state.shopper_id = shopper_id
            response = await call_next(request)
            return response
    
    except Exception:
        return JSONResponse(content={"description": "Unauthorized"},
                            status_code=401)
