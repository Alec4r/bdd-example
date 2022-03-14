from abc import ABC, abstractmethod
from typing import Optional, Type


class ImageRepository(ABC):
    @abstractmethod
    def find(self, image_name: str) -> Optional[Type[str]]:
        pass
    