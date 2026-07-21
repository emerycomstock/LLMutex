from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from ...common.types.configuration import Settings, Resources

ConfigModel = TypeVar('ConfigModel', Settings, Resources)

class ConfigurationSource(ABC, Generic[ConfigModel]):

    @abstractmethod
    def resolve_config(self) -> ConfigModel:
        pass
