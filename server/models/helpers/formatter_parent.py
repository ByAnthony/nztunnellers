from typing import Optional


def get_parent(name: Optional[str], country: Optional[str]) -> Optional[dict[Optional[str], Optional[str]]]:
    if name and country is not None:
        return {'name': name, 'origin': country}
    return None
