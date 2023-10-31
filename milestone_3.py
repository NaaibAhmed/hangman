{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a802a56b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guess a letter: b\n",
      "You guessed: b\n"
     ]
    }
   ],
   "source": [
    "# Step 1: While loop\n",
    "while True:\n",
    "    # Step 2\n",
    "    guess = input(\"Guess a letter: \")\n",
    "\n",
    "    # Step 3: Check if the guess is a single alphabetical character\n",
    "    if guess.isalpha() and len(guess) == 1:\n",
    "        # Step 4: If the guess is valid, break out of the loop\n",
    "        break\n",
    "    else:\n",
    "        # Step 5: If the guess is invalid, print an error message\n",
    "        print(\"Invalid letter. Please, enter a single alphabetical character.\")\n",
    "\n",
    "# Print a message indicating that a valid guess was made\n",
    "print(f\"You guessed: {guess}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bde9baa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guess a letter: m\n",
      "Sorry, 'm' is not in the word. Try again.\n",
      "Guess a letter: a\n",
      "Good guess! 'a' is in the word.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# List of words\n",
    "word_list = [\"apple\", \"banana\", \"cherry\", \"strawberry\", \"mango\"]\n",
    "\n",
    "# Choose random word from the list\n",
    "secret_word = random.choice(word_list)\n",
    "\n",
    "#Step 1: If statement to check if the guess is in the word\n",
    "while True:\n",
    "    guess = input(\"Guess a letter: \")\n",
    "    \n",
    "    if guess.isalpha() and len(guess) == 1:\n",
    "        if guess in secret_word:\n",
    "            # Step 2: If the guess is in the word, print \"Good guess\"\n",
    "            print(f\"Good guess! '{guess}' is in the word.\")\n",
    "            break\n",
    "        else:\n",
    "            # Step 3: If the guess is not in the word, print\"Sorry, try again\" message\n",
    "            print(f\"Sorry, '{guess}' is not in the word. Try again.\")\n",
    "    else:\n",
    "        print(\"Invalid letter. Please, enter a single alphabetical character.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2e486dd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guess a letter: b\n",
      "Sorry, 'b' is not in the word. Try again.\n",
      "Guess a letter: c\n",
      "Good guess! 'c' is in the word.\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "# Word list\n",
    "word_list = [\"apple\", \"banana\", \"cherry\", \"strawberry\", \"mango\"]\n",
    "\n",
    "# random word from the list\n",
    "secret_word = random.choice(word_list)\n",
    "\n",
    "# Step 1: Function to check the guess\n",
    "def check_guess(guess):\n",
    "    # Step 2: lowercase\n",
    "    guess = guess.lower()\n",
    "    \n",
    "    # Step 3: Check if the guess is in the word\n",
    "    if guess in secret_word:\n",
    "        print(f\"Good guess! '{guess}' is in the word.\")\n",
    "        return True\n",
    "    else:\n",
    "        print(f\"Sorry, '{guess}' is not in the word. Try again.\")\n",
    "        return False\n",
    "\n",
    "# Step 1: input function\n",
    "def ask_for_input():\n",
    "    while True:\n",
    "        guess = input(\"Guess a letter: \")\n",
    "        if guess.isalpha() and len(guess) == 1:\n",
    "            # Step 3: Call the check_guess function to check if the guess is in the word\n",
    "            if check_guess(guess):\n",
    "                break\n",
    "        else:\n",
    "            print(\"Invalid letter. Please, enter a single alphabetical character.\")\n",
    "\n",
    "# Step 4: test the code\n",
    "ask_for_input()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8682a2de",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
