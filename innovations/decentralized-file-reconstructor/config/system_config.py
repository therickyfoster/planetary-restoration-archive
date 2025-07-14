# config/system_config.py
# Centralized runtime constants for AI-driven file reconstruction

# Maximum RAM (in MB) that the system is allowed to use for buffering
RAM_CAP_MB = 512  # Default: 512MB for safety on low-resource devices

# Chunk size in bytes (should align with IPFS offload size and agent constraints)
DEFAULT_CHUNK_SIZE = 5 * 1024 * 1024  # 5MB per chunk

# Max number of active AI agents in parallel (for swarming setups)
MAX_ACTIVE_AGENTS = 4

# Timeouts and retries
CHUNK_FETCH_TIMEOUT = 10     # seconds
CHUNK_FETCH_RETRIES = 3

# Fallback strategy
ENABLE_AGENT_FALLBACK = True

# File reassembly logic toggle
AUTO_STITCH_RECONSTRUCTION = False

# Default AI agent model versions (editable for benchmarking)
DEFAULT_VICUNA_MODEL = "vicuna-7b"
DEFAULT_DIFFUSION_MODEL = "sd-1.5"
DEFAULT_T5_MODEL = "t5-base"

# Gateway cycling behavior
ROTATE_GATEWAYS = True
