import yaml
from cest_calculator import main  # Import the calculator function

def run_scenario(scenario_file):
    with open(scenario_file, 'r') as f:
        scenario_data = yaml.safe_load(f)
    
    # Example: iterate over different configurations in the scenario YAML
    for config in scenario_data['configs']:
        print(f"Running scenario with {config}")
        # Here you would call the actual calculator with arguments from config
        main()  # (Adjust this to pass specific config args to the main function)
