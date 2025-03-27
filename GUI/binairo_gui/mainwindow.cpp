#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include "instructionsdialog.hh"
#include "documentationdialog.hh"

///this goes in .hh instead of .cpp, because we are not doing the .exec()
/*
#include "settingsdialog.hh"
#include "gamewindow.hh"
*/


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}



void MainWindow::on_pushButton_clicked()
{
    //Initialize settings dialog

    settings_dialog = new SettingsDialog(this);
    this->hide();

    //START EVERYTHING
    ///these may be changed to exec() so it auto-deletes when closing
    settings_dialog->show();



}


void MainWindow::on_pushButton_3_clicked()
{
    QApplication::quit();
}


void MainWindow::on_pushButton_2_clicked()
{
    InstructionsDialog instr_dialog;
    instr_dialog.setModal(true);
    this->hide();
    instr_dialog.exec();
    this->show();


}





void MainWindow::on_pushButton_4_clicked()
{
    DocumentationDialog doc_dialog;
    doc_dialog.setModal(true);
    this->hide();
    doc_dialog.exec();
    this->show();
}

