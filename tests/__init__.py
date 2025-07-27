import contextlib
import sys
from collections.abc import Generator

import qt_themes
from qtpy import QtCore, QtWidgets


@contextlib.contextmanager
def application() -> Generator[QtCore.QCoreApplication]:
    theme = 'one_dark_two'
    if app := QtWidgets.QApplication.instance():
        qt_themes.set_theme(theme)
        yield app
        return

    app = QtWidgets.QApplication(sys.argv)
    qt_themes.set_theme(theme)
    yield app
    app.exec()
