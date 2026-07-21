from configuration_source import ConfigurationSource
from ...common.types.configuration import Settings, Resources

class ConfigurationManager:

    def __init__(
            self,
            settings_sources: list[ConfigurationSource[Settings]],
            resources_sources: list[ConfigurationSource[Resources]],
            refresh_interval_s: int):
        pass

    def refresh(self):
        pass