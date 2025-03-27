#ifndef SETTINGSDIALOG_HH
#define SETTINGSDIALOG_HH

#include <QDialog>
#include "gamewindow.hh"
#include "qlabel.h"
#include "binairo-base/gameboard.hh"
#include "qradiobutton.h"
#include "qtimer.h"

//Input variables

namespace Ui {
class SettingsDialog;
}

class SettingsDialog : public QDialog
{
    Q_OBJECT

public:
    explicit SettingsDialog(QWidget *parent = nullptr);
    ~SettingsDialog();

    ///commit variables
    GameBoard* board_object;
    uint board_size_;
    uint number_of_symbols_;
    std::string seed_;
    std::string text_board_;
    std::string file_input_;
    std::string init_mode_;
    GameWindow* gamewindow;

    QTimer* timer_;
    std::string fill_mode_;




private slots:
    //slot for when a coordinate button is clicked
    //@param coords: coordinates of the button clicked
    //@param button: pointer to the button clicked
    void buttonClicked(QString coords, QPushButton* button); ///////

    //slot for when the pushbutton is clicked
    void on_pushButton_clicked();

    //Auto Deletes the dialog object
    void closeEvent(QCloseEvent *event);

    //slot for when the radioButton_4 is toggled
    void on_radioButton_4_toggled(bool checked);

    //slot for when the radioButton_5 is toggled
    void on_radioButton_5_toggled(bool checked);

    //slot for when the spinbox value is changed
    void on_spinBox_valueChanged(int arg1);



    void on_radioButton_toggled(bool checked);

    void on_radioButton_2_toggled(bool checked);

    void on_pushButton_2_clicked();

    void on_lineEdit_textChanged(const QString &arg1);

    void on_lineEdit_2_textChanged(const QString &arg1);

    //void setTimerLabelText(QLabel* timer_label);

    void restartButtonClicked();
    void radioButton0Toggled(bool checked, QRadioButton* button_restart);
    void radioButton1Toggled(bool checked, QRadioButton* button_restart);

private:
    Ui::SettingsDialog *ui;
    ///change play status with Qt::CustomizeWindowHint
    bool play_status;
};

#endif // SETTINGSDIALOG_HH
