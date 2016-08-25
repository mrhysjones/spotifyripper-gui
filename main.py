from PyQt4 import QtGui
import design
import spotify_tools
import sys

class RipperApp(QtGui.QMainWindow, design.Ui_mainWindow):
    
    
    def __init__(self, parent=None):
        super(RipperApp, self).__init__(parent)
        self.setupUi(self)
        self.results.setSortingEnabled(True)
        self.search_button.clicked.connect(self.search)
        self.download_all_songs_button.clicked.connect(self.download_all_songs)
        
    def download_song(self):
        button = self.sender()
        index = self.results.indexAt(button.pos())
        if index.isValid():
            uri = str(self.results.item(index.row(), 0).text())
            spotify_tools.download_track(uri)
            

    def download_all_songs(self):
        for x in range(0, self.results.rowCount()):
            uri = str(self.results.item(index.row(), 0).text())
                   
    def search(self):
        search_term = str(self.search_bar.text())
        if len(search_term) > 0:
            spot_results = spotify_tools.keyword_search(search_term)
            self.results.setRowCount(len(spot_results.tracks))

            for x in range(0, len(spot_results.tracks)):
                track = spot_results.tracks[x]
                uri = str(track)[8
                                 :-2]
                self.results.setItem(x, 0, QtGui.QTableWidgetItem(uri))
                self.results.setItem(x, 1, QtGui.QTableWidgetItem(track.name))
                self.results.setItem(x, 2, QtGui.QTableWidgetItem(track.artists[0].name))
                self.results.setItem(x, 3, QtGui.QTableWidgetItem(track.album.name))
                self.results.setItem(x, 4, QtGui.QTableWidgetItem(spotify_tools.duration_string(track.duration)))
                download_btn = QtGui.QPushButton(self.results)
                download_btn.setText('Download')
                download_btn.clicked.connect(self.download_song)
                self.results.setCellWidget(x, 5, download_btn)
def main():
    app = QtGui.QApplication(sys.argv)
    form = RipperApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
