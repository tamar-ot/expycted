from __future__ import annotations

from typing import Any, Collection, Tuple, Type
import pickle

from expycted.core.matchers import assertion
from expycted.internals.base import BaseExpectation
from expycted.internals.utils import assertion as assertion_old
from expycted.matchers import (
    BeEmptyMatcher,
    ContainedInMatcher,
    EqualMatcher,
    GreatThanMatcher,
    InheritMatcher,
    IsFalseMatcher,
    IsTrueMatcher,
    LessThanMatcher,
    NumericMatcher,
    TypeMatcher,
)


class Value(BaseExpectation):
    _ASSERTION_MESSAGES = {
        "be": "Expected {expected} to be {actual}",
        "contain": "Expected {expected} to contain {actual}",
    }

    def _internal_be(self, actual: Any) -> Tuple[bool, str]:
        return any(
            [
                str(self._actual) == str(actual),
                pickle.dumps(self._actual) == pickle.dumps(actual),
                self._actual == actual,
            ]
        ), self._message("be", actual)

    def _internal_contain(self, expected: Any) -> Tuple[bool, str]:
        try:
            return expected in self._actual, self._message("contain", expected)
        except Exception:
            raise AssertionError(
                f'Type "{type(self._actual)} cannot contain {expected}"'
            )

    @property
    @assertion
    def equal(self) -> Type[EqualMatcher]:
        """Asserts that two variables have the same value."""

        return EqualMatcher

    @property
    def be_equal_to(self) -> EqualMatcher:
        """Alias for ``equal``."""

        return self.equal

    @assertion_old
    def be(self, actual: Any) -> None:
        """Checks whether the value is 'softly' equal to something."""

    @assertion_old
    def contain(self, actual: Any) -> None:
        """Checks whether the value contains something."""

    @property
    @assertion
    def be_empty(self) -> Type[BeEmptyMatcher]:
        """Asserts that the actual value is empty."""

        return BeEmptyMatcher

    @property
    @assertion
    def be_true(self) -> Type[IsTrueMatcher]:
        """Asserts that the actual value is ``True``."""

        return IsTrueMatcher

    @property
    @assertion
    def be_false(self) -> Type[IsFalseMatcher]:
        """Asserts that the actual value is ``False``."""

        return IsFalseMatcher

    @property
    @assertion
    def be_truthy(self) -> IsTrueMatcher:
        """Asserts that the actual value is truthy."""

        return IsTrueMatcher(self, strict=False)

    @property
    def be_trueish(self) -> IsTrueMatcher:
        """Alias for ``be_truthy``."""

        return self.be_truthy

    @property
    def be_truey(self) -> IsTrueMatcher:
        """Alias for ``be_truthy``."""

        return self.be_truthy

    @property
    @assertion
    def be_falsey(self) -> IsFalseMatcher:
        """Asserts that the actual value is falsey."""

        return IsFalseMatcher(self, strict=False)

    @property
    def be_falsish(self) -> IsFalseMatcher:
        """Alias for ``be_falsey``."""

        return self.be_falsey

    @property
    def be_falsy(self) -> IsFalseMatcher:
        """Alias for ``be_falsey``."""

        return self.be_falsey

    @property
    @assertion
    def be_of_type(self) -> Type[TypeMatcher]:
        """Assert that the actual type is equivalent to the expected type."""

        return TypeMatcher

    @property
    def be_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

        return self.be_of_type

    @property
    def have_type(self) -> TypeMatcher:
        """Alias for ``be_of_type``."""

        return self.be_of_type

    @property
    @assertion
    def be_greater_than(self) -> Type[GreatThanMatcher]:
        """Asserts that the actual value is greater than the expected value."""

        return GreatThanMatcher

    @property
    def be_greater(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than``."""

        return self.be_greater_than

    @property
    @assertion
    def be_greater_than_or_equal_to(self) -> GreatThanMatcher:
        """Asserts the actual value is greater than or equal to the expected value."""

        return GreatThanMatcher(self, or_equal=True)

    @property
    def be_greater_or_equal_to(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    def be_greater_or_equal(self) -> GreatThanMatcher:
        """Alias for ``be_greater_than_or_equal_to``."""

        return self.be_greater_than_or_equal_to

    @property
    @assertion
    def be_lesser_than(self) -> Type[LessThanMatcher]:
        """Asserts that the actual value is lesser than the expected value."""

        return LessThanMatcher

    @property
    @assertion
    def be_lesser_than_or_equal_to(self) -> LessThanMatcher:
        """Asserts that the actual value is less than or equal to the expected value."""

        return LessThanMatcher(self, or_equal=True)

    @property
    def be_less_than(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_less(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_lesser(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than``."""

        return self.be_lesser_than

    @property
    def be_lesser_or_equal_to(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_less_than_or_equal_to(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_less_or_equal(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    def be_lesser_or_equal(self) -> LessThanMatcher:
        """Alias for ``be_lesser_than_or_equal_to``."""

        return self.be_lesser_than_or_equal_to

    @property
    @assertion
    def be_numeric(self) -> Type[NumericMatcher]:
        """Asserts that the value is numeric."""
        return NumericMatcher

    @property
    def be_a_number(self) -> NumericMatcher:
        """Alias for ``be_numeric``."""
        return self.be_numeric

    @property
    @assertion
    def be_contained_in(self) -> Type[ContainedInMatcher]:
        """Assert that the actual value is contained in the expected value."""
        return ContainedInMatcher

    @property
    def be_in(self) -> ContainedInMatcher:
        """Alias for ``be_contained_in``."""
        return self.be_contained_in

    @property
    def be_included_in(self) -> ContainedInMatcher:
        """Alias for ``be_contained_in``."""
        return self.be_contained_in

    @property
    @assertion
    def inherit(self) -> Type[InheritMatcher]:
        """Assert that the actual value inherit from expected value."""
        return InheritMatcher

    @property
    def have_parent(self) -> InheritMatcher:
        """Alias for ``inherit``."""
        return self.inherit

    @property
    def be_subclass_of(self) -> InheritMatcher:
        """Alias for ``inherit``."""
        return self.inherit

    # Aliases

    has = have = include = contain
