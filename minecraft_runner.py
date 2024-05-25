# python pico runner
import argparse
from portablemc.standard import Version

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--release", type=str, default="release", help="Release of minecraft you want to play. Defaults to latest.")
args = parser.parse_args()

version = Version(args.release)
version.install().run()