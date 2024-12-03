import pytest

from pytouchlinesl import Module, TouchlineSL, Zone

from .fake_client import FakeRothAPI


@pytest.fixture
def test_touchlinesl() -> TouchlineSL:
    client = FakeRothAPI()
    return TouchlineSL(client=client)


@pytest.fixture
def test_touchlinesl_short_cache() -> TouchlineSL:
    client = FakeRothAPI()
    return TouchlineSL(client=client, cache_validity=0.1)


@pytest.fixture
async def test_module(test_touchlinesl: TouchlineSL) -> Module:
    m = await test_touchlinesl.module(module_id="1234a5678a9123a456a7891234a56789")
    assert isinstance(m, Module)
    return m


@pytest.fixture
async def test_module_short_cache(test_touchlinesl_short_cache: TouchlineSL) -> Module:
    m = await test_touchlinesl_short_cache.module(module_id="1234a5678a9123a456a7891234a56789")
    assert isinstance(m, Module)
    return m


@pytest.fixture
async def test_zone(test_module: Module) -> Zone:
    z = await test_module.zone_by_name("Kitchen")
    assert isinstance(z, Zone)
    return z
