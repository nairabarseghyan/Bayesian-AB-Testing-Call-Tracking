from setuptools import setup, find_packages

setup(
    author="""Anush Aghinyan, 
                Anahit Navoyan, 
                Yeva Avetisyan, 
                Naira Maria Barseghyan, 
                Mher Movsisyan""",
    author_email="""mher@movsisyan.info""", # needed to change this because of 
            # ERROR    HTTPError: 400 Bad Request from https://upload.pypi.org/legacy/
            #  'anush_aghinyan@edu.aua.am, ana...m, mher_movsisyan@edu.aua.am, ' is an invalid value for Author-email. Error: Use a valid email address See
            #  https://packaging.python.org/specifications/core-metadata for more information.
    description='AB testing tool, designed for testing data of call tracking services',
    name='bayesian_ab_testing',
    version='1.0.0',
    packages=find_packages(include=['bayesian_ab_testing','bayesian_ab_testing.*']),
    long_description="""# Bayesian AB Testing  \n\nAB testing tool, designed for testing data of call tracking services\n""",
    long_description_content_type='text/markdown',
    python_requires=">=3.11",
    install_requires=open("requirements.txt", "r").read().split("\n")
)
