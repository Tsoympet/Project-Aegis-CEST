import yaml

def load_choices(override_path=None):
    # Load the default choices from the YAML file
    if override_path:
        with open(override_path, 'r') as f:
            return yaml.safe_load(f)
    else:
        with open('config/choices_default.yaml', 'r') as f:
            return yaml.safe_load(f)
