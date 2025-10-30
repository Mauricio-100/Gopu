#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# setup.py — GopuOS: minimal, agentic, and dependency‑free CLI packaging
# Focus: zero external deps, clean console entrypoint, INI‑based config

from setuptools import setup, find_packages
from pathlib import Path

ROOT = Path(__file__).parent
README = (ROOT / "README.md").read_text(encoding="utf-8")

setup(
    # Identity
    name="gopu",
    version="0.1.0",
    description="GopuOS — Agentic CLI for deployment, Git, and inference (pure stdlib).",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Ceose",
    url="https://github.com/Mauricio-100/Gopu",

    # Packaging
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",

    # Zero external dependencies — pure stdlib (configparser, json, subprocess)
    install_requires=[],

    # Entry points: `gopu` routes to your Python CLI
    entry_points={
        "console_scripts": [
            "gopu = gopu.cli:main",
        ],
    },

    # Classifiers for clarity
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],

    # Optional metadata
    keywords=["agentic", "cli", "gopu", "deployment", "git", "inference", "stdlib"],
)
