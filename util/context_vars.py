import contextvars

request_id_contextvar = contextvars.ContextVar("request_id", default='')