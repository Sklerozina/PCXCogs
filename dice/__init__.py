"""Package for Dice cog."""
import asyncio
from .dice import Dice


async def setup(bot):
    """Load Dice cog."""
    if asyncio.iscoroutinefunction(bot.add_cog):
            await bot.add_cog(Dice(bot))
    else:
        bot.add_cog(Dice(bot))
