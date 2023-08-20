from PyQt5.QtWidgets import QWidget, QGridLayout, QLayout


# "Interface" for interacting with layout of widget
class MyWidgetWithLayout:
    # Placement of single child widget
    def place(self, widget, row: int = 0, column: int = 0, rowSpan: int = 1, columnSpan: int = 1):
        if isinstance(self.layout(), QLayout):
            # Grid layout
            if type(self.layout()) is QGridLayout:
                if (row > 0) and (column > 0):
                    self.layout().addWidget(widget, row, column, rowSpan, columnSpan)
            # VBox/HBox layout
            else:
                self.layout().addWidget(widget)

    # Placement of multiple child widgets
    def placeAll(self, *widgets):
        for widget in widgets:
            self.place(widget)

    # Removal of default margins
    def removeLayoutMargins(self: QWidget):
        self.layout().setContentsMargins(0, 0, 0, 0)
