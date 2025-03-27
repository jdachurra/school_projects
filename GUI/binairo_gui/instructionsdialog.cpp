#include "instructionsdialog.hh"
#include "ui_instructionsdialog.h"

InstructionsDialog::InstructionsDialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::InstructionsDialog)
{
    ui->setupUi(this);
}

InstructionsDialog::~InstructionsDialog()
{
    delete ui;
}

void InstructionsDialog::on_pushButton_clicked()
{
    this->close();
}

