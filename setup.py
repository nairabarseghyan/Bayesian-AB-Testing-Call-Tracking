from setuptools import setup, find_packages

setup(
    author="""Anush Aghinyan, 
                Anahit Navoyan, 
                Yeva Avetisyan, 
                Naira Maria Barseghyan, 
                Mher Movsisyan""",
    author_email="""anush_aghinyan@edu.aua.am, 
                    anahit_navoyan@edu.aua.am,
                    yeva_avetisyan@edu.aua.am,
                    naira_barseghyan@edu.aua.am,
                    mher_movsisyan@edu.aua.am,
                    """,
    description='AB testing tool, designed for testing data of call tracking services',
    name='Bayesian-AB-Testing-Call-Tracking',
    version='0.1.0',
    packages=find_packages(include=['Bayesian-AB-Testing-Call-Tracking','Bayesian-AB-Testing-Call-Tracking.*']),
    
)
