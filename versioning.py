"""
Get the version number of Qurry and versioning the documentation.
"""

import datetime
import subprocess

from qurry import __version__


if __name__ == "__main__":
    CURRENT_DATE_STRING = datetime.datetime.now().strftime("%Y%m%d")
    STABLE_VERSION = ".".join(__version__.split(".")[:3])
    TAG_CHECK = STABLE_VERSION + "*"

    print(f"| Current Qurry version: {__version__}")
    print(f"| Current date string: {CURRENT_DATE_STRING}")
    print(f"| Tagging check by: {TAG_CHECK}")
    LABELS = subprocess.check_output(["git", "tag", "-l", TAG_CHECK]).strip()
    LABELS = LABELS.decode("utf-8")
    LABEL_NUM = 0 if LABELS == "" else len(LABELS.split("\n"))

    VERSION = STABLE_VERSION + f"rc{LABEL_NUM + 1}"

    print(f"| CURRENT_DATE_STRING: {CURRENT_DATE_STRING}, label_num: {LABEL_NUM}")
    print(f"| Version: {VERSION}")
    print(f"| Release candidate: {LABEL_NUM + 1}")
    subprocess.run(
        ["git", "tag", "-a", VERSION, "-m", f"chore: Release candidate {VERSION}"],
        check=True,
    )
    subprocess.run(["git", "push", "origin", VERSION], check=True)

    print("| Versioning complete.")
