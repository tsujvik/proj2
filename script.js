let currentPlayer = 'X';
let board = ['', '', '', '', '', '', '', '', ''];
let gameActive = true;

const cells = document.querySelectorAll('.cell');
const resetButton = document.getElementById('resetBtn');

var checkWinner = () => {
    const winPatterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // vertical wins
        [0, 4, 8], [2, 4, 6] // diagonel wins
    ];

    for (let pattern of winPatterns) {
        const [a, b, c] = pattern;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            gameActive = false;
            setTimeout(() => alert(`${currentPlayer} wins!`), 100);
            return true;
        }
    }
    return false;
};


const handleCellClick = (index) => {
    if (!gameActive || board[index] !== '') return;

    board[index] = currentPlayer;
    cells[index].textContent = currentPlayer;

    if (!checkWinner()) {
        currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
    }
};

const resetGame = () => {
    gameActive = true;
    currentPlayer = 'X';
    board = ['', '', '', '', '', '', '', '', ''];
    cells.forEach(cell => cell.textContent = '');
};

cells.forEach(cell => {
    cell.addEventListener('click', () => {
        const index = cell.getAttribute('data-index');
        handleCellClick(index);
    });
});


resetButton.addEventListener('click', resetGame);
