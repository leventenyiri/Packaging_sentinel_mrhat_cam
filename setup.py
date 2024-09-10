from setuptools import setup, find_packages

setup(
    name='sentinel_mrhat_cam',
    version='1.1.1',
    description='Testing python code for Starling detection project',
    author='Ferenc Nandor Janky, Attila Gombos, Nyiri Levente, Nyitrai Bence',
    author_email='info@effective-range.com',
    packages=find_packages(),
    scripts=['scripts/sentinel_mrhat_cam.sh', 'scripts/daemon.sh'],
    install_requires=['pytest',
                      'PyYAML>=6.0',
                      'pillow',
                      'pytz',
                      'paho-mqtt',
                      'numpy',
                      'pybase64',
                      'pdocs']
)
