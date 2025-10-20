"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# Import after app creation but avoid inline imports by placing under try-except
try:
    from service import routes  # noqa: F401
    from service.common import log_handlers
except ImportError:
    pass

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
