from setuptools import setup, find_packages

setup(
    name='sentinel_mrhat_cam',
    version='1.1.6',
    description='Testing python code for Starling detection project',
    author='Ferenc Nandor Janky, Attila Gombos, Nyiri Levente, Nyitrai Bence',
    author_email='info@effective-range.com',
    packages=find_packages(),
    scripts=['scripts/sentinel_mrhat_cam.sh', 'scripts/sentinel_mrhat_cam_main.py'],
    data_files=[('config', ['config/config.json', 'config/log_config.yaml'])],
    install_requires=['picamera2', 'PyYAML>=6.0', 'pillow', 'pytz', 'paho-mqtt', 'numpy'],
)
