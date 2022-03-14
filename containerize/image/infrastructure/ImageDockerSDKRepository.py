import docker
from typing import Optional, Type
from containerize.image.domain.ImageRepository import ImageRepository
from containerize.image.domain.ImageNotFound import ImageNotFound

class ImageDockerSDKRepository(ImageRepository):
    def __init__(self, username: str, password: str, registry: str = "https://index.docker.io/v1/"):
        self.CLIENT = docker.from_env()
        self.CLIENT.login(username=username, password=password, registry=registry) 

    def find(self, image_name: str) -> Optional[Type[str]]:
        try:
           registry_data = self.CLIENT.images.get_registry_data(name=image_name)
        except docker.errors.NotFound as e:
            raise ImageNotFound(f"The image {image_name} doesn't exists")

        return registry_data.image_name
