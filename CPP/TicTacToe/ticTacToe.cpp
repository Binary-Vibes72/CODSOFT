#include <iostream>
#include <vector>

using namespace std;

// Function to display the Tic Tac Toe board
void displayBoard(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            cout << cell << " ";
        }
        cout << endl;
    }
}

// Function to check if a player has won
bool checkWin(const vector<vector<char>>& board, char player) {
    // Check rows and columns
    for (int i = 0; i < 3; ++i) {
        if (board[i][0] == player && board[i][1] == player && board[i][2] == player)
            return true; // Row win
        if (board[0][i] == player && board[1][i] == player && board[2][i] == player)
            return true; // Column win
    }

    // Check diagonals
    if (board[0][0] == player && board[1][1] == player && board[2][2] == player)
        return true; // Diagonal win
    if (board[0][2] == player && board[1][1] == player && board[2][0] == player)
        return true; // Diagonal win

    return false;
}

// Function to check if the board is full (a tie)
bool checkTie(const vector<vector<char>>& board) {
    for (const auto& row : board) {
        for (char cell : row) {
            if (cell == ' ')
                return false; // If any cell is empty, the game is not a tie
        }
    }
    return true; // All cells are filled, the game is a tie
}

// Function to make a move on the board
void makeMove(vector<vector<char>>& board, int row, int col, char player) {
    if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
        cout << "Invalid move! Try again." << endl;
    } else {
        board[row][col] = player;
    }
}

int main() {
    vector<vector<char>> board(3, vector<char>(3, ' ')); // Initialize an empty 3x3 board
    char currentPlayer = 'X';

    while (true) {
        cout << "Current board:" << endl;
        displayBoard(board);

        int row, col;
        cout << "Player " << currentPlayer << ", enter your move (row and column): ";
        cin >> row >> col;

        makeMove(board, row, col, currentPlayer);

        if (checkWin(board, currentPlayer)) {
            cout << "Player " << currentPlayer << " wins!" << endl;
            break;
        } else if (checkTie(board)) {
            cout << "It's a tie!" << endl;
            break;
        }

        // Switch to the other player for the next turn
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    return 0;
}
