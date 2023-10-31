{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46181837",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'strawberry', 'mango']\n"
     ]
    }
   ],
   "source": [
    "favorite_fruits = [\"apple\", \"banana\", \"cherry\", \"strawberry\", \"mango\"]\n",
    "word_list = favorite_fruits\n",
    "print(word_list)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "26724ec9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "word_list = [\"apple\", \"banana\", \"cherry\", \"strawberry\", \"mango\"]\n",
    "word = random.choice(word_list)\n",
    "print(word)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "96d1e846",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a single letter: 2\n",
      "Oops! That is not a valid input.\n"
     ]
    }
   ],
   "source": [
    "guess = input(\"Please enter a single letter: \")\n",
    "if len(guess) == 1 and guess.isalpha():\n",
    "    print(\"Good guess!\")\n",
    "else:\n",
    "    print(\"Oops! That is not a valid input.\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4fa553c5",
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
