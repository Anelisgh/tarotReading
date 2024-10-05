import random
from enum import Enum

class TarotCard:
    def __init__(self, number, name, explanation):
        self.number = number
        self.name = name
        self.explanation = explanation

    def __str__(self):
        return f"{self.number}: {self.name} - {self.explanation}"


class TarotDeck:
    def __init__(self):
        self.cards = [
            TarotCard(0, "The Fool", "Represents new beginnings, innocence, and adventure. It encourages taking risks and embracing the unknown."),
            TarotCard(1, "The Magician", "Symbolizes manifestation, resourcefulness, and power. It signifies the ability to harness one's skills to achieve goals."),
            TarotCard(2, "The High Priestess", "Embodies intuition, subconscious knowledge, and mystery. It invites you to trust your instincts and inner voice."),
            TarotCard(3, "The Empress", "Represents femininity, fertility, and nurturing. It signifies abundance, growth, and the importance of nature."),
            TarotCard(4, "The Emperor", "Symbolizes authority, structure, and control. It represents leadership and the establishment of order."),
            TarotCard(5, "The Hierophant", "Embodies tradition, spirituality, and conformity. It often signifies seeking guidance or following established beliefs."),
            TarotCard(6, "The Lovers", "Represents love, harmony, and partnership. It signifies choices and the importance of relationships."),
            TarotCard(7, "The Chariot", "Symbolizes determination, willpower, and victory. It represents overcoming obstacles through focus and control."),
            TarotCard(8, "Strength", "Embodies courage, inner strength, and compassion. It signifies the power of patience and gentle persistence."),
            TarotCard(9, "The Hermit", "Represents introspection, solitude, and inner guidance. It signifies the search for deeper truths and self-discovery."),
            TarotCard(10, "Wheel of Fortune", "Symbolizes cycles, fate, and destiny. It represents the ups and downs of life and the importance of adaptability."),
            TarotCard(11, "Justice", "Embodies fairness, truth, and law. It signifies the importance of making balanced decisions and taking responsibility."),
            TarotCard(12, "The Hanged Man", "Represents surrender, letting go, and new perspectives. It signifies a pause to reflect before taking action."),
            TarotCard(13, "Death", "Symbolizes transformation, endings, and new beginnings. It represents the natural cycle of change and rebirth."),
            TarotCard(14, "Temperance", "Embodies balance, moderation, and harmony. It signifies the importance of finding equilibrium in life."),
            TarotCard(15, "The Devil", "Represents temptation, materialism, and bondage. It signifies confronting fears and unhealthy attachments."),
            TarotCard(16, "The Tower", "Symbolizes upheaval, chaos, and revelation. It represents sudden change that can lead to growth and clarity."),
            TarotCard(17, "The Star", "Embodies hope, inspiration, and renewal. It signifies healing and the importance of following your dreams."),
            TarotCard(18, "The Moon", "Represents illusion, intuition, and the subconscious. It signifies navigating through uncertainty and trusting your instincts."),
            TarotCard(19, "The Sun", "Symbolizes joy, success, and positivity. It represents happiness and the realization of goals."),
            TarotCard(20, "Judgment", "Embodies reflection, reckoning, and awakening. It signifies the need to evaluate past actions and make decisions for the future."),
            TarotCard(21, "The World", "Represents completion, achievement, and wholeness. It signifies the successful conclusion of a journey and the attainment of goals."),
        ]

    def draw_cards(self, num_cards):
        return random.sample(self.cards, num_cards)


class TarotReader:
    max_num = 5

    def __init__(self):
        self.deck = TarotDeck()

    def get_spread_choice(self):
        question = input("Would you like a classic tarot spread (1) or do you have a specific question (2)? Answer only with 1 or 2: ")
        return question.strip()

    def handle_classic_spread(self, choice):
        spreads = {
            "1": 3,  # Past, Present, Future
            "2": 3,  # Current situation, recommended action, expected outcome
            "3": 1,  # Relationship
            "4": 1,  # Job
            "5": 1   # Money
        }

        if choice in spreads:
            num_cards = spreads[choice]
            drawn_cards = self.deck.draw_cards(num_cards)
            print("Drawn Cards:")
            for card in drawn_cards:
                print(card)
        else:
            print("Invalid choice. Please choose a valid option.")

    def handle_specific_question(self):
        answer = input("What would you like to know? After your question write how many answers there should be. \nExample: My past, present and future. 3 \nYour question:  ")
        parts = answer.strip().split(" ")
        num_cards = int(parts[-1])
        
        if num_cards > self.max_num:
            print("Sorry, you can only get 5 questions at a time.")
        else:
            drawn_cards = self.deck.draw_cards(num_cards)
            print("Drawn Cards:")
            for card in drawn_cards:
                print(card)

    def run(self):
        while True:
            spread_choice = self.get_spread_choice()
            
            if spread_choice == "1":
                print("1. Past, Present, Future")
                print("2. Current situation, recommended action, expected outcome")
                print("3. Relationship")
                print("4. Job")
                print("5. Money")
                spread_number = input("Which one do you choose? Type the number: ")
                self.handle_classic_spread(spread_number)
            elif spread_choice == "2":
                self.handle_specific_question()
            else:
                print("Invalid input. Please try again.")

            another_question = input("Do you have another question? (yes/no): ").strip().lower()
            if another_question != 'yes':
                print("Thank you for using the tarot reading service. Goodbye!")
                break


if __name__ == "__main__":
    reader = TarotReader()
    reader.run()
