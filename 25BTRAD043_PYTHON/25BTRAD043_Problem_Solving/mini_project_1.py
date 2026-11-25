{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "d1950ce1",
   "metadata": {},
   "source": [
    "Name : Jasaswini Sahu\n",
    "\n",
    "USN:25BTRAD043\n",
    "\n",
    "MINI PROJECT-1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9867222d",
   "metadata": {},
   "source": [
    "QUESTION:\n",
    "\n",
    "Unit Converter or Bill Generator\n",
    "\n",
    "CODE:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "350aa34d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===== UNIT CONVERTER =====\n",
      "\n",
      "----- RESULT -----\n",
      "Kilometers  : 12.0\n",
      "Meters      : 12000.0\n",
      "Centimeters : 1200000.0\n"
     ]
    }
   ],
   "source": [
    "print(\"===== UNIT CONVERTER =====\")\n",
    "\n",
    "kilometers = float(input(\"Enter distance in kilometers: \"))\n",
    "meters = kilometers * 1000\n",
    "centimeters = kilometers * 100000\n",
    "\n",
    "print(\"\\n----- RESULT -----\")\n",
    "print(\"Kilometers  :\", kilometers)\n",
    "print(\"Meters      :\", meters)\n",
    "print(\"Centimeters :\", centimeters)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv (3.9.6)",
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
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
