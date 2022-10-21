from datetime import date
from typing import Optional


def get_transferred_to_tunnellers(posted_date: Optional[date], posted_from: Optional[str]) -> Optional[dict[Optional[str], Optional[str]]]:
    if posted_date and posted_from is not None:
        return {'posted_date': posted_date, 'posted_from': posted_from}
    return None
