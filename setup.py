import os
import sys
import shutil
import subprocess
import zipfile
from setuptools import setup, find_packages, Command
from pathlib import Path
import tomli
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

# Read pyproject.toml
with open("pyproject.toml", "rb") as f:
    pyproject = tomli.load(f)

PACKAGE_NAME = pyproject["project"]["name"]
VERSION = pyproject["project"]["version"]
ZIP_SOURCE_DIRS = [PACKAGE_NAME.replace("-", "_")]

app_dir = os.path.dirname(os.path.abspath(__file__))

class BdistSpark(Command):
    """ Forked from https://github.com/alekseyig/spark-submit-deps/blob/master/setup.py """

    description = "create deps and project distribution files for spark_submit"
    user_options = [
        ('requirement=', 'r', 'Install from the given requirements file. [default: requirements.txt]'),
        ('wheel-dir=', 'w', 'Build deps into dir. [default: spark_dist]'),
        ('build-deps=', 'b', 'Flag to zip dependencies from requirements file [default: False]'),
    ]

    def initialize_options(self):
        self.wheel_dir = os.path.join(app_dir, 'spark_dist')
        self.build_deps = False

        # Create a temporary requirements file from pyproject dependencies
        self.temp_dir = os.path.join(self.wheel_dir, '.temp')
        os.makedirs(self.temp_dir, exist_ok=True)
        self.requirements = os.path.join(self.temp_dir, 'requirements.txt')
        with open(self.requirements, 'w') as f:
            for dep in pyproject["project"]["dependencies"]:
                f.write(f"{dep}\n")

    def finalize_options(self):
        assert os.path.exists(self.requirements), (
            "requirements file '{}' does not exist.".format(self.requirements))

    @staticmethod
    def re_zip(z, dir_name, files):
        for f_name in files:
            full_fname = os.path.join(dir_name, f_name)
            with zipfile.ZipFile(full_fname, mode='r', compression=zipfile.ZIP_DEFLATED) as w:
                for file_info in w.filelist:
                    print("Adding %s to dependency zip archive" % file_info.filename)
                    z.writestr(file_info, w.read(file_info.filename))

    def zip_dependencies(self):
        print("running zip_dependencies")

        wheel_cmd = subprocess.check_output(["pip", "wheel", "-r", self.requirements, "-w", self.requirements]).splitlines(True)
        if wheel_cmd:
            dependencies_package = os.path.join(self.wheel_dir, '{}-{}-deps.zip'.format(PACKAGE_NAME, VERSION))
            with zipfile.ZipFile(dependencies_package, mode='w', compression=zipfile.ZIP_DEFLATED) as z:
                for dirname, _, files in os.walk(self.requirements):
                    self.re_zip(z, dirname, files)
        else:
            raise RuntimeError("Unable to package dependencies into dist dir.")
        
        # Clean up temporary directory
        shutil.rmtree(self.temp_dir)

    def zip_artifacts(self):
        print("running zip_artifacts")
        package_name = '{}/{}-{}.zip'.format(self.wheel_dir, PACKAGE_NAME, VERSION)

        with zipfile.ZipFile(package_name, mode='w', compression=zipfile.ZIP_DEFLATED) as z:
            for module in ZIP_SOURCE_DIRS:
                source = os.path.join(app_dir, module)
                for dir_name, _, f_names in os.walk(source):
                    for f_name in f_names:
                        if '.pyc' not in f_name:
                            path = os.path.join(dir_name, f_name)
                            dest = path.replace(app_dir + '/', '')
                            print("Adding %s to zip archive" % path)
                            z.write(path, dest)

    def run(self):
        # delete older wheel_dir if exists and create new
        if os.path.exists(self.wheel_dir):
            shutil.rmtree(self.wheel_dir)
        os.makedirs(self.wheel_dir)

        if self.build_deps:
            self.zip_dependencies()

        self.zip_artifacts()


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=pyproject["project"]["description"],
    author=pyproject["project"]["authors"][0]["name"],
    packages=find_packages(
        include=[PACKAGE_NAME.replace("-", "_")],
        exclude=['*.tests.*', '*.test_*']),
    package_dir={'': '.'},
    install_requires=pyproject["project"]["dependencies"],
    package_data={
        PACKAGE_NAME: ['*.py']
    },
    cmdclass={
        "bdist_spark": BdistSpark
    },
    url='https://git.amobee.com/data-science/cleanroom-ml',
)
