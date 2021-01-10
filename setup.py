from setuptools import setup

setup(
    name="euler",
    version="1.0",
    py_modules=["euler", "commands"],
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        euler=euler:cli
        """,
)
