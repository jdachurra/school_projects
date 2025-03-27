#ifndef GAMEBOARD_CPP
#define GAMEBOARD_CPP

#include "gameboard.hh"

#include <iostream>
#include <random>




GameBoard::GameBoard(uint board_size_temp, uint number_of_symbols_temp)
{
    board_size = board_size_temp;
    number_of_symbols = number_of_symbols_temp;
    init();
}


///added destructor: erase de board from memory
GameBoard::~GameBoard()
{
 board_.clear(); ///is this line redundant? i dont know, i cant find any info online
}




bool GameBoard::fill_randomly(unsigned int seed, QLabel *label_error)
{
    // Checking the validity of the given seed
    for(unsigned int bad_seed : BAD_SEEDS)
    {
        if(seed == bad_seed)
        {   label_error->setText("Bad seed");
            ///std::cout << "Bad seed" << std::endl;
            return false;
        }
    }

    // Constructing a string with random symbols
    std::default_random_engine eng(seed);
    std::uniform_int_distribution<unsigned int> distr(0, DISTR_UPPER_BOUND);
    std::string input = "";

    for(unsigned int i = 0; i < board_size * board_size; ++i)
    {
        switch(distr(eng))
        {
        case 0: input += '0'; break;
        case 1: input += '1'; break;
        default: input += ' '; break;
        }
    }

    // Calling fill_from_input with the constructed string (enclosed with quote
    // marks), whereupon the return value of fill_from_input will be true
    ///added label_error here too
    return fill_from_input('"' + input + '"' , label_error);
}

std::vector<std::vector<Element_type>> GameBoard::getBoardVector() const
{
    return board_;
}

bool GameBoard::fill_from_input(const std::string &input, QLabel *label_error)
{
    // Checking the size (assuming that input is enclosed with quote marks)
    if(input.size() != board_size * board_size + 2)
    {
        label_error->setText("Wrong size of input");
        ///std::cout << "Wrong size of input" << std::endl;
        return false;
    }

    // Removing quote marks
    std::string actual_input = input.substr(1, board_size * board_size);

    // Checking the content && moving each element on the gameboard
    for(unsigned int i = 0; i < board_size * board_size; ++i)
    {
        Element_type current_element = EMPTY;
        switch(actual_input.at(i))
        {
        case '0':
            current_element = ZERO; break;
        case '1':
            current_element = ONE; break;
        case ' ':
            current_element = EMPTY; break;
        default:
            label_error->setText("Wrong character");
            ///std::cout << "Wrong character" << std::endl;
            return false;
        }

        board_.at(i / board_size).at(i % board_size ) = current_element;
    }
    if(ok_adjacent_symbols() && ok_amount_of_symbols())
    {
        return true;
    }
    else
    {
        label_error->setText("Bad input");
        ///std::cout << "Bad input" << std::endl;
        return false;
    }
}

bool GameBoard::ok_adjacent_symbols() const
{
    return ok_adjacent_syms_in_rows(ZERO) &&
           ok_adjacent_syms_in_rows(ONE) &&
           ok_adjacent_syms_in_columns(ZERO) &&
           ok_adjacent_syms_in_columns(ONE);
}

bool GameBoard::ok_amount_of_symbols() const
{
    unsigned int zeros_in_row = 0;
    unsigned int ones_in_row = 0;
    unsigned int zeros_in_column = 0;
    unsigned int ones_in_column = 0;

    for(unsigned int i = 0; i < board_.size(); ++i)
    {
        for(unsigned int j = 0; j < board_.at(i).size(); ++j)
        {
            if(board_.at(i).at(j) == ZERO)
            {
                ++zeros_in_row;
            }
            else if(board_.at(i).at(j) == ONE)
            {
                ++ones_in_row;
            }
            if(board_.at(j).at(i) == ZERO)
            {
                ++zeros_in_column;
            }
            else if(board_.at(j).at(i) == ONE)
            {
                ++ones_in_column;
            }
        }
        if(zeros_in_row > number_of_symbols ||
           ones_in_row > number_of_symbols ||
           zeros_in_column > number_of_symbols ||
           ones_in_column > number_of_symbols)
        {
            return false;
        }
        zeros_in_row = ones_in_row = zeros_in_column = ones_in_column = 0;
    }
    return true;
}

bool GameBoard::add_symbol(unsigned int x, unsigned int y, char symbol_char)
{
    if(board_.at(y).at(x) != EMPTY)
    {
        //std::cout << "Not empty: ";
        return false;
    }

    Element_type elem = EMPTY;
    switch(symbol_char)
    {
    case '0': elem = ZERO; break;
    case '1': elem = ONE; break;
    default: return false; // This should never happen, checked in main.cpp
    }

    // Adding the symbol && checking if everything is still fine
    board_.at(y).at(x) = elem;
    if(ok_adjacent_symbols() &&
       ok_amount_of_symbols())
    {
        return true;
    }
    // If all was not fine after adding, making the index empty again
    else
    {
        board_.at(y).at(x) = EMPTY;
        return false;
    }
}

bool GameBoard::is_game_over() const
{
    for(unsigned int i = 0; i < board_.size(); ++i)
    {
        for(unsigned int j = 0; j < board_.at(i).size(); ++j)
        {
            if(board_.at(i).at(j) == EMPTY)
            {
                return false;
            }
        }
    }
    return true;
}

void GameBoard::print() const
{

    // Tulostetaan pelilaudan varsinainen sisältö
    // Printing the actual content of the gameboard
    for(unsigned int i = 0; i < board_size; ++i)
    {
        for(unsigned int j = 0; j < board_size; ++j)
        {
            switch(board_.at(i).at(j))
            {
            case ZERO:
                std::cout << "0 ";
                break;
            case ONE:
                std::cout << "1 ";
                break;
            case EMPTY:
                std::cout << "  ";
                break;
            }
        }
        std::cout << "|" << std::endl;
    }


}

void GameBoard::init()
{
    std::vector<Element_type> row(board_size, EMPTY);
    for(unsigned int i = 0; i < board_size; ++i)
    {
        board_.push_back(row);
    }
}


bool GameBoard::ok_adjacent_syms_in_rows(Element_type elem) const
{
    for(unsigned int i = 0; i < board_.size(); ++i)
    {
        for(unsigned int j = 0; j < board_.at(i).size() - 2; ++j)
        {
            if(board_.at(i).at(j) == elem &&
               board_.at(i).at(j + 1) == elem &&
               board_.at(i).at(j + 2) == elem)
            {
                return false;
            }
        }
    }
    return true;
}

bool GameBoard::ok_adjacent_syms_in_columns(Element_type elem) const
{
    for(unsigned int i = 0; i < board_.size() - 2; ++i)
    {
        for(unsigned int j = 0; j < board_.at(i).size(); ++j)
        {
            if(board_.at(i).at(j) == elem &&
               board_.at(i + 1).at(j) == elem &&
               board_.at(i + 2).at(j) == elem)
            {
                return false;
            }
        }
    }
    return true;
}

#endif // GAMEBOARD_CPP

