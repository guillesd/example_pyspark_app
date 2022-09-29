To test code using dbx, first:

1. Install dbx in your environment
```bash
pip install dbx
```

2. Configure your databricks cli
```bash
databricks configure --profile example_pyspark_app --token <my_personal_access_token>
```
You can reuse this profile

3. After defining the `deployment.yml` (see example) you can run your code against an interactive cluster, like so:
```bash
dbx execute awesome-etl --task=main --cluster-name="some-interactive-cluster-name"
```

4. To deploy the code, you can run this script in your CI/CD pipeline
```bash
export DATABRICKS_HOST=<my_host>
export DATABRICKS_TOKEN=<my_service_principal_token>
databricks configure
dbx deploy awesome-etl --deployment-file=deployment.yml --environment=default
```
Take into account that the environment should be configured in your deployment.yml!