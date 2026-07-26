from typing import TypeVar, Generic
from abc import ABC, abstractmethod
from ...common.types.configuration import Settings, Resources

ConfigModel = TypeVar('ConfigModel', Settings, Resources)

class ConfigurationSourceOfTruth(ABC, Generic[ConfigModel]):

    @abstractmethod
    def resolve(self) -> ConfigModel:
        """ Returns the last """
        pass
