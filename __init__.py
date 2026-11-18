"""Doubleword provider profile."""

from providers import register_provider
from providers.base import ProviderProfile

doubleword = ProviderProfile(
    name="doubleword",
    aliases=("doubleword-ai", "dw"),
    display_name="Doubleword",
    description="Open models (GLM, Kimi, DeepSeek, Qwen)",
    signup_url="https://app.doubleword.ai",
    env_vars=("DOUBLEWORD_API_KEY", "DOUBLEWORD_BASE_URL"),
    base_url="https://api.doubleword.ai/v1",
    auth_type="api_key",
    default_aux_model="zai-org/GLM-5.3-Flash",
    fallback_models=(
        "zai-org/GLM-5.3",
        "moonshotai/Kimi-K3.1-Pro",
        "deepseek-ai/DeepSeek-V4.1-Flash",
        "deepseek-ai/DeepSeek-V4-Pro-0813",
        "zai-org/GLM-5.3-Flash",
    ),
)

register_provider(doubleword)
