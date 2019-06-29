from setuptools import setup, find_packages

setup(
    name='retentioneering',
    version='0.4.1',
    license='Mozilla Public License',
    description='Python package for user trajectories analysis in the app',
    long_description='Python package for user trajectories analysis in the app',
    author='Retentioneering User Trajectory Analysis Lab',
    author_email='maxim.godzi@gmail.com',
    url='',
    keywords=['ANALYTICS', 'CLICKSTREAM', 'RETENTIONEERING', 'RETENTION', 'GRAPHS', 'TRAJECTORIES'],
    install_requires=[
        'pandas>=0.24.2',
        'numpy>=1.16.1',
        'networkx>=2.3',
        'seaborn>=0.9.0',
        'scikit-learn>=0.20.2',
        'shap>=0.29.1',
        'eli5>=0.8.2',
    ],
    classifiers=[
        'Development Status :: 4 - Beta'
    ],
    packages=find_packages()
)