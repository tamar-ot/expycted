from expycted import expect
from expycted.matchers import BeEmptyMatcher

from helpers import stubs
from helpers.utils import parametrize_expectation


def test_via_expect(context):
    expectation = expect([])

    assert isinstance(expectation.to.be_empty, BeEmptyMatcher)

    expectation.to.be_empty()

    with context.raises:
        expectation.to_not.be_empty()


@parametrize_expectation(
    [
        stubs.EMPTY_LIST(),
        stubs.EMPTY_DICT(),
        stubs.EMPTY_SET(),
        stubs.EMPTY_TUPLE(),
        stubs.EMPTY_STRING(),
        stubs.EMPTY_BSTRING(),
        stubs.EMPTY_RANGE(),
        stubs.EMPTY_GENERATOR(),
    ],
    matcher=BeEmptyMatcher,
)
def test_matches(expectation):
    matcher = expectation.matcher()

    assert matcher() is True


@parametrize_expectation(
    [
        stubs.NOT_EMPTY_LIST(),
        stubs.NOT_EMPTY_DICT(),
        stubs.NOT_EMPTY_SET(),
        stubs.NOT_EMPTY_TUPLE(),
        stubs.NOT_EMPTY_STRING(),
        stubs.NOT_EMPTY_BSTRING(),
        stubs.NOT_EMPTY_RANGE(),
        stubs.NOT_EMPTY_GENERATOR(),
    ],
    matcher=BeEmptyMatcher,
)
def test_not_matches(expectation):
    matcher = expectation.matcher()

    assert matcher() is False


@parametrize_expectation(
    [
        stubs.ZERO(),
        stubs.INT(),
        stubs.FLOAT(),
        stubs.FUNCTION_BUILT(),
        stubs.SINGLETON_OBJECT(),
        True,  # @TODO: use stub
    ],
    matcher=BeEmptyMatcher,
    wrap=True,
)
def test_type_error(expectation, context):
    matcher = expectation.matcher()

    with context.type_error:
        matcher()
