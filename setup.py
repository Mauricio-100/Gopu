from setuptools import setup, find_packages

setup(
    name="gopu",
    version="1.0.0",
    description="Agentic CLI for GopuOS — introspection, deployment, and cloud orchestration",
    author="Ceose",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "PyYAML"
    ],
    entry_points={
        "console_scripts": [
            "gopu = gopu:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Topic :: System :: Shells",
        "Topic :: Utilities"
    ],
    python_requires=">=3.8"
)
