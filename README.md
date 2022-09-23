# Example pyspark application

## Project structure

- cicd: here is where you have your pipelines that run integration tests and your python package is built into a wheel that can be installed in the Dataproc cluster.
- scripts: here you can find the python script that will run the app
- src: in this directory you will have your module(s) that can easily be imported from the deployed scripts and tested (modularity is the key to good tests!)
- tests: test module. Here you could test your transforms locally to make sure the output is the desired one.
- requirements.txt: python dependencies, useful for local development and also to configure your Dataproc cluster
- setup.cfg, setup.py: python package stuff (if you want to go for the building a wheel approach)