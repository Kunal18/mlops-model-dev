from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    params_n_estimators: int
    params_learning_rate: float
    params_random_state: int
    params_subsample: float
    params_n_jobs: int
    params_max_depth: int
    
    
    
