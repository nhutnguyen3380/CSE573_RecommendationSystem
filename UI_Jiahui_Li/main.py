"""
Created on April 9th, 2023, 7:17:16 PM

@author: Jiahui Li
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
from interface import Ui_RecommenderSystem
import sys
import pandas as pd

class MainWindow(QMainWindow, Ui_RecommenderSystem):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.comboBox.currentIndexChanged.connect(self.display)

    def display(self):
        new_rating = pd.read_csv('new_rating.csv')

        user_id = self.comboBox.currentText()

        names_str = '\n'.join(new_rating.loc[new_rating['userId'] == int(user_id), 'movieName'].values.tolist())

        self.RM_browser.setText(names_str)
        
        self.MF_browser.setText("Matrix Factorization")
        self.NCF_browser.setText("Neural Collaborative Filtering")



if __name__ == "__main__":
    ratings_raw = [item.strip().split("::") for item in open('ml-1m/ratings.dat', 'r').readlines()]
    movies_raw = [item.strip().split("::") for item in
                  open('ml-1m/movies.dat', 'r', encoding="ISO-8859-1").readlines()]

    movies = pd.DataFrame(movies_raw, columns=['movieId', 'title', 'genres'])
    ratings = pd.DataFrame(ratings_raw, columns=['userId', 'movieId', 'rating', 'timestamp'])
    ratings[['movieId', 'rating', 'userId']] = ratings[['movieId', 'rating', 'userId']].apply(pd.to_numeric)
    movies['movieId'] = movies['movieId'].apply(pd.to_numeric)

    name_dict = dict(zip(movies['movieId'], movies['title']))

    ratings['movieName'] = ratings['movieId'].map(name_dict)

    ratings.to_csv('new_rating.csv', index=False)

    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())
