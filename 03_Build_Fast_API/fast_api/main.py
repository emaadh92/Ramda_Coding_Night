from fastapi import FastAPI
import random

app = FastAPI()  # Define the FastAPI app first

side_hustles = [
    "Freelance Graphic Design",
    "Social Media Management",
    "Dropshipping Business",
    "Online Tutoring",
    "Content Writing",
    "Affiliate Marketing",
    "Handmade Crafts on Etsy"
]

money_quotes = [
    "The best investment is in yourself. Hustle: Start an online course or coaching business.",
    "Money grows on the tree of persistence. Hustle: Build a dropshipping store and scale it.",
    "Don’t watch the clock; do what it does—keep going. Hustle: Freelance writing or content creation.",
    "Opportunities don’t happen, you create them. Hustle: Launch a YouTube channel or podcast.",
    "The more you learn, the more you earn. Hustle: Offer consulting services in your expertise.",
    "Small steps every day lead to big results. Hustle: Sell digital products like eBooks or templates.",
    "Your time is money; invest it wisely. Hustle: Start a side hustle in affiliate marketing."
]

@app.get("/side_hustles")  # Decorator
def get_side_hustle(api_key: str):
    """Return a random side hustle"""
    if api_key != 1234567890:
        return {"error": "Invalid API Key"}
    return random.choice(side_hustles)

@app.get("/money_quotes")  # Decorator
def get_money_quote():
    """Return a random money quote"""
    return random.choice(money_quotes)