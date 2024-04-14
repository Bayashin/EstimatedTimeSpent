from _typeshed import Incomplete
from api.lib.mysql import get_db as get_db
from sqlalchemy.orm import Session as Session

router: Incomplete

async def get_probability_reporting_before(reporting: str, before: str, user_id: int = 0, str_date: str = '2024-1-1', time: str = '10:30:00', db: Session = ...): ...
