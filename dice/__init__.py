"""Package for Dice cog."""
import asyncio
import json
from pathlib import Path

from redbot.core.bot import Red

from .dice import Dice

with open(Path(__file__).parent / "info.json") as fp:
    __red_end_user_data_statement__ = json.load(fp)["end_user_data_statement"]


async def setup(bot: Red) -> None:
    """Load Dice cog."""
    if asyncio.iscoroutinefunction(bot.add_cog):
            await bot.add_cog(Dice(bot))
    else:
        bot.add_cog(Dice(bot))
