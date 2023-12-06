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
    name='Bayesian-AB-Testing-Call-Tracking',
    version='0.1.0',
    packages=find_packages(include=['Bayesian-AB-Testing-Call-Tracking','Bayesian-AB-Testing-Call-Tracking.*']),
)
