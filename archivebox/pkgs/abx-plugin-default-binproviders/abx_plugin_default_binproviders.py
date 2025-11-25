import abx
from pydantic import BaseModel
from typing import Dict
from abx_pkg import (
    AptProvider,
    BrewProvider,
    EnvProvider,
    BinProvider,
)

# Define BinProviderOverrides here
class BinProviderOverrides(BaseModel):
    # Add any fields that are required
    pass

# Set up the providers
apt = APT_BINPROVIDER = AptProvider()
brew = BREW_BINPROVIDER = BrewProvider()
env = ENV_BINPROVIDER = EnvProvider()

# Call setup methods
apt.setup()
brew.setup()
env.setup()

@abx.hookimpl(tryfirst=True)
def get_BINPROVIDERS() -> Dict[str, BinProvider]:
    return {
        'apt': APT_BINPROVIDER,
        'brew': BREW_BINPROVIDER,
        'env': ENV_BINPROVIDER,
    }
