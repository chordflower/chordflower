import argparse
import yaml
import os
import jinja2
import logging

logging.basicConfig(
    format="[%(levelname)s][%(name)s][%(asctime)s]: %(message)s", level=logging.INFO
)

parser = argparse.ArgumentParser(
    prog="scripts",
    description="Runs scripts on the project",
    usage="%(prog)s ['process','process-local','build','build-local']",
)
parser.add_argument(
    "name", choices=["process", "process-local", "build", "build-local", "build-my-local"],
    help="The name of the script to run"
)
args = parser.parse_args()


def filterFile(filename: str, config: any) -> None:
    with open(filename, "r+") as currfile:
        destiny = open(filename.removesuffix(".tmpl"), "w+")
        t = jinja2.Template("".join(currfile.readlines()))
        destiny.write(t.render(config=config))


def process() -> None:
    logging.info("Doing the process script")
    with open("./mkdocs.yml", "r+") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        logging.debug("config is: %s", config)
        path = os.path.join(os.getcwd(), "docs")
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".tmpl"):
                    logging.debug("Filtering file %s", file)
                    filterFile(os.path.join(root, file), config)


def processLocal():
    logging.info("Doing the process script")
    with open("./mkdocs-local.yml", "r+") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        logging.debug("config is: %s", config)
        path = os.path.join(os.getcwd(), "docs")
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".tmpl"):
                    logging.debug("Filtering file %s", file)
                    filterFile(os.path.join(root, file), config)


def mkdocs(local: bool, command: str) -> None:
    logging.info("Running mkdocs")
    if local:
        os.system("poetry run mkdocs {} --config-file ./mkdocs-local.yml".format(command))
    else:
        os.system("poetry run mkdocs {}".format(command))


match args.name:
    case "process":
        process()
    case "process-local":
        processLocal()
    case "build":
        process()
        mkdocs(False, "build")
    case "build-local":
        processLocal()
        mkdocs(True, "build")
    case "build-my-local":
        processLocal()
        mkdocs(True, "build -d /home/carddamom/Web/wiki")
    case _:
        pass
