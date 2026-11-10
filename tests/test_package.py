"""Smoke tests confirming the package and its modules import correctly."""

import importlib

import pytest

import decision_tree

MODULES = ["impurity", "splitter", "node", "tree", "forest", "viz"]


def test_version_is_defined() -> None:
    assert isinstance(decision_tree.__version__, str)
    assert decision_tree.__version__.count(".") == 2


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module: str) -> None:
    assert importlib.import_module(f"decision_tree.{module}") is not None
