from __future__ import annotations

from typing import Any

import wrapt


class MatcherProxy(wrapt.ObjectProxy):
    """Override a matcher instance's ``__call__`` method."""

    def __call__(self, expected: Any = ...):
        results = self.__wrapped__.__call__(expected=expected)

        assert results, self.message().render(
            self._expectation.actual,
            expected=expected,
        )

        self._expectation.qualifiers.clear()
