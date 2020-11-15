"""A user lookup result."""


class LookupResult:
    """A user lookup result."""

    def __init__(
        self,
        service: str,
        result: str,
        *,
        reason: str = "",
        proof_url: str = "",
    ):
        """Create the base lookup result."""
        self.service = service
        self.result = result
        self.reason = reason
        self.proof_url = proof_url
