from honeybee_model_schema.energy.simulationparameter import SimulationParameter
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'honeybee_model_schema', 'samples')


def test_detailed_simulation_par():
    file_path = os.path.join(target_folder, 'simulation_par_detailed.json')
    SimulationParameter.parse_file(file_path)


def test_simple_simulation_par():
    file_path = os.path.join(target_folder, 'simulation_par_simple.json')
    SimulationParameter.parse_file(file_path)
