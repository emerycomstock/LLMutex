from llmutex.src.core.configuration.configuration_source_of_truth import ConfigurationSourceOfTruth
from ...common.types.configuration import Settings, Resources

class ConfigurationManager:

    # TODO: Set "source of truth" ConfigurationSource alongside "overrides" where "source of truth" has overrides written back to it, maybe a new ABC type that allows writes
    # TODO: Other sources are "override sources" they will not yield a full configuration, only targeted overrides, will need a different type
    def __init__(
            self,
            settings_sources: ConfigurationSourceOfTruth[Settings],
            resources_sources: ConfigurationSourceOfTruth[Resources],
            refresh_interval_s: int):
        pass

    def refresh(self):
        pass