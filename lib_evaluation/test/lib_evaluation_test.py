import pytest

from lib_evaluation import lib_a


def test_get_df__returns_df_on_call():

    result = lib_a.get_df()

    assert result.column.to_list() == ["timestamp", "lat", "long"]
