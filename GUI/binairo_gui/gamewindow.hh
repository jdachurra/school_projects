#ifndef GAMEWINDOW_HH
#define GAMEWINDOW_HH

#include <QMainWindow>

namespace Ui {
class GameWindow;
}

class GameWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit GameWindow(QWidget *parent = nullptr);
    ~GameWindow();


private slots:
    void closeEvent(QCloseEvent *event);
    void buttonClicked(QString coords);

private:
    Ui::GameWindow *ui;
};

#endif // GAMEWINDOW_HH
