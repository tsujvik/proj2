from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# static html
app.mount("/static", StaticFiles(directory="static"), name="static")

board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        return board[0][2]
    return None

def check_draw():
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True


@app.get("/", response_class=HTMLResponse)
async def get_game():
    with open("static/index.html", "r") as f:
        content = f.read()
    return content

@app.post("/move/{row}/{col}")
async def make_move(row: int, col: int):
    global current_player
    if board[row][col] == '':
        board[row][col] = current_player
        winner = check_winner()
        if winner:
            return {"status": "win", "winner": winner}
        elif check_draw():
            return {"status": "draw"}
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
        return {"status": "continue"}
    else:
        return {"status": "invalid"}
    
@app.get("/reset")
async def reset_game():
    global board, current_player
    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    return {"status": "reset"}
