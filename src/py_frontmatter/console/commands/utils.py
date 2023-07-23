# SPDX-FileCopyrightText: 2023-present YEUNG King On <koyeung@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0
from typing import TextIO

from py_frontmatter.core import Document, dump_document


def overwrite_file(*, file: TextIO, document: Document) -> None:
    # reset current position before calling truncate
    file.seek(0)
    file.truncate()

    dump_document(document, file)
