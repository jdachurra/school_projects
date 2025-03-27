#include <iostream>
#include "settingsdialog.hh"
#include "mainmodule.hh"
#include "gameboard.hh"
#include <QDebug>


using namespace std;
namespace mainmodule
{
// Muuttaa numeerisen merkkijonon vastaavaksi kokonaisluvuksi
// (kutsumalla stoi-funktiota) ja palauttaa tämän kokonaisluvun.
// Jos annettu merkkijono ei ollut numeerinen, palauttaa nollan.
//
// Converts the given numeric string to the corresponding integer
// (by calling stoi) & returns the integer.
// If the given string is ! numeric, returns zero.
unsigned int stoi_with_check(const std::string& str)
{
    bool is_numeric = true;
    ///este if lo agregue por si str = ""
    if (str.empty())
    {
        is_numeric = false;
    }
    for(unsigned int i = 0; i < str.length(); ++i)
    {
        if(! isdigit(str.at(i)))
        {
            is_numeric = false;
            break;
        }
    }
    if(is_numeric)
    {
        ///
        ///#include <QDebug>
        ///qDebug() << str.length();
        ///qDebug() << str;
        return stoi(str);
    }
    else
    {
        return 0;
    }
}

// Poistaa tyhjät merkit (kuten ' ') annetusta merkkijonosta.
// Palauttaa toden, jos annetussa merkkijonossa on täsmälleen yksi ei-tyhjä
// merkki, joka on '0' tai '1', muussa tapauksessa palauttaa epätoden.
//
// Removes empty characters (such as ' ' etc.) from the given string.
// Returns true if the given string has exactly one non-empty character,
// which is either '0' || '1', otherwise returns false.
bool find_fill_symbol(string& str)
{
    string fill_str = "";
    for(unsigned int i = 0; i < str.size(); ++i)
    {
        if(!isspace(str.at(i)))
        {
            fill_str += str.at(i);
        }
    }
    str = fill_str;
    return (fill_str.size() == 1 &&
           (fill_str.at(0) == '0' || fill_str.at(0) == '1'));
}

// Mahdollistaa pelin pelaamisen eli kysyy toistuvasti lisättävää merkkiä
// ja sen sijaintia, kunnes peli päättyy.
//
// Enables the user to play the game, i.e. by repeatedly asking an element
// to be added & its position, until the game is over.
string play_game(GameBoard& board, string coor, string fill_mode)
{
    //create a string from a single character with "{}"
    string x_str{coor[0]};
    string y_str{coor[2]};

        unsigned int x = stoi_with_check(x_str);
        unsigned int y = stoi_with_check(y_str);



        // Tässä kohdassa tiedetään, että syöte oli hyväksyttävä, mutta ei
        // ole varmaa, voidaanko annettu merkki lisätä annettuun kohtaan
        //
        // At this point, we know that the input is valid, but we don't know
        // if it is possible to add the given symbol on the given position
       /// --x;
        ///--y;

        if(!board.add_symbol(x, y, fill_mode[0]))
        {
            return "CANT_ADD";
        }

        // Jos annettu merkki voitiin lisätä, tulostetaan muuttunut pelilauta
        // If the given symbol was possible to add, print the changed gameboard

    // Jos peli päättyy täyteen pelilautaan, pelaaja voitti
    // If the game ends up to a totally filled gameboard, the player won
    else if(! board.is_game_over())
    {

        return "UPDATE";
    }
    else
    {

    return "WIN";
    }
}

// Kysyy käyttäjältä pelilaudan täyttötapaa.
// Palauttaa toden, jos pelilaudan täyttäminen onnistui,
// muuten palauttaa epätoden.
//
// Gives the user a possibility to select a filling way.
// Returns true if filling succeeded, otherwise returns false.

bool select_start(GameBoard& board, SettingsDialog &settings, QLabel* label_error)
{

    string choice = "";
    ////Por ejemplo, Aqui cambie el cin y cout, y lo conecte de una vez a lo de QT, como te estaba diciendo el otro dia.
    /*
    cout << "Select start (R for random, I for input): ";
    getline(cin, choice);
    */

    ///login here
    choice = settings.init_mode_;


    if(choice != "R" && choice != "r" && choice != "I" && choice != "i")
    {
        return false;
    }
    else if(choice == "R" || choice == "r")
    {
        string seed_string = "";
        ///cout << "Enter a seed value: ";
        ///getline(cin, seed_string);
        seed_string = settings.seed_;

        return board.fill_randomly(stoi_with_check(seed_string), label_error);
    }
    else // if(choice == "I" || choice == "i")
    {
        string input = "";
        ///cout << "Input: ";
        ///getline(cin, input);
        input = settings.text_board_;

        return board.fill_from_input(input, label_error);
    }
}

}
