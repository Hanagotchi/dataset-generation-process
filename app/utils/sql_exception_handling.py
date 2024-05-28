from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import PendingRollbackError, IntegrityError, NoResultFound
import logging

logger = logging.getLogger("app")
logger.setLevel("DEBUG")


def handle_common_errors(err):
    logger.error(format(err))
    raise err


def withSQLExceptionsHandle(async_mode: bool = False):
    def decorator(func):
        async def handleAsyncSQLException(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception as err:
                return handle_common_errors(err)

        def handleSyncSQLException(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                return handle_common_errors(err)

        return (
            handleAsyncSQLException if async_mode else handleSyncSQLException
        )

    return decorator
