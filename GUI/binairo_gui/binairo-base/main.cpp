///#include "mainmodule.hh"
#include "mainmodule.cpp"

// Lyhyt ja yksinkertainen pääohjelma.
// Short & simple main function.
int main()
{
    GameBoard board;
    while(!select_start(board)); // ei toistettavaa koodia
                                    // no code to be repeated
    play_game(board);
    return 0;
}
