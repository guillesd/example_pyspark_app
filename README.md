# Example pyspark application
The main goal of this repository is to provide an example of a PySpark application that can be packaged into a wheel file and easily deployed to any cloud service that supports Spark (e.g. Databricks, EMR, DataProc). The structure is opinionated based on what I consider to be best practice in developing PySpark/Python applications for data processing.

## Project structure

- .github/workflows: This is were your CI/CD pipeline lives. This pipeline runs the integration tests, builds and deploys your code to a hosted Spark service (e.g. Databricks, EMR, DataProc)
- data: Sample data used to run your code locally
- src: In this directory you will have your module(s) with transformations, read and write functions as well as the entrypoint scripts for your Spark jobs.
- tests: Here is where you define unit tests. The main goal is to unit test the transforms and also have an end-2-end test to make sure that the pipeline is able to work without raising exceptions. If you are using Delta, make sure you specify the Delta dependencies in your Spark sesison.
- setup.py: Python package stuff (if you want to go for the building a wheel approach)
- .pre-commit-config.yaml: Pre-commit to format your code appropriately.

## Development

Install the package in edit mode:
```
pip install -e .
```
This will install all requirements (not much). If pinned versions of certain dependencies are needed for development, add a `requirements.txt` file or consider using other package managers such as Poetry or Flit.

To run unit tests, run the following command:
```
pytest
```

To keep your code formatted on every commit, please run the following:
```
pre-commit install
```