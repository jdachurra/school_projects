QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    documentationdialog.cpp \
    gamewindow.cpp \
    instructionsdialog.cpp \
    main.cpp \
    mainwindow.cpp \
    instructions.cpp \
    binairo-base/gameboard.cpp \
    binairo-base/mainmodule.cpp \
    settingsdialog.cpp



HEADERS += \
    documentationdialog.hh \
    gamewindow.hh \
    instructionsdialog.hh \
    mainwindow.hh \
    binairo-base/gameboard.hh \
    binairo-base/mainmodule.hh \
    settingsdialog.hh

FORMS += \
    documentationdialog.ui \
    gamewindow.ui \
    instructionsdialog.ui \
    mainwindow.ui \
    settingsdialog.ui


# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
