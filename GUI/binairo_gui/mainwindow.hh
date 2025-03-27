#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include "settingsdialog.hh"


#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE



class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

    bool restart = false;



    ///can this go private?
    SettingsDialog* settings_dialog;




private slots:
    void on_pushButton_clicked();

    void on_pushButton_3_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_4_clicked();

private:
    Ui::MainWindow *ui;


};
#endif // MAINWINDOW_HH
