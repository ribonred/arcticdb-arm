"""
ArcticDB package for Linux ARM64
"""

# Import the installed wheel package
try:
    from arcticdb import *
except ImportError:
    import os
    import sys
    import subprocess
    import pkg_resources
    import warnings
    
    # Path to the wheel file
    here = os.path.abspath(os.path.dirname(__file__))
    wheel_path = os.path.join(os.path.dirname(here), "dist", "arcticdb-0.0.0.dev0-cp311-cp311-linux_aarch64.whl")
    
    if os.path.exists(wheel_path):
        # Check if we're on the right platform
        is_linux = sys.platform.startswith('linux')
        is_arm64 = 'aarch64' in os.uname().machine if is_linux else False
        
        if not (is_linux and is_arm64):
            warnings.warn(f"This package is built for Linux ARM64, but you're running on {sys.platform}")
        
        # Install the wheel
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", wheel_path])
            # Try importing again after installation
            from arcticdb import *
        except Exception as e:
            warnings.warn(f"Failed to install ArcticDB wheel: {e}")
    else:
        warnings.warn(f"Wheel file not found at {wheel_path}")