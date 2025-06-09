from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field
from pydantic_pkgr import NpmProvider, PATHStr, BinProviderName
from archivebox.config import DATA_DIR, CONSTANTS
from abbx.archivebox.base_binary import BaseBinProvider

OLD_NODE_BIN_PATH = DATA_DIR / 'node_modules' / '.bin'
NEW_NODE_BIN_PATH = CONSTANTS.DEFAULT_LIB_DIR / 'npm' / 'node_modules' / '.bin'

class BinProviderOverrides(BaseModel):
    some_field: str = Field(default="default_value")

class SystemNpmBinProvider(NpmProvider, BaseBinProvider):
    name: BinProviderName = "sys_npm"
    npm_prefix: Optional[Path] = None
    # overrides: BinProviderOverrides = BinProviderOverrides()

# Call model_rebuild to finalize the model
SystemNpmBinProvider.model_rebuild()

class LibNpmBinProvider(NpmProvider, BaseBinProvider):
    name: BinProviderName = "lib_npm"
    PATH: PATHStr = f'{NEW_NODE_BIN_PATH}:{OLD_NODE_BIN_PATH}'
    npm_prefix: Optional[Path] = CONSTANTS.DEFAULT_LIB_DIR / 'npm'
    # overrides: BinProviderOverrides = BinProviderOverrides()

    def setup(self) -> None:
        from archivebox.config.common import STORAGE_CONFIG
        if STORAGE_CONFIG.LIB_DIR != CONSTANTS.DEFAULT_LIB_DIR:
            self.npm_prefix = STORAGE_CONFIG.LIB_DIR / 'npm'
            self.PATH = f'{STORAGE_CONFIG.LIB_DIR / "npm" / "node_modules" / ".bin"}:{NEW_NODE_BIN_PATH}:{OLD_NODE_BIN_PATH}'
        super().setup()

# Call model_rebuild to finalize the model
LibNpmBinProvider.model_rebuild()

# Create instances
SYS_NPM_BINPROVIDER = SystemNpmBinProvider()
LIB_NPM_BINPROVIDER = LibNpmBinProvider()
npm = LIB_NPM_BINPROVIDER
