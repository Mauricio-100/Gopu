from setuptools import setup, find_packages

setup(
    name="gopu",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gopu = gopu.core:launch"
        ]
    },
    install_requires=[
        "flask",
        "psutil",
        "PyYAML"
    ],
    include_package_data=True,
    description="🧠 Module agentique pour GopuOS",
    author="Ceose",
)
