from setuptools import setup, find_packages


requirements = [
    "pyspark>=3.0.0"
]
setup_requirements = ["pytest-runner"]
tests_requirements = ["pytest>=5.4.1"]
dev_requirements = [
    "pre-commit>=2.19.0",
    "flake8>=4.0.0",
    "black>=22.3.0",
    "bump2version",
] + tests_requirements
extras_requirements = {"dev": dev_requirements}
setup(
    name="example_pyspark",
    version="0.1",
    description="Example pyspark package",
    # Author details
    author="Guillermo Sanchez",
    author_email="guillermosanchez@godatadriven.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=tests_requirements,
    extras_require=extras_requirements,
)