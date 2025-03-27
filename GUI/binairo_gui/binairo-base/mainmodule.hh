#ifndef MAINMODULE_HH
#define MAINMODULE_HH

#include "gameboard.hh"
#include "settingsdialog.hh"

using namespace std;

namespace mainmodule
{

const string QUIT;
const string OUT_OF_BOARD;
const string INVALID_INPUT;
const string CANT_ADD;
const string WIN;

unsigned int stoi_with_check(const std::string& str);

bool find_fill_symbol(string& str);

string play_game(GameBoard& board, std::string coor, std::string fill_mode);

bool select_start(GameBoard& board, SettingsDialog &settings, QLabel* label_error);
}

#endif // MAINMODULE_HH
