#ifndef DOCUMENTATIONDIALOG_HH
#define DOCUMENTATIONDIALOG_HH

#include <QDialog>

namespace Ui {
class DocumentationDialog;
}

class DocumentationDialog : public QDialog
{
    Q_OBJECT

public:
    explicit DocumentationDialog(QWidget *parent = nullptr);
    ~DocumentationDialog();

private slots:
    void on_pushButton_clicked();

private:
    Ui::DocumentationDialog *ui;
};

#endif // DOCUMENTATIONDIALOG_HH
