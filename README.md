# Mass File Renamer Tool (MFRT)

A small CLI for bulk-renaming files in a directory using a simple naming convention.
It was built as a minimal, easy-to-read example using Click and standard library modules. I made this tool to gain more experience with python projects and CLI development.

## Features

- Rename all files (non-recursive) in a target directory
- Simple naming convention: base name + incremental index + original extension
- Small, dependency-light: depends only on `click`

## Requirements

- Python 3.8+
- `pip` to install dependencies

## Installation (developer)

From the project root, install in editable mode so you can modify the code and test quickly:

PowerShell
```
pip install -e .
```

Or install normally:

PowerShell
```
pip install .
```

## Usage

The package installs a `mfrt` console script. Run `mfrt --help` to see options.

PowerShell
```
mfrt --help
```

Basic options:

- `--path`: directory containing files to rename (default: current directory)
- `--nameconvention`: base name to use for renamed files (default: `file`)

### Examples

Rename files in the current directory using the default convention:

PowerShell
```
mfrt
```

Rename files in a specific directory with a custom base name:

PowerShell
```
mfrt --path C:\Users\you\Downloads --nameconvention holiday
```

Files in the directory will be renamed to `holiday_1.ext`, `holiday_2.ext`, etc., preserving original extensions. The tool only renames regular files in the specified directory and does not recurse into subdirectories.

### Safety notes

- There is currently no "dry-run" or undo built-in. Test on a copy of files or a sample directory first.
- Filenames that collide with generated names may be overwritten.

## Development notes

- The CLI entry point is defined at `mfrt.cli:main` (see `setup.py` entry points).
- Source lives in the `mfrt/` package. If you change code, reinstall with `pip install -e .`.

## Contributions & Improvements

This is a small project so feel free to open issues or PRs to add features such as:

- dry-run mode
- preview and confirmation step
- conflict-handling policies (skip, rename, backup)
- recursive mode and filters by extension or pattern

