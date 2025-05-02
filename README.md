# ArcticDB ARM64 Linux Build

This repository contains pre-built wheel files for ArcticDB targeting Linux ARM64 architecture.

## Installation

### Using pip directly from git

```bash
# Install the latest version
pip install git+https://github.com/ribonred/arcticdb-arm.git

# Install a specific version/tag/commit
pip install git+https://github.com/ribonred/arcticdb-arm.git@v1.0.0
```

### Using uv directly from git

```bash
# Install the latest version
uv pip install git+https://github.com/ribonred/arcticdb-arm.git

# Install a specific version/tag/commit
uv pip install git+https://github.com/ribonred/arcticdb-arm.git@v1.0.0
```

### Automatic architecture-based installation with uv

Using uv's platform-specific sources feature, you can automatically install:
- The regular arcticdb from PyPI for AMD64 architectures
- This ARM64-specific version for ARM64 architectures

Add this to your pyproject.toml:

```toml
# Include arcticdb in your dependencies
[project]
dependencies = [
    "arcticdb",
]

# Tell uv which source to use based on architecture
[tool.uv.sources]
arcticdb = [
    # For ARM64, use the git repository
    { git = "https://github.com/ribonred/arcticdb-arm.git", marker = "platform_machine == 'aarch64' or platform_machine == 'arm64'" },
    # For AMD64, use PyPI (default)
    { index = "pypi", marker = "platform_machine == 'x86_64' or platform_machine == 'AMD64'" }
]
```

When using uv to install dependencies (`uv pip sync` or `uv pip install`), it will automatically select the right source based on your system's architecture.

## Supported Platforms

- Python 3.11
- Linux ARM64 architecture