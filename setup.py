import setuptools

setuptools.setup(
	name='poll_bot',
	version='0.2.0',
	url='https://github.com/bmintz/poll-bot',

	author='Benjamin Mintz',
	author_email='bmintz@protonmail.com',

	description='A simple reaction-based Discord poll bot',
	long_description=open('README.rst').read(),

	packages=setuptools.find_packages(),

	install_requires=['discord.py'],

	classifiers=[
		'Development Status :: 2 - Pre-Alpha',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3.5',
	],
)
