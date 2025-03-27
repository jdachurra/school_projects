/*BINAIRO GUI PROJECT
 *
 *
 *
 *
 * Description:
 *
 *   This program implements a Binairo GUI game with a customized gameboard
 * Each square in the gameboard has zero, one, or empty. The aim is to add
 * zeros and ones in the empty squares by following the rules:
 * - each horizontal and vertical line can have at most three identical numbers
 * - each horizontal and vertical line can have at most two identical number
 *   sequentially.
 *
 *   At first, the user is asked, if the gameboard will be filled with
 * randomly drawn characters, or with user-given character input as "1 001 ...". In the first
 * option, a seed value for the random number generator will be asked next.
 * If the player inputs an invalid setting, it will be displayed on-screen
 *
 *   On each round, the player can add a 0 or 1 by selecting in on-screen  The player wins if
 * the gameboard has been filled following the rules above. The program does
 * not allow additions violating the above rules, but it is possible to end up
 * to a situation where no addition is possible any more.
 *
 * Implementedfeatures can be found in-game (in "documentation") or in the instructions.cpp file
 * 
 * 
 * Program authors:
 *
 * Names:
 *        Jose Daniel Achurra Santos
 *
 * Student number:
 *        151487475
 *
 * UserID:
 *         tvjoac
 * E-Mail:
 *         jose.achurrasantos@tuni.fi
 *
 */


#include "mainwindow.hh"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
