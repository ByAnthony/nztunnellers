from typing import Optional


def get_parent(name: Optional[str], origin: Optional[str]) -> Optional[dict[Optional[str], Optional[str]]]:
    if name and origin is not None:
        return {'name': name, 'origin': origin}
    return None
