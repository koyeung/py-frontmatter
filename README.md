# py-frontmatter

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
[![formatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Check](https://github.com/koyeung/py-frontmatter/actions/workflows/check.yml/badge.svg)](https://github.com/koyeung/py-frontmatter/actions/workflows/check.yml)

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

## License

`py-frontmatter` is distributed under the terms of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
