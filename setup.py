from setuptools import find_packages, setup

PACKAGE_NAME = "tx-recipes"
VERSION = "1.0.0"
AUTHOR = "textX"
DESCRIPTION = "textX extension for language recipes"
KEYWORDS = "textX DSL python domain specific languages workflow"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    keywords=KEYWORDS,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textX"],
    extras_require={
        "test": ["pytest"],
    },
    entry_points={
        "textx_languages": [
            "config = recipec:config_lang",
            "ingredient = recipec:ingredient_lang",
            "recipe = recipec:recipe_lang",
            "plan = recipec:plan_lang",
        ],
        "textx_generators": [
            "plan_gen = recipec.code_gen:plan_generator",
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
