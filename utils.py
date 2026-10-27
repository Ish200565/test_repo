import logging
import re
from datetime import datetime, timezone

# Setup application logging
def setup_logging(level: str = "INFO") -> logging.Logger:
    """Configure and return a standard logger."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger("app_logger")

logger = setup_logging()

def validate_email(email: str) -> bool:
    """Validate email format using a standard regular expression."""
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    return False

def get_utc_now() -> datetime:
    """Return the current timezone-aware UTC datetime."""
    return datetime.now(timezone.utc)

def format_datetime(dt: datetime, fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format a datetime object into a clean string representation."""
    return dt.strftime(fmt)

def slugify(text: str) -> str:
    """Convert a string into a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text
