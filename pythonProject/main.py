from PyQt5.QtWidgets import QApplication
import MainWindow as main
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''

        ''')
    main_window = main.MainWindow()
    main_window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing Windows...")
