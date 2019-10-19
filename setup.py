from setuptools import setup, find_packages

setup(name='cheeseApplication', version='1.0', packages=find_packages(), install_requires=['click', 'click_repl',
                                                                                           'prompt_toolkit'])