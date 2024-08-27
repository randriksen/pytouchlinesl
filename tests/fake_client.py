import json
import os
from pathlib import Path

from pytouchlinesl.client import BaseClient
from pytouchlinesl.client.models import AccountModuleModel, ModuleModel

data_dir = Path(os.path.realpath(__file__)).parent / "sample-data"


class FakeRothAPI(BaseClient):
    def __init__(self):
        self._user_id = 123456789
        self._token = "deadbeef"

    async def user_id(self) -> int:
        return self._user_id

    async def authenticated(self) -> bool:
        return True if self._token else False

    async def modules(self) -> list[AccountModuleModel]:
        with open(data_dir / "modules.json", "r") as f:
            data = json.load(f)

        return [AccountModuleModel(**m) for m in data]

    async def module(self, module_id: str) -> ModuleModel:
        with open(data_dir / "module.json", "r") as f:
            data = json.load(f)

        return ModuleModel(**data)

    async def set_zone_temperature(
        self, module_id: str, mode_id: int, zone_id: int, temperature: float
    ):
        raise NotImplementedError

    async def set_zone_schedule(self, module_id: str, zone_id: int, schedule_id: int):
        raise NotImplementedError
