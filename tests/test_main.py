from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_mock.plugin import MockerFixture

import services_test


def test_entrypoint_calls_app(mocker: "MockerFixture") -> None:
    mocker.patch("services_test.cli.app")
    from services_test import __main__  # noqa: F401

    services_test.cli.app.assert_called_once_with(
        prog_name="services-test",
    )  # type: ignore[attr-defined]
