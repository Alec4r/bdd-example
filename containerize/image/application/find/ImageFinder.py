from containerize.image.domain import ImageRepository

class ImageFinder:
    def __init__(self, repository: ImageRepository):
        self.repository = repository

    def __call__(self, image_name: str):
        return self.repository.find(image_name=image_name)
