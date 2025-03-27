        #include "settingsdialog.hh"
#include "ui_settingsdialog.h"
#include "binairo-base/mainmodule.cpp"
#include "gamewindow.hh"
#include "binairo-base/gameboard.hh"
///quite el gameboard include
#include <QCloseEvent>

#include <QGridLayout>
#include <QPushButton>
#include <QSignalMapper>
#include <QTimer>



SettingsDialog::SettingsDialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::SettingsDialog)
{
    ui->setupUi(this);


    ui->label_5->setText(QString::number(BOARD_SIZE_DEF));
    board_size_ = BOARD_SIZE_DEF;
    number_of_symbols_ = NUMBER_OF_SYMBOLS_DEF;
    seed_ = "";
    text_board_ = "";
    file_input_ = "";
    init_mode_ = "";
    play_status = false;



}

SettingsDialog::~SettingsDialog()
{
    delete ui;
}

void SettingsDialog::closeEvent(QCloseEvent *event)
{

        parentWidget()->show();
        event->accept();

}


void SettingsDialog::on_pushButton_clicked()
{

    parentWidget()->show();
    this->close();

}



void SettingsDialog::on_radioButton_4_toggled(bool checked)
{
    if (checked)
    {
        board_size_ = BOARD_SIZE_DEF;
    }
}


void SettingsDialog::on_radioButton_5_toggled(bool checked)
{

    ui->spinBox->setReadOnly(!checked);
}


void SettingsDialog::on_spinBox_valueChanged(int arg1)
{
    board_size_ = arg1;
}


void SettingsDialog::on_radioButton_toggled(bool checked)
{
    if (checked)
    {
        init_mode_ = "R";
        ui->lineEdit->setReadOnly(false);
    }
    else
    {
        ui->lineEdit->setReadOnly(true);
    }

}


void SettingsDialog::on_radioButton_2_toggled(bool checked)
{
    if (checked)
    {
        init_mode_ = "I";
        ui->lineEdit_2->setReadOnly(false);
    }
    else
    {
        ui->lineEdit_2->setReadOnly(true);
    }
}


