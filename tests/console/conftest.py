# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
import sys
from importlib.metadata import entry_points
from pathlib import Path
from unittest.mock import patch

import pytest


@pytest.fixture
def sample(tmp_path: Path) -> Path:
    full_content = """\
---
title: Hacker's note
tags: [a, b]
---
# header
text
"""

    sample_file = tmp_path / "sample.md"
    with sample_file.open(mode="w") as file_:
        file_.write(full_content)

    return sample_file


@pytest.fixture
def sample_wo_tags(tmp_path: Path) -> Path:
    full_content = """\
---
title: Hacker's note
---
# header
text
"""

    sample_file = tmp_path / "sample.md"
    with sample_file.open(mode="w") as file_:
        file_.write(full_content)

    return sample_file


def run_console_script(name, *args):
    entry_point, *_ = entry_points(group="console_scripts", name=name)
    func = entry_point.load()

    with patch.object(sys, "argv", [name, *args]):
        return func()
