from typing import Optional, Type
from containerize.image.domain.ImageRepository import ImageRepository
from containerize.image.domain.ImageNotFound import ImageNotFound

class ImageInMemoryRepository(ImageRepository):
    def find(self, image_name: str) -> Optional[Type[str]]:
        return image_name
