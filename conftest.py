import pytest as pytest


@pytest.fixture(scope='function',params=['1'],autouse=True)
def aaa(request):
    return request.param