void SettingsDialog::on_pushButton_2_clicked()
{


    board_object = new GameBoard(board_size_, number_of_symbols_);
    if (!mainmodule::select_start(*board_object, *this, ui->label_error))
    {


        if (ui->label_error->text() == "---------")
        {
            ui->label_error->setText("Invalid input");
        }

        delete board_object;

    }
    else
    {


        gamewindow = new GameWindow(this);
        play_status = true;
        this->hide();

        //gamewindow->initializeBorad(board_size_, board_size_);


            QGridLayout *gridLayout = new QGridLayout;

            for(uint i = 0; i <board_size_; ++i)
            {
                for(uint j = 0; j < board_size_; ++j)
                {
                    QPushButton *button = new QPushButton;
                    button->setText("");
                    button->setObjectName(QString::number(i) + "," + QString::number(j));


                    gridLayout->addWidget(button, i, j);

                    connect(button, &QPushButton::clicked, this, [this, button]() {
                        buttonClicked(button->objectName(), button);
                    });
                }
            }


            // Create the main layout
            QHBoxLayout *mainLayout = new QHBoxLayout;

            // Create the grid layout and add it to the main layout
            QWidget *gridWidget = new QWidget;
            gridWidget->setLayout(gridLayout);
            mainLayout->addWidget(gridWidget);


            // Create the controller layout and add it to the main layout
            QVBoxLayout *controllerLayout = new QVBoxLayout;

            //adding 2 radiobuttons and a pushbutton
            QRadioButton *radioButton0 = new QRadioButton("0");
            controllerLayout->addWidget(radioButton0);
            //radioButton0 is activated by default
            fill_mode_ = "0";
            radioButton0->setChecked(true);
            QRadioButton *radioButton1 = new QRadioButton("1");
            controllerLayout->addWidget(radioButton1);

            QPushButton *button_restart = new QPushButton("restart");
            controllerLayout->addWidget(button_restart);

            //connect each widget with a function
            connect(radioButton0, &QRadioButton::toggled, this, [this, radioButton0]() {
                radioButton0Toggled(radioButton0->isChecked(), radioButton0);
            });
            connect(radioButton1, &QRadioButton::toggled, this, [this, radioButton1]() {
                radioButton1Toggled(radioButton1->isChecked(), radioButton1);
            });


            connect(button_restart, &QPushButton::clicked, this, [this]() {
                restartButtonClicked();
            });


            static int time_start = 0;
            //add the timer as a label
            QLabel *timer_label = new QLabel("Time:");
            controllerLayout->addWidget(timer_label);
            timer_ = new QTimer(this);
            connect(timer_, &QTimer::timeout, this, [timer_label](){
                timer_label->setText(QString::number(time_start++));
            });
            timer_->start(1000);


            // Add the controller layout to the main layout
            QWidget *controllerWidget = new QWidget;
            controllerWidget->setLayout(controllerLayout);
            mainLayout->addWidget(controllerWidget);

            // Set the main layout as the layout of the central widget
            QWidget *centralWidget = new QWidget;
            centralWidget->setLayout(mainLayout);
            gamewindow->setCentralWidget(centralWidget);

        gamewindow->show();

        for(unsigned int i = 0; i < board_size_; ++i)
        {
        for(unsigned int j = 0; j < board_size_; ++j)
        {
            switch(board_object->getBoardVector().at(i).at(j))
            {
            case ZERO:
                static_cast<QPushButton*>(gridLayout->itemAtPosition(i,j)->widget())->setText("0");
                static_cast<QPushButton*>(gridLayout->itemAtPosition(i,j)->widget())->setEnabled(false);
                break;
            case ONE:
                static_cast<QPushButton*>(gridLayout->itemAtPosition(i,j)->widget())->setText("1");
                static_cast<QPushButton*>(gridLayout->itemAtPosition(i,j)->widget())->setEnabled(false);
                break;
            case EMPTY:
                break;
            }

        }
        }




    }
}



void SettingsDialog::buttonClicked(QString coords, QPushButton* button)
{
    qDebug() << coords;

    std::string update_value = mainmodule::play_game(*board_object, coords.toStdString(), fill_mode_);
    qDebug() << QString::fromStdString(update_value);
    //3 things can be returned: "UPDATE", WIN, or CANT_ADD
    if(update_value == "UPDATE")
    {
        //update the board
        button->setText(QString::fromStdString(fill_mode_));
        button->setDisabled(true);
    }
    else if(update_value == "WIN")
    {
        //update the board
        button->setText(QString::fromStdString(fill_mode_));
        button->setDisabled(true);
        //change window title to "YOU WIN"
        gamewindow->setWindowTitle("YOU WIN");
        //change gamedialog background color to green
        gamewindow->setStyleSheet("background-color: green");
        //stop the timer in the settings dialog
        timer_->stop();




    }
    else if (update_value == "CANT_ADD")
    {
       //set the button to red for 1 second
       button->setStyleSheet("background-color: red");
       QTimer::singleShot(1000, [button](){
           button->setStyleSheet("");
       });

    }


}


void SettingsDialog::radioButton0Toggled(bool checked, QRadioButton *radioButton)
{
    qDebug() << radioButton->text();
    if (checked)
    {

      fill_mode_  = "0";
    }

}

void SettingsDialog::radioButton1Toggled(bool checked, QRadioButton *radioButton)
{
    qDebug() << radioButton->text();
    if (checked)
    {

        fill_mode_  = "1";
    }
}


void SettingsDialog::restartButtonClicked()
{
  //send a signal to the parent widget to open the settings window again and start the game with the same settings
    qDebug() << "restart";
}


void SettingsDialog::on_lineEdit_textChanged(const QString &arg1)
{
    seed_ = arg1.toStdString();
}


void SettingsDialog::on_lineEdit_2_textChanged(const QString &arg1)
{
    text_board_ = arg1.toStdString();
}




