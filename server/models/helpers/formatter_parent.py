from typing import Optional
from models.origins import Parent


def get_parent(name: Optional[str], origin: Optional[str]) -> Optional[Parent]:
    if name and origin is not None:
        return {'name': name, 'origin': origin}
    return None
