import yaml
from typing import TypeVar
from pydantic import ValidationError
from llmutex.src.core.configuration.configuration_source_of_truth import ConfigurationSourceOfTruth
from ...common.constants import YAML_EXTENSIONS
from ...common.types.configuration import Settings, Resources

ConfigModel = TypeVar('ConfigModel', Settings, Resources)

class FileConfigurationSource(ConfigurationSourceOfTruth[ConfigModel]):
    """ Configuration source that reads from a file """

    # TODO: Add validation as a method or byproduct of existing method
    # TODO: Validate path exists
    # TODO: Validate file extension supported

    # TODO: Do not crash on validation as long as initial config was resolved - this means you resolve config immediately on initialization
    # TODO: If file is deleted mid-run re-create
    # TODO: If file is not found at start, generate with defaults

    def __init__(self, path: str, default_config: ConfigModel):
        self.path = self._validate_file_type_supported(path)
        self.config = default_config

    def resolve(self) -> ConfigModel:
        try:
            with open(self.path, 'r') as file:
                data = yaml.safe_load(file)
                self.config = ConfigModel.model_validate(data)
        except FileNotFoundError as e:
            # If config file does not exist -> create it from last valid config (likely the default)
            # TODO: Error log
            self._dump_config_to_file()
        except ValidationError as e:
            # If config file has invalid format -> back up the file and overwrite with last valid config (likely the default)
            # TODO: Error log
            # TODO: Move broken file to .bak
            self._dump_config_to_file()
        except Exception as e:
            # TODO: Error log
            pass

        return self.config
    
    def _dump_config_to_file(self) -> ConfigModel:
        try:
            yaml_str = yaml.dump(self.config.model_dump(), default_flow_style=False, indent=4)
            with open(self.path, 'w') as file:
                file.write(yaml_str)
        except Exception as e:
            # TODO: Error log
            pass
        
    def _validate_file_type_supported(self, path: str) -> str:
        if any(YAML_EXTENSIONS, path.endswith):
            return path
        raise ValueError(f"Configuration file '{path}' must be a valid YAML file type.")
