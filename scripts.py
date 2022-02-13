import argparse
import yaml
import os
import jinja2
import logging
import shutil
import sys
from typing import Any

logging.basicConfig(
    format="[%(levelname)s][%(name)s][%(asctime)s]: %(message)s", level=logging.INFO
)

parser = argparse.ArgumentParser(
    prog="scripts",
    description="Runs scripts on the project",
    usage="%(prog)s ['dist','clean','build']",
)
parser.add_argument(
    "name",
    help="The name of the script to run",
)
args = parser.parse_args()


class Tasks:
    def _get_script_path(self):
        return os.path.dirname(os.path.realpath(sys.argv[0]))

    def _mkdocs(self, local: bool) -> bool:
        logging.info("\tRunning mkdocs")
        if local:
            if os.system(
                "poetry run mkdocs build --config-file ./mkdocs-local.yml --quiet --no-directory-urls"
            ) != 0:
                logging.error("Error running mkdocs")
                return False
        else:
            if os.system("poetry run mkdocs build --config-file ./mkdocs.yml --quiet --no-directory-urls") != 0:
                logging.error("Error running mkdocs")
                return False
        return True

    def _filterFile(self, filename: str, config: Any) -> bool:
        try:
            with open(filename, "r+") as currfile, open(
                filename.removesuffix(".tmpl"), "w+"
            ) as destiny:
                t = jinja2.Template("".join(currfile.readlines()))
                destiny.write(t.render(config=config))
            return True
        except BaseException:
            return False

    def _process(self, local: bool) -> bool:
        logging.info("\tFiltering the static files")
        filename = (
            os.path.join(self._get_script_path(), "./mkdocs-local.yml")
            if local
            else os.path.join(self._get_script_path(), "./mkdocs.yml")
        )
        try:
            with open(filename, "r+") as f:
                config = yaml.load(f, Loader=yaml.FullLoader)
                path = os.path.join(self._get_script_path(), "site")
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.endswith(".tmpl"):
                            logging.debug("Filtering file %s", file)
                            if not self._filterFile(os.path.join(root, file), config):
                                logging.warn(
                                    "Unable to filter file &s, continuing", file
                                )
            return True
        except BaseException as ex:
            logging.error("Error while filtering the files", exc_info=ex)
            return False

    def _copyStatic(self) -> bool:
        logging.info('\tCoping the static files')
        try:
            shutil.copytree(
                os.path.join(self._get_script_path(), "static"),
                os.path.join(self._get_script_path(), "site"),
                dirs_exist_ok=True,
                ignore_dangling_symlinks=True,
            )
            return True
        except shutil.Error as ex:
            logging.error("Error while copying the static files", exc_info=ex)
            return False

    def _copyDocs(self) -> bool:
        logging.info('\tCopying the documentation files')
        try:
            shutil.copytree(
                os.path.join(self._get_script_path(), "docs"),
                os.path.join(self._get_script_path(), "site"),
                dirs_exist_ok=True,
                ignore_dangling_symlinks=True,
            )
            return True
        except shutil.Error as ex:
            logging.error("Error while copying the documentation files", exc_info=ex)
            return False

    def build(self) -> bool:
        logging.info("Starting the build process:")
        if not self._copyStatic():
            return False
        if not self._process(False):
            return False
        if not self._copyDocs():
            return False
        if not self._mkdocs(False):
            return False
        logging.info("Finished the build process")
        return True

    def build_local(self) -> bool:
        logging.info("Starting the local build process:")
        if not self._copyStatic():
            return False
        if not self._process(True):
            return False
        if not self._copyDocs():
            return False
        if not self._mkdocs(True):
            return False
        logging.info("Finished the local build process")
        return True

    def clean(self) -> bool:
        logging.info("Starting the clean process")
        try:
            if os.path.exists(os.path.join(self._get_script_path(), "aux")):
                shutil.rmtree(os.path.join(self._get_script_path(), "aux"))
            if os.path.exists(os.path.join(self._get_script_path(), "site")):
                shutil.rmtree(os.path.join(self._get_script_path(), "site"))
            if os.path.exists(os.path.join(self._get_script_path(), "dist")):
                shutil.rmtree(os.path.join(self._get_script_path(), "dist"))
        except shutil.Error as ex:
            logging.error("Error while cleaning the directories", exc_info=ex)
            return False
        except FileNotFoundError:
            pass
        logging.info("Finished the clean process")
        return True

    def clean_local(self) -> bool:
        logging.info("Starting the local clean process")
        try:
            if os.path.exists(os.path.join(self._get_script_path(), "aux")):
                shutil.rmtree(os.path.join(self._get_script_path(), "aux"))
            if os.path.exists(os.path.join(self._get_script_path(), "site")):
                shutil.rmtree(os.path.join(self._get_script_path(), "site"))
            if os.path.exists("/home/carddamom/Web/wiki"):
                shutil.rmtree("/home/carddamom/Web/wiki", ignore_errors=False)
        except shutil.Error as ex:
            logging.error("Error while cleaning the directories", exc_info=ex)
            return False
        except FileNotFoundError:
            pass
        logging.info("Finished the local clean process")
        return True

    def dist(self) -> bool:
        logging.info("Starting the dist process:")
        if not self.clean():
            return False
        if not self.build():
            return False
        logging.info("Finished the dist process")
        return True

    def dist_local(self) -> bool:
        logging.info("Starting the local dist process:")
        if not self.clean_local():
            return False
        if not self.build_local():
            return False
        logging.info("Finished the local dist process")
        return True


tasks = Tasks()
match args.name:
    case "build":
        if not tasks.build():
            sys.exit(1)
        else:
            sys.exit(0)
    case "build:local":
        if not tasks.build_local():
            sys.exit(1)
        else:
            sys.exit(0)
    case "clean":
        if not tasks.clean():
            sys.exit(1)
        else:
            sys.exit(0)
    case "clean:local":
        if not tasks.clean_local():
            sys.exit(1)
        else:
            sys.exit(0)
    case "dist":
        if not tasks.dist():
            sys.exit(1)
        else:
            sys.exit(0)
    case "dist:local":
        if not tasks.dist_local():
            sys.exit(1)
        else:
            sys.exit(0)
    case _:
        pass
