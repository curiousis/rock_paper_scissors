from fastapi import FastAPI
import random

app = FastAPI()
sessions = []
active_sessions = {}


@app.get("/api/start_session")
async def start_session():
    random_list = [str(random.randint(0, 9)) for _ in range(6)]
    session_id = "".join(random_list)
    sessions.append(session_id)
    return {"session_id": session_id, "message": f"session {session_id} created"}


@app.get("/api/join_session")
async def join_session(username, session_id):
    if session_id not in sessions:
        return {"error, session id not found"}

    print(active_sessions)
    if session_id in active_sessions:
        print(active_sessions[session_id])

    if session_id not in active_sessions:
        active_sessions[session_id] = [
            {
                "username": username,
                "choice": random.choice(["rock", "paper", "scissors"]),
            }
        ]
        return {"data": active_sessions}
    elif (
        len(active_sessions[session_id]) < 2
        and username not in active_sessions[session_id]
    ):
        active_sessions[session_id].append(
            {
                "username": username,
                "choice": random.choice(["rock", "paper", "scissors"]),
            }
        )
        return {"data": active_sessions}
    else:
        return {"message": "error, session full, or username already in use"}


@app.get("/api/session_info")
async def session_info(session_id):
    try:
        if session_id in active_sessions:
            user1 = active_sessions[session_id][0]
            user2 = active_sessions[session_id][1]
            user1_username = user1["username"]
            user2_username = user2["username"]
            user1_choice = user1["choice"]
            user2_choice = user2["choice"]

            if user1_choice == user2_choice:
                return {"result": "draw"}
            elif user1_choice == "rock" and user2_choice == "scissors":
                return {"result": f"{user1_username} won!"}
            elif user1_choice == "scissors" and user2_choice == "paper":
                return {"result": f"{user1_username} won!"}
            elif user1_choice == "paper" and user2_choice == "rock":
                return {"result": f"{user1_username} won!"}
            else:
                return {"result": f"{user2_username} won!"}
        else:
            return {"error": "error, session not found"}
    except KeyError:
        return {"error": "error, session not found"}
