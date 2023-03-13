from setuptools import setup

setup(
    packages=[
        'cubapy',
    ],
    data_files=[('licenses', ['MIT']), ('README', ['README.md'])],
    install_requires=[
        'numpy',
        'plotly'
    ]
)
