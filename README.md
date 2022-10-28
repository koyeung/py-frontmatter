# py-frontmatter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![formatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/koyeung/py-frontmatter/main.svg)](https://results.pre-commit.ci/latest/github/koyeung/py-frontmatter/main)

To manipulate front matter in document file.

## Installation

```shell
pip install py-frontmatter
```

## Usage

Given text file:
```markdown
---
title: Hacker's note
tags: [a, b]
---
# header
text
```

### Get or set whole section of front matter

To retrieve front matter as JSON:
```commandline
% frontmatter get note.md | jq
{
  "title": "Hacker's note",
  "tags": [
    "a",
    "b"
  ]
}
```

To replace the front matter:
```commandline
% echo '{"title": "My note", "tags": ["a", "b", "c"]}' | frontmatter set note.md
% cat note.md
---
title: My note
tags:
- a
- b
- c
---
# header
text
```

### Add or remove item from front matter

```commandline
% frontmatter add-item --jsonpath '$.tags' --item d note.md
% cat note.md
---
title: My note
tags:
- a
- b
- c
- d
---
# header
text
%
% frontmatter remove-item --jsonpath '$.tags' --item d note.md
% cat note.md
---
title: My note
tags:
- a
- b
- c
---
# header
text
```

### Specialize commands to add/remove tag

```commandline
% frontmatter add-tag --tag d note.md
% cat note.md
---
title: My note
tags:
- a
- b
- c
- d
---
# header
text
% frontmatter remove-tag --tag d note.md
% cat note.md
---
title: My note
tags:
- a
- b
- c
---
# header
text
```
