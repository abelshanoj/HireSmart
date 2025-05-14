from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import httpx
import asyncio

router = APIRouter()

class Answer(BaseModel):
 answers: dict

# Hardcoded questions and answers
# QUESTIONS = [
#     {"id": 1, "question": "What is 2 + 2?", "options": ["1", "2", "3", "4"], "answer": "4"},
#     {"id": 2, "question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "answer": "Paris"},
#     # Add 3 more questions as needed
# ]

# async def get_questions(count: int = 5):
#     global global_questions  # Use the global questions array
#     url = "https://aptitude-api.vercel.app/Random"
#     global_questions = []  # Clean the global array

#     try:
#         async with httpx.AsyncClient() as client:
#             for i in range(1, count + 1):  # Loop to fetch `count` questions
#                 response = await client.get(url)
#                 await asyncio.sleep(0.1)  # Small delay between requests
#                 response.raise_for_status()
                
#                 question_data = response.json()
#                 question_data["id"] = i  # Add the question number as "id"
#                 print(question_data["answer"])
#                 global_questions.append(question_data)

#         return global_questions

#     except httpx.RequestError as exc:
#         raise HTTPException(status_code=500, detail=f"An error occurred while connecting to the API: {exc}")
#     except httpx.HTTPStatusError as exc:
#         raise HTTPException(status_code=exc.response.status_code, detail=f"API error: {exc.response.text}")

# @router.get("/questions")
# async def fetch_questions(count: int = 5):
#     """
#     Fetches questions and updates the global array.
#     """
#     return await get_questions(count)

@router.post("/submit")
async def submit_answers(answers: Answer):
    """
    Submits answers and evaluates the user's score based on the global questions.
    """
    global global_questions  # Access the global questions array

    if not global_questions:
        raise HTTPException(status_code=400, detail="No questions available. Please fetch questions first.")

    # Evaluate score
    score = 0
    for question in global_questions:
        question_id = question["id"]
        correct_answer = question["answer"]
        user_answer = answers.answers.get(str(question_id))
        
        if user_answer == correct_answer:
            score += 1

    # Clear questions after evaluation (optional)
    global_questions = []

    return {"score": score, "total_questions": len(global_questions)}
