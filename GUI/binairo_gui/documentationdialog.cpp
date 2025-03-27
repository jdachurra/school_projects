#include "documentationdialog.hh"
#include "ui_documentationdialog.h"

DocumentationDialog::DocumentationDialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::DocumentationDialog)
{
    ui->setupUi(this);
}

DocumentationDialog::~DocumentationDialog()
{
    delete ui;
}

void DocumentationDialog::on_pushButton_clicked()
{
    //quit dialog
    this->close();
}

