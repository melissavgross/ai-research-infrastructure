import random
import time
import logging

# Set up logging for better traceability
logging.basicConfig(level=logging.INFO)

class ExperimentRunner:
    def __init__(self, model, parameters, retries=3):
        """
        Initialize the experiment runner.

        Args:
        model (object): The AI model to run experiments on.
        parameters (dict): Parameters to configure the experiment.
        retries (int): Number of retries in case of failures. Default is 3.
        """
        self.model = model
        self.parameters = parameters
        self.retries = retries

    def run_experiment(self):
        """
        Run the experiment with retries on failure.

        Returns:
        bool: True if the experiment succeeds, False otherwise.
        """
        success = False
        attempt = 0

        while attempt < self.retries and not success:
            try:
                logging.info(f"Running experiment with parameters: {self.parameters}")
                success = self.model.run(self.parameters)

                if success:
                    logging.info("Experiment succeeded.")
                else:
                    logging.error("Experiment failed. Retrying...")
                    raise ValueError("Model failed to run successfully.")

            except Exception as e:
                logging.error(f"Error occurred: {e}. Retrying... (Attempt {attempt+1}/{self.retries})")
                attempt += 1
                time.sleep(random.randint(1, 3))  # Simulate retry delay

        if not success:
            logging.error(f"Experiment failed after {self.retries} attempts.")
        return success

# Example AI model (Mock)
class MockModel:
    def run(self, params):
        """
        Simulate running an experiment. Randomly succeed or fail.

        Args:
        params (dict): Parameters for the experiment.

        Returns:
        bool: Random success or failure.
        """
        return random.choice([True, False])

if __name__ == "__main__":
    # Test with a mock model
    experiment = ExperimentRunner(MockModel(), {'param1': 'value1', 'param2': 'value2'})
    experiment.run_experiment()
