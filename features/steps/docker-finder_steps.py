import pytest
from behave import given, when, then, step
from containerize.image.application.find.ImageFinder import ImageFinder
from containerize.image.infrastructure.ImageDockerSDKRepository import ImageDockerSDKRepository
from containerize.image.infrastructure.ImageInMemoryRepository import ImageInMemoryRepository
from containerize.image.domain.ImageNotFound import ImageNotFound

@given('We have installed docker')
def step_impl(context):
    context.repository = ImageInMemoryRepository(username="", password="")

@when('We search {user}/{repository}:{tag}')
def step_impl(context, user, repository, tag):
    assert isinstance(repository, str) and isinstance(tag, str)
    context.image_name = f"{user}/{repository}:{tag}"

@then('We get the image name')
def step_impl(context):
    
    finder = ImageFinder(repository=context.repository)
    assert context.failed is False
    assert finder(image_name=context.image_name) == context.image_name

@then('We get an exeption')
def step_impl(context):
    try:
        finder = ImageFinder(repository=context.repository)
        finder(image_name=context.image_name)
        assert False, "Exception didn't exec"
    except ImageNotFound:
        assert True

