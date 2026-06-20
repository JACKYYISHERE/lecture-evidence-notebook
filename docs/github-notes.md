# GitHub Publishing Notes

## What Is Safe To Publish

Safe:

- tool scripts,
- schemas,
- blank templates,
- synthetic examples,
- workflow documentation,
- installation instructions.

Usually unsafe:

- course recordings,
- Zoom transcripts,
- PDFs/slides from paid courses,
- screenshots of professor slides,
- student names,
- platform links with access tokens,
- downloaded Smart Summary content if it contains course material.

## Recommended Repository Settings

For public GitHub:

- keep only tool code and templates,
- use synthetic examples,
- keep `.gitignore` strict,
- do not include real lecture screenshots.

For private GitHub:

- still avoid uploading large recordings,
- still check course copyright rules,
- consider Git LFS only if you truly need media versioning,
- avoid committing signed Zoom URLs.

## Before First Commit

Run:

```bash
git status --short
git check-ignore -v path/to/private/file
```

Check that these are ignored:

```text
*.mp4
*.m4a
*.vtt
*.pdf
local_bundles/
frames/
```

## Suggested Repo Description

```text
Local-first lecture evidence notebook: sync recordings, transcripts, slides, and classroom annotations into exam-ready study notes.
```

