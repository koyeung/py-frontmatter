# py-frontmatter
To manipulate front matter in document file.

## Installation

```shell
pip install py-frontmatter
```

## Usage

```
% cat note.md 
---
title: Hacker's note
tags: [a, b]
---
# header
text
```

To retrieve front matter as JSON:
```
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
```
% echo '{"title": "My note", "tags": ["a", "b", "c"]}' | frontmatter set note.md 
% cat ~/today/note.md 
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
