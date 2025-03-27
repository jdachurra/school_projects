#ifndef INSTRUCTIONSDIALOG_HH
#define INSTRUCTIONSDIALOG_HH

#include <QDialog>

namespace Ui {
class InstructionsDialog;
}

class InstructionsDialog : public QDialog
{
    Q_OBJECT

public:
    explicit InstructionsDialog(QWidget *parent = nullptr);
    ~InstructionsDialog();

private slots:
    void on_pushButton_clicked();

private:
    Ui::InstructionsDialog *ui;
};

#endif // INSTRUCTIONSDIALOG_HH
