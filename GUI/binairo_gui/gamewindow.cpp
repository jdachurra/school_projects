#include "gamewindow.hh"
#include "ui_gamewindow.h"


#include <QCloseEvent>



#include <QGridLayout>
#include <QPushButton>
#include <QSignalMapper>

GameWindow::GameWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::GameWindow)
{
    ui->setupUi(this);
}

GameWindow::~GameWindow()
{
    delete ui;
}

void GameWindow::closeEvent(QCloseEvent *event)
{
    event->accept();
    parentWidget()->close();

}

void GameWindow::buttonClicked(QString coords)
{
    qDebug() << coords;
}


